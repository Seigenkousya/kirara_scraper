#-*-coding:utf-8 -*-
import re
import regex
import sys
import requests
import collections
from bs4 import BeautifulSoup
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

month_list=['Jan.','Feb.','Mar.','Apr.','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.']
mid_list=['642', '646', '650', '654', '658', '662', '666', '670', '674', '678', '682', '686', '690', '694', '698', '702', '706', '710', '714', '718', '722','726','730','734']
bottom=24
mid=187
year=2019
month=1
index=0

mark_point_x=[]
mark_point_y=[]
mark_point_color=[]
color_cycle=plt.rcParams['axes.prop_cycle'].by_key()['color']

center_colors=[]
center_color_all=[]
count_cc={}

date_list=[]
date_place=[]


class Article:
    def __init__(self,_label,_keyword):
        self.label=_label
        self.keyword=_keyword
        self.list=[]
        self.center_list=[]

    def is_centercolor(self,center_colors):
        flag=False
        for cc in center_colors:
            if self.keyword in cc:
                flag=True
                break
        
        self.center_list.append(flag)
        return flag

Article_list=[  Article("bozaro","ぼっち"),
                Article("syachiku","社畜さん"),
                Article("umirie","旅する海と"),
                Article("syouko","しょうこセンセイ"),
                Article("kinmoza","きんいろ"),
                Article("gochiusa","ご注文は"),
                Article("comic_girls","こみっくが"),
                Article("stella","ステラのまほう")]
                
while index < len(mid_list):

    print ("\n{}年{}月号".format(year,month))
    
    date_list.append(str(year)+"\n"+month_list[month-1]);
    date_place.append(index)

    url='http://www.dokidokivisual.com/magazine/max/book/index.php?mid={0}'.format(mid_list[index])
    html=requests.get(url)

    source=BeautifulSoup(html.content,"html.parser")

    strongs=source.find_all("strong")

    center_colors=[]
    for i in range(0,len(strongs),2):
        _result=re.search('センターカラー|巻頭カラー',strongs[i].text)
        if _result!= None:
            center_colors.append(re.search('『.+』',strongs[i+1].text).group())
            center_color_all.append(center_colors[-1])

    print(center_colors)
    
    span=source.find_all("font",color="#8000FF")

    i=0
    for tag in span:
        try:
            i+=1
            name=tag.string
            
            print(i,name)

            for color_index,art in enumerate(Article_list):
                if art.keyword in name and len(art.list)==index:
                    art.list.append(i)
                    if art.is_centercolor(center_colors):
                        mark_point_x.append(index)
                        mark_point_y.append(i)
                        mark_point_color.append(color_cycle[color_index])
        
        except:
            pass 

    for art in Article_list:
        if len(art.list)==index:
            art.list.append(None)
            art.center_list.append(None)

    index+=1

    if month==12:
        year+=1
        month=1
    else:
        month+=1


    sleep(1)

print(collections.Counter(center_color_all))

for art in Article_list:
    print(art.label)
    print(art.center_list)

X_list=list(range(len(mid_list)))
plt.xlabel('Publication issue')
plt.ylabel('Publication order')
plt.title('Changes in the order of publication')

"""
for art in Article_list:
    plt.plot(X_list, art.list, '.', linestyle='solid', marker="D", markevery=art.mark_point ,label=art.label)
"""
for art in Article_list:
    plt.plot(X_list, art.list, linestyle='solid', marker=".", label=art.label)

print(mark_point_x)
print(mark_point_y)
print(mark_point_color)
for _x,_y,_color in zip(mark_point_x,mark_point_y,mark_point_color):
    plt.plot(_x, _y, linestyle='none', marker='D', color=_color)

plt.gca().invert_yaxis()
plt.grid(color='gray')
plt.legend(bbox_to_anchor=(1.02,1),loc='upper left',borderaxespad=0)
plt.subplots_adjust(right=0.7)
plt.xticks(date_place,date_list)
plt.yticks(range(1,bottom))
plt.show()
