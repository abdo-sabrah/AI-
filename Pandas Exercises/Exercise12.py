#!/usr/bin/env python
# coding: utf-8

# # Fictitious Names

# ### Introduction:
# 
# This time you will create a data again 
# 
# Special thanks to [Chris Albon](http://chrisalbon.com/) for sharing the dataset and materials.
# All the credits to this exercise belongs to him.  
# 
# In order to understand about it go [here](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/).
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Create the 3 DataFrames based on the following raw data

# In[3]:


raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}


# ### Step 3. Assign each to a variable called data1, data2, data3

# In[4]:


data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])


# ### Step 4. Join the two dataframes along rows and assign all_data

# In[6]:


all_data = pd.concat([data1,data2])
all_data.head()


# ### Step 5. Join the two dataframes along columns and assing to all_data_col

# In[7]:


all_data_col = pd.concat([data1, data2], axis = 1)
all_data_col


# ### Step 6. Print data3

# In[8]:


data3


# ### Step 7. Merge all_data and data3 along the subject_id value

# In[11]:


data4 = pd.merge(all_data, data3, on='subject_id')
data4


# ### Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2

# In[13]:


data5 = pd.merge(data1,data2,on='subject_id',how='inner')
data5


# ### Step 9. Merge all values in data1 and data2, with matching records from both sides where available.

# In[14]:


data6 = pd.merge(data1, data2, on='subject_id', how='outer')
data6


# In[ ]:




