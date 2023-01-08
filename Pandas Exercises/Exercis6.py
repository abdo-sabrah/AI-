#!/usr/bin/env python
# coding: utf-8

# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarized as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 

# ### Step 3. Assign it to a variable called drinks.

# In[5]:


drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks


# ### Step 4. Which continent drinks more beer on average?

# In[10]:


drinks.groupby('continent').beer_servings.mean().sort_values(ascending = False).head(1)


# ### Step 5. For each continent print the statistics for wine consumption.

# In[11]:


drinks.groupby('continent').wine_servings.describe()


# ### Step 6. Print the mean alcohol consumption per continent for every column

# In[13]:


drinks.groupby('continent').mean()


# ### Step 7. Print the median alcohol consumption per continent for every column

# In[14]:


drinks.groupby('continent').median()


# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# In[15]:


drinks.groupby('continent').agg(['mean','min','max'])


# In[ ]:




