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

month_list=['Jan.','Feb.','Mar.','Apr.','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.'];
mid_list=['187', '191', '195', '199', '203', '207', '211', '215', '219', '223', '227', '231', '235', '239', '244', '249', '254', '259', '264', '269', '274', '279', '284', '289', '294', '299', '304', '309', '314', '319', '324', '329', '334', '340', '345', '350', '355', '360', '362', '370', '375', '380', '385', '390', '395', '400', '405', '410', '415', '420', '425', '430', '435', '440', '445', '450', '455', '460', '465', '470', '475', '480', '485', '490', '495', '500', '505', '510', '514', '520', '525', '530', '535', '540', '545', '550', '555', '560', '565', '570', '575', '580', '585', '590', '594', '598', '602', '606', '610', '614', '618', '622', '626', '630', '634', '638', '642', '646', '650', '654', '658', '662', '666', '670', '674', '678', '682', '686', '690', '694', '698', '702']
bottom=24
mid=187
year=2011
month=1
index=0

mark_point_x=[]
mark_point_y=[]
mark_point_color=[]
color_cycle=plt.rcParams['axes.prop_cycle'].by_key()['color']

center_colors=[]
center_color_all=[]

date_list=[]
date_place=[]
error_list=[]

class Article:
    def __init__(self,_label,_keyword):
        self.label=_label
        self.keyword=_keyword
        self.list=[]
        self.center_list=[]
        self.count_cc=0
        self.count_article=0

    def is_centercolor(self,center_colors):
        flag=False
        for cc in center_colors:
            if self.keyword in cc:
                flag=True
                self.count_cc+=1
                break
        
        self.center_list.append(flag)
        return flag

Article_list=[  Article("doubiju","どうして私が美術科に"),
                Article("kinmoza","きんいろ"),
                Article("gochiusa","ご注文は"),
                Article("comic_girls","こみっくが"),
                Article("stella","ステラのまほう")]
                
while index < len(mid_list):

    print ("\n{}年{}月号".format(year,month))
    
    if month==1 or month==5 or month==9:
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
            try:
                center_colors.append(re.search('(「|『).+(」|』)',strongs[i+1].text).group())
                center_color_all.append(center_colors[-1])
            except:
                print("Not Found.")
                error_list.append("{}年{}月号".format(year,month))

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
                    art.count_article+=1
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

print(Article_list[2].count_cc)
print(Article_list[2].count_article-36)
print(Article_list[2].count_cc/(Article_list[2].count_article-36))

print(list(set(error_list)))

plt.gca().invert_yaxis()
plt.grid(color='gray')
plt.legend(bbox_to_anchor=(1.02,1),loc='upper left',borderaxespad=0)
plt.subplots_adjust(right=0.7)
plt.xticks(date_place,date_list)
plt.yticks(range(1,bottom))
plt.show()
