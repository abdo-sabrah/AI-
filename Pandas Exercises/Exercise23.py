#!/usr/bin/env python
# coding: utf-8

# # Investor - Flow of Funds - US

# ### Introduction:
# 
# Special thanks to: https://github.com/rgrp for sharing the dataset.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv). 

# ### Step 3. Assign it to a variable called 

# In[22]:


url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)


# ### Step 4.  What is the frequency of the dataset?

# In[23]:


df.head()


# ### Step 5. Set the column Date as the index.

# In[24]:


df.set_index('Date',inplace=True )
df.head()


# ### Step 6. What is the type of the index?

# In[25]:


df.index.dtype


# ### Step 7. Set the index to a DatetimeIndex type

# In[41]:


df.index = pd.to_datetime(df.index)
df.index.dtype


# ### Step 8.  Change the frequency to monthly, sum the values and assign it to monthly.

# In[42]:


monthly = df.resample('M').sum(min_count=1)
monthly.head()


# ### Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.

# In[47]:


monthly.dropna(axis='index',how = 'all',inplace=True)
monthly.head()


# ### Step 10. Good, now we have the monthly data. Now change the frequency to year.

# In[48]:


monthly.resample('A').sum()


# ### BONUS: Create your own question and answer it.

# In[ ]:




