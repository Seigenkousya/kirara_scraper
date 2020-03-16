#-*-coding:utf-8 -*-
import re
import regex
import sys
import requests
import collections
import bs4
from bs4 import BeautifulSoup
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

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
                Article("RPG","不動産"),
                Article("killme","キルミー"),
                Article("machikado","まちカド"),
                Article("Achannel","チャンネル"),
                Article("anima","アニマエ"),
                Article("NEWGAME","GAME")]
                
print ("\n{}年{}月号".format(year,month))

date_list.append(str(year)+"\n"+month_list[month-1]);
date_place.append(index)

url='http://www.dokidokivisual.com/magazine/carat/book/index.php?mid={0}'.format(mid_list[index])
html=requests.get(url)

source=BeautifulSoup(html.content,"html.parser")

strongs=source.find_all("strong")

center_colors=[]
for i in range(0,5):
    center_colors.append(re.search('「.+」',strongs[i].text).group())
    center_color_all.append(center_colors[-1])

#print(center_colors)

i=0
for art in source.find("ul",class_="lineup").find_all("strong"):
        print(art.string)
        print(type(art))
        i+=1

index+=1
