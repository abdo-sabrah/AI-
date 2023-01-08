#!/usr/bin/env python
# coding: utf-8

# # Wine

# ### Introduction:
# 
# This exercise is a adaptation from the UCI Wine dataset.
# The only pupose is to practice deleting data with pandas.
# 
# ### Step 1. Import the necessary libraries

# In[37]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data). 

# ### Step 3. Assign it to a variable called wine

# In[42]:


wine = pd.read_csv('wine.data')

wine.head()


# ### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns

# In[43]:


wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)

wine.head()


# ### Step 5. Assign the columns as below:
# 
# The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 

# In[44]:


wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
wine.head()


# ### Step 6. Set the values of the first 3 rows from alcohol as NaN

# In[45]:


wine.iloc[0:3,0] = np.nan
wine.head()


# ### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN

# In[46]:


wine.iloc[2:4,3]= np.nan
wine.head()


# ### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium

# In[47]:


wine.alcohol.fillna(10,inplace=True)
wine.magnesium.fillna(100,inplace=True)
wine.head()


# ### Step 9. Count the number of missing values

# In[48]:


wine.isnull().sum()


# ### Step 10.  Create an array of 10 random numbers up until 10

# In[49]:


arr = np.random.randint(10, size = 10)

arr


# ### Step 11.  Use random numbers you generated as an index and assign NaN value to each of cell.

# In[50]:


wine.alcohol.loc[arr] = np.nan
wine.head()


# ### Step 12.  How many missing values do we have?

# In[51]:


wine.isnull().sum()


# ### Step 13. Delete the rows that contain missing values

# In[52]:


wine = wine.dropna()
wine.head()


# ### Step 14. Print only the non-null values in alcohol

# In[54]:


y = wine.notna()
y.head(3)


# In[55]:


wine[y]


# ### Step 15.  Reset the index, so it starts with 0 again

# In[57]:


wine.reset_index(drop=True)
wine.head()


# ### BONUS: Create your own question and answer it.

# In[ ]:




