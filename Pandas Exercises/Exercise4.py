#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). 

# ### Step 3. Assign it to a variable called euro12.

# In[6]:


euro12 = pd.read_csv("Euro_2012_stats_TEAM.csv")
euro12


# ### Step 4. Select only the Goal column.

# In[14]:


euro12.Goals


# ### Step 5. How many team participated in the Euro2012?

# In[18]:


count = np.count_nonzero(euro12.Team) #or euro12.team.unique()
count


# ### Step 6. What is the number of columns in the dataset?

# In[19]:


len(euro12.columns) #euro12.shape[1]


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[22]:


discipline = euro12[['Team','Yellow Cards','Red Cards']]
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[27]:


discipline.sort_values(by=['Red Cards','Yellow Cards'],inplace=True)
discipline


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[29]:


discipline['Yellow Cards'].mean()


# ### Step 10. Filter teams that scored more than 6 goals

# In[31]:


euro12[euro12['Goals']>6]


# ### Step 11. Select the teams that start with G

# In[35]:


euro12[euro12.Team.str.startswith('G')]


# ### Step 12. Select the first 7 columns

# In[37]:


euro12.head(7)


# ### Step 13. Select all columns except the last 3.

# In[38]:


euro12.iloc[:,0:-3]


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[ ]:


euro12.loc[euro.Team.isin(['England', 'Italy', 'Russia']),['Team','']

