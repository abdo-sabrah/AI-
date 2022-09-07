#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Download youtube video
from pytube import YouTube
Save_at = "D:/"
video_link = "https://youtu.be/oyzJIGuZzNw"
try :
    y = YouTube(video_link)
except :
    print ("EROR")
y.streams.filter(file_extension="mp4").get_by_resolution("360p").download(Save_at)


# In[ ]:


#scrape images from website
import requests
from bs4 import BeautifulSoup
url="https://unsplash.com/collections/1301956/discussion-photos"
request=requests.get(url)
soup = BeautifulSoup(request.text,'html.parser')
images= soup.find_all('img',class_="YVj9w")
for image in images :
    name = image ['alt'] 
    link = image['src']
    with open (name.replace(' ','-') +'.jpg','wb') as f :
        my_img= requests.get(link)
        f.write(my_img.content)       


# In[100]:


#scrap 5 articles from website
import requests
from bs4 import BeautifulSoup
import csv 
website=requests.get("https://coreyms.com").text
soup = BeautifulSoup(website,'lxml')
csvfile=open("scrape-task.csv",'w')
writer = csv.writer(csvfile)
writer.writerow(['headline','summary','link'])
articles = soup.find_all('articles')
for article in articles :
    headline = article.h2.a.text
    summary= article.find('div',class_='entry-content').p.text
    link='none'
    try:
        vid = article.find('iframe',class_= "youtube-player")['src']
        vid_id = vid.split('/')
        video = video_id[4].split('?')
        c=video[0]
        link = (f"https://www.youtube.com/watch?v={c}")
    except :
        link="no link"
    writer.writerow[headline,summary,link]
csvfile.close()

    


# In[ ]:





# In[92]:





# In[ ]:




