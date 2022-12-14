#!/usr/bin/env python
# coding: utf-8

# # Student Alcohol Consumption

# ### Introduction:
# 
# This time you will download a dataset from the UCI.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd 
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).

# ### Step 3. Assign it to a variable called df.

# In[3]:


url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv"
df = pd.read_csv(url)
df.head()


# ### Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column

# In[16]:


df1 = df.loc[:,'school': 'guardian' ]


# ### Step 5. Create a lambda function that will capitalize strings.

# In[20]:


capitalizer = lambda x: x.capitalize()


# ### Step 6. Capitalize both Mjob and Fjob

# In[23]:


df1['Mjob'].apply(capitalizer)
df1['Fjob'].apply(capitalizer)


# ### Step 7. Print the last elements of the data set.

# In[24]:


df1.tail()


# ### Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.

# In[32]:


df1['Mjob'] = df1['Mjob'].apply(capitalizer)
df1['Fjob'] = df1['Fjob'].apply(capitalizer)
df1.tail()


# ### Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)

# In[33]:


def majority (x):
    if x>17:
        return True 
    else:
        return False


# In[38]:


df1['legal_drinker'] = df['age'].apply(majority)  
df1.head()


# ### Step 10. Multiply every number of the dataset by 10. 
# ##### I know this makes no sense, don't forget it is just an exercise

# In[44]:


def mul10(x) :
    if type(x) is int:
        return 10 * x
    return x


# In[46]:


df1.applymap(mul10)


# In[ ]:




