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

#input get_mid.py result here.
mid_list=['644', '648', '652', '656', '660', '664', '668', '672', '676', '680', '684', '688', '692', '696', '700', '704']

month_list=['Jan.','Feb.','Mar.','Apr.','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.'];
bottom=24
mid=187
year=2019
month=1
index=0

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
        self.mark_point=[]

    def is_centercolor(self,center_colors):
        flag=False
        for cc in center_colors:
            if self.keyword in cc:
                flag=True
                break
                
        if flag:
            self.mark_point.append(len(self.center_list))
        
        self.center_list.append(flag)


Article_list=[  Article("koias","恋する"),
                Article("ochifuru","おちこぼれ"),
                Article("hidameri","ひだまり"),
                Article("RPG","不動産"),
                Article("killme","キルミー"),
                Article("machikado","まちカド"),
                Article("Achannel","チャンネル"),
                Article("anima","アニマエ"),
                Article("NEWGAME","GAME")]

while index < len(mid_list):

    print ("\n{}年{}月号".format(year,month))
    
    date_list.append(str(year)+"\n"+month_list[month-1]);
    date_place.append(index)

    url='http://www.dokidokivisual.com/magazine/carat/book/index.php?mid={0}'.format(mid_list[index])
    html=requests.get(url)

    source=BeautifulSoup(html.content,"html.parser")

    strongs=source.find_all("strong")

    center_colors=[]
    info=(source.find_all("div",class_="info"))[1]
    strongs=info.find_all("strong")

    if re.search('表紙(&|＆)巻頭カラー',info.text):
        print("both")
        start=0
        end=5
    else:
        print("other")
        start=1
        end=6


    for art in strongs[start:end]:
        center_colors.append(re.search('「.+」',art.string).group())
        center_color_all.append(center_colors[-1])

    print(center_colors)

    i=0
    articles=source.find("ul",class_="lineup").find_all("strong")
    for art in articles:
        try:
            i+=1
            name=art.string
            
            print(i,name)

            for art in Article_list:
                if art.keyword in name and len(art.list)==index:
                    art.list.append(i)
                    art.is_centercolor(center_colors)
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
    print(art.list)
    print(art.center_list)
    print(art.mark_point)

X_list=list(range(len(mid_list)))
plt.xlabel('Publication issue')
plt.ylabel('Publication order')
plt.title('Changes in the order of publication')

for art in Article_list:
    #plt.plot(X_list, art.list, linestyle='solid', marker="D", markevery=art.mark_point ,label=art.label)
    plt.plot(X_list, art.list, linestyle='solid', marker=".", label=art.label)

plt.gca().invert_yaxis()
plt.grid(color='gray')
plt.legend(bbox_to_anchor=(1.02,1),loc='upper left',borderaxespad=0)
plt.subplots_adjust(right=0.7)
plt.xticks(date_place,date_list)
plt.yticks(range(1,bottom))
plt.show()
