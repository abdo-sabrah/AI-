#!/usr/bin/env python
# coding: utf-8

# In[29]:


f=open (r"D:\AI1\info.txt","r")
text_file = f.readlines()
text = ' '.join(text_file)
type(text)


# In[89]:


import re 
pattern = re.compile (r" \d{10}")
matches = pattern.finditer(text)
phonenum_list = []

for match in matches :
    phonenum_list.append(text [match.span() [0] : match.span() [1]])
print (phonenum_list)


# In[87]:


import re 
pattern = re.compile (r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.\w{3}")
matches = pattern.finditer(text)
Emails_list = []
for match in matches :
    Emails_list.append(text[match.span()[0] : match.span() [1]])
print (Emails_list)
    


# In[102]:


import re 
pattern = re.compile(r"[A-Z][a-z]+")
matches=pattern.finditer(text)
name_list=[]
for match in matches :
    name_list.append(text[match.span()[0] : match.span()[1]])
print(name_list)
    


# In[88]:





# In[ ]:




