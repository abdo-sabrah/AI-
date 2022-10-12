#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to display all the dates for the month of March, 2017.
# 
# 

# In[5]:


import numpy as np 
print("april 2022")
print(np.arange('2022-04', '2022-05', dtype='datetime64[D]'))


# #### 2-Write a NumPy program to get the dates of yesterday, today and tomorrow.
# 
# 

# In[11]:


yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today = np.datetime64('today','D')
today = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)


# #### 3-Write a NumPy program to count the number of days of specific month.
# 
# 

# In[17]:


print("Number of days, February, 2022: ")
print(np.datetime64('2022-03-01') - np.datetime64('2022-02-01'))
print("Number of days, February, 2021: ")
print(np.datetime64('2021-03-01') - np.datetime64('2021-02-01'))
print("Number of days, February, 2020: ")
print(np.datetime64('2020-03-01') - np.datetime64('2020-02-01'))



# #### 4-Write a NumPy program to create 24 python datetime. datetime objects (single object for every hour), and then put it in a numpy array.

# In[29]:


import datetime
start = datetime.datetime(2000,1,1)
dt_arr = np.array([start + datetime.timedelta (hours = i) for i in range (24)])
print(dt_arr)


# #### 5-Write a NumPy program to find the first Monday in May 2017.
# 
# 

# In[31]:


print("First Monday in march 2022:")
print(np.busday_offset('2022-03', 0, roll='forward', weekmask='Mon'))


# #### 6-Write a NumPy program to find the number of weekdays in March 2017.
# 
# 

# In[32]:


print("Number of weekdays in december 2022:")
print(np.busday_count('2017-11', '2017-12'))


# 
# 

# In[ ]:




