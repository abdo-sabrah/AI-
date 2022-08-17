#!/usr/bin/env python
# coding: utf-8

# In[12]:


class goods :
    def __init__(self):
        print ("what you want to delete")
        self.kind = input(" what goods kind")
        self.amount = int(input("how many item do you want to delete"))
    def __del__ (self):
        print ("the goods is deleted")
a=goods ()


# In[ ]:




