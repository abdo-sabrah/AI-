#!/usr/bin/env python
# coding: utf-8

# # Housing Market

# ### Introduction:
# 
# This time we will create our own dataset with fictional numbers to describe a house market. As we are going to create random data don't try to reason of the numbers.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np


# ### Step 2. Create 3 differents Series, each of length 100, as follows: 
# 1. The first a random number from 1 to 4 
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000

# In[4]:


S1 = pd.Series(np.random.randint(1,high=5,size=100,dtype='l'))
S2 =pd.Series(np.random.randint(1,high=4,size=100,dtype='l'))
S3 =pd.Series(np.random.randint(10000,high=30000,size=100,dtype='l'))


# ### Step 3. Let's create a DataFrame by joinning the Series by column

# In[6]:


df = pd.concat([S1,S2,S3],axis=1)
df


# ### Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

# In[10]:


df.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
df


# ### Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

# In[12]:


Big = pd.concat([S1, S2, S3], axis=0)
Big = Big.to_frame()
Big


# ### Step 6. Oops, it seems it is going only until index 99. Is it true?

# In[13]:


len(Big)


# ### Step 7. Reindex the DataFrame so it goes from 0 to 299

# In[15]:


Big.reset_index(drop=True, inplace=True)
Big


# In[ ]:




