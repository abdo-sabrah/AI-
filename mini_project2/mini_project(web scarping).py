#!/usr/bin/env python
# coding: utf-8

# In[41]:



import requests 
from bs4 import BeautifulSoup 
import csv
from itertools import zip_longest
name=[]
rate=[]
year=[]
rank=[]
file_list=[rank,name,year,rate]
website = requests.get("https://www.imdb.com/chart/top/").text
soup =BeautifulSoup (website,'lxml')
names = soup.find_all('td',class_="titleColumn")
years = soup.find_all('span',class_='secondaryInfo')
rates = soup.find_all('td',class_="ratingColumn imdbRating")
for i in range (len(names)) :
    name.append(names[i].a.text)
    year.append(years[i].text)
    rate.append(rates[i].strong.attrs['title'])
    ranks = names[i].text.split()
    rank.append(ranks[0])

exported = zip_longest(*file_list)
csvfile=open("web-scrape.csv",'w')
writer = csv.writer(csvfile)
writer.writerow(['rank','name','year','rate'])
writer.writerows(exported)    


# In[ ]:




