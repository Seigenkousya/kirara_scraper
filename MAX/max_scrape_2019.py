#-*-coding:utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

mid_list=['139', '143', '147', '151', '155', '159', '163', '167', '171', '175', '179', '183', '187', '191', '195', '199', '203', '207', '211', '215', '219', '223', '227', '231', '235', '239', '244', '249', '254', '259', '264', '269', '274', '279', '284', '289', '294', '299', '304', '309', '314', '319', '324', '329', '334', '340', '345', '350', '355', '360', '362', '370', '375', '380', '385', '390', '395', '400', '405', '410', '415', '420', '425', '430', '435', '440', '445', '450', '455', '460', '465', '470', '475', '480', '485', '490', '495', '500', '505', '510', '514', '520', '525', '530', '535', '540', '545', '550', '555', '560', '565', '570', '575', '580', '585', '590', '594', '598', '602', '606', '610', '614', '618', '622', '626', '630', '634', '638', '642', '646', '650', '654']
bottom=24
mid=187
year=2010
month=1
index=0
doubiju_list=[]
kanojo_list=[]
gochiusa_list=[]
kinmoza_list=[]
comic_list=[]
stella_list=[]
date_list=[]
date_place=[]

while index < len(mid_list):

    print ("\n{}年{}月号".format(year,month))
    
    if month==1:
        date_list.append(str(year)+"\n"+"Jan.")
        date_place.append(index+1)
    if month==7:
        date_list.append(str(year)+"\n"+"Jul.")
        date_place.append(index+1)

    url='http://www.dokidokivisual.com/magazine/max/book/index.php?mid={0}'.format(mid_list[index])
    html=requests.get(url)

    source=BeautifulSoup(html.content,"html.parser")

    span=source.find_all("font")

    i=0
    for tag in span:
        try:
            i+=1
            name=tag.string
            
            print(i,name)

            if "どうして" in name and len(doubiju_list)==index:
                doubiju_list.append(i)
            if "彼女が" in name and len(kanojo_list)==index:
                kanojo_list.append(i)
            if "きんいろ" in name and len(kinmoza_list)==index:
                kinmoza_list.append(i)
            if "ご注文は" in name and len(gochiusa_list)==index:
                gochiusa_list.append(i)
            if "こみっくがーるず" in name and len(comic_list)==index:
                comic_list.append(i)
            if "ステラのまほう" in name and len(stella_list)==index:
                stella_list.append(i)
        except:
            pass 

    if len(kanojo_list)==index:
        kanojo_list.append(None)
    if len(doubiju_list)==index:
        doubiju_list.append(None)
    if len(kinmoza_list)==index:
        kinmoza_list.append(None)
    if len(gochiusa_list)==index:
        gochiusa_list.append(None)
    if len(comic_list)==index:
        comic_list.append(None)
    if len(stella_list)==index:
        stella_list.append(None)


    index+=1

    if month==12:
        year+=1
        month=1
    else:
        month+=1


    sleep(1)

#print(doubiju_list)
#print(kanojo_list)
#print(kinmoza_list)
#print(gochiusa_list)
#print(comic_list)
#print(stella_list)

print(len(doubiju_list))
print(len(kanojo_list))
print(len(kinmoza_list))
print(len(gochiusa_list))
print(len(comic_list))
print(len(stella_list))

##kanojo_list=[24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 17, 10, 5, 5, 21, 5, 5, 6, 5, 5, 5, 17, 4, 4, 14, 8, 14, 14, 21, 23, 22]
#kanojo_list=[17, 10, 5, 5, 21, 5, 5, 6, 5, 5, 5, 17, 4, 4, 14, 8, 14, 14, 21, 23, 22]
#gochiusa_list=[9, 9, 9, 13, 9, 9, 13, 9, 13, 9, 13, 9, 9, 1, 9, 1, 9, 9, 9, 1, 9, 1, 1, 1, 9, 1, 9, 9, 9, 9, 9, 1, 9, 1, 9, 1, 9, 9]
#kinmoza_list=[2, 2, 13, 2, 3, 2, 9, 2, 9, 3, 9, 2, 1, 3, 2, 2, 1, 2, 1, 3, 2, 13, 3, 2, 2, 2, 3, 2, 3, 2, 1, 2, 1, 2, 2, 2, 2, 2]

X_list=list(range(len(mid_list)))
plt.xlabel('Publication issue')
plt.ylabel('Publication order')
plt.title('Changes in the order of publication')
plt.plot(X_list, doubiju_list, label='doubiju')
plt.plot(X_list, kanojo_list, label='kanojoga')
plt.plot(X_list, kinmoza_list, label='kinmoza')
plt.plot(X_list, gochiusa_list, label='gochiusa')
plt.plot(X_list, comic_list, label='comic')
plt.plot(X_list, stella_list, label='stella')
plt.gca().invert_yaxis()
plt.grid(color='gray')
plt.legend(bbox_to_anchor=(1.02,1),loc='upper left',borderaxespad=0)
plt.subplots_adjust(right=0.7)
plt.xticks(date_place,date_list)
plt.yticks(range(1,bottom))
plt.show()
