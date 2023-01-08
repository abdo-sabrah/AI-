#!/usr/bin/env python
# coding: utf-8

# # US - Baby Names

# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv). 

# ### Step 3. Assign it to a variable called baby_names.

# In[13]:


baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()


# ### Step 4. See the first 10 entries

# In[3]:


baby_names.head(10)


# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

# In[14]:


baby_names = baby_names.drop(['Unnamed: 0', 'Id'], axis = 1)


baby_names.head()


# ### Step 6. Is there more male or female names in the dataset?

# In[15]:


baby_names['Gender'].value_counts()


# ### Step 7. Group the dataset by name and assign to names

# In[16]:


names = baby_names.groupby('Name')
names = baby_names.drop('Year', axis = 1).groupby('Name').sum()
names


# ### Step 8. How many different names exist in the dataset?

# In[19]:


baby_names.Name.nunique()


# ### Step 9. What is the name with most occurrences?

# In[21]:


baby_names.groupby('Name').Count.sum().sort_values(ascending = False).head(1)


# ### Step 10. How many different names have the least occurrences?

# In[24]:


names[names.Count == names.Count.min()].shape[0]


# ### Step 11. What is the median name occurrence?

# In[30]:


(names.Count == names.Count.median()).sum()


# ### Step 12. What is the standard deviation of names?

# In[27]:


names.Count.std()


# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

# In[26]:


baby_names.describe()


# In[ ]:




