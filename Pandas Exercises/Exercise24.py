#!/usr/bin/env python
# coding: utf-8

# # Iris

# ### Introduction:
# 
# This exercise may seem a little bit strange, but keep doing it.
# 
# ### Step 1. Import the necessary libraries

# In[17]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). 

# ### Step 3. Assign it to a variable called iris

# In[28]:


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url)
iris.head()


# ### Step 4. Create columns for the dataset

# In[33]:


# 1. sepal_length (in cm)
# 2. sepal_length (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class
iris.columns = ['sepal_length','sepal_length','petal_length','petal_width','class']
iris.head()


# ### Step 5.  Is there any missing value in the dataframe?

# In[34]:


iris.info()


# ### Step 6.  Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN

# In[38]:


iris.loc[10:29,'petal_length']=np.nan
iris.loc[10:29]


# ### Step 7. Good, now lets substitute the NaN values to 1.0

# In[39]:


iris.fillna(1.0,inplace=True)
iris.info()


# ### Step 8. Now let's delete the column class

# In[40]:


del iris['class']
iris.head()


# ### Step 9.  Set the first 3 rows as NaN

# In[42]:


iris.loc[:3]=np.nan
iris.loc[:3]


# ### Step 10.  Delete the rows that have NaN

# In[45]:


iris.dropna(inplace=True)
iris.head(5)


# ### Step 11. Reset the index so it begins with 0 again

# In[47]:


iris = iris.reset_index(drop = True)
iris.head(5)


# ### BONUS: Create your own question and answer it.

# In[ ]:




