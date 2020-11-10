#-*-coding:utf-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup
from time import sleep

year=2019
mid_list=[]

while year<=2020:

    print ("\n{}年".format(year))

    url='http://www.dokidokivisual.com/magazine/kirara/backnumber/index.php?y={0}'.format(year)
    html=requests.get(url)

    source=BeautifulSoup(html.content,"html.parser")

    #print(source.prettify())

    a=source.find_all("a")

    #print(source.find("font"))

    i=0
    for tag in a:
        try:
            if "mid" in tag['href']:
                print(tag['href'])
                print(re.search("\d*$",tag['href']).group(0))
                mid_list.append(re.search("\d*$",tag['href']).group(0))
        except:
            pass 

    year+=1
    mid_list=list(set(mid_list))

    sleep(1)

mid_list.sort()
print(mid_list)
