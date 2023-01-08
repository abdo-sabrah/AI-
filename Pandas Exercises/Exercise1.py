#!/usr/bin/env python
# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd 
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[3]:


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"


# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[4]:


users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep='|' )


# ### Step 4. See the first 25 entries

# In[5]:


users.head(25)


# ### Step 5. See the last 10 entries

# In[6]:


users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[11]:


users.describe


# ### Step 7. What is the number of columns in the dataset?

# In[13]:


users.shape[1]


# ### Step 8. Print the name of all the columns.

# In[14]:


users.columns


# ### Step 9. How is the dataset indexed?

# In[15]:


users.index


# ### Step 10. What is the data type of each column?

# In[16]:


users.dtypes


# ### Step 11. Print only the occupation column

# In[17]:


users['occupation']


# ### Step 12. How many different occupations are in this dataset?

# In[19]:


users.occupation.value_counts().count()


# ### Step 13. What is the most frequent occupation?

# In[20]:


users.occupation.value_counts().head(1).index[0]


# ### Step 14. Summarize the DataFrame.

# In[21]:


users.describe


# ### Step 15. Summarize all the columns

# In[22]:


users.describe(include='all')


# ### Step 16. Summarize only the occupation column

# In[24]:


users.occupation.describe()


# ### Step 17. What is the mean age of users?

# In[25]:


users.age.mean()


# ### Step 18. What is the age with least occurrence?

# In[27]:


users.age.value_counts().tail()


# In[ ]:




