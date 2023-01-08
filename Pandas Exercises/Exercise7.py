#!/usr/bin/env python
# coding: utf-8

# # Occupation

# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd 
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users.

# In[4]:


users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep = '|')
users


# ### Step 4. Discover what is the mean age per occupation

# In[5]:


users.groupby('occupation').age.mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[16]:


users['is_male'] = users.gender.apply(lambda x: True if x=='M' else False )
(users.groupby('occupation').is_male.sum()/users.groupby('occupation').gender.count()).sort_values(ascending = False)


# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[17]:


users.groupby('occupation').agg(['min','max'])


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[18]:


users.groupby('occupation').agg(['mean'])


# ### Step 8.  For each occupation present the percentage of women and men

# In[30]:


occup_gender= users.groupby(['occupation','gender']).agg({'gender':'count'})
occup_count = users.groupby(['occupation']).count()
occup_gender = gender_ocup.div(occup_count, level = "occupation")
occup_gender.loc[:, 'gender']


# In[ ]:




