#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[15]:


#1 sorted dict by key 
salaries = {"Ahmed": 5000 , "Mohamed":8000 , "Badr": 6000 , "Salah":7000 }
b = sorted (salaries)
print (b)
c = sorted (salaries.items())
print(c)


# In[12]:


#2 my own lib
import anglevalue 
print (anglevalue.octagon(50,20,10,20,10,50,60))
print (anglevalue.prntgram(10,20,30,40))
print(anglevalue.triangle(100,60))


# In[ ]:


#3 stack fill by user
from queue import LifoQueue as stack
st = stack()

def put_into_stack():
    for i in range (0,11):
        x = input()
        st.put(x)
put_into_stack()
while st !=0 : 
    print(st.get())


# In[ ]:


#4 multiset
from multiset import Multiset
mset=Multiset([1,5,6,7,9,4,4,1,5])
mset


# In[ ]:


#5 ordered set
from orderedset import Orderedset
Oset= Orderedset([10,50,40,70,9,70,6])


# In[ ]:





# In[3]:





# In[ ]:





# In[ ]:





# In[7]:





# In[ ]:




