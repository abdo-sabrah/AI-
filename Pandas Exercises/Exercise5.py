#!/usr/bin/env python
# coding: utf-8

# # Fictional Army - Filtering and Sorting

# ### Introduction:
# 
# This exercise was inspired by this [page](http://chrisalbon.com/python/)
# 
# Special thanks to: https://github.com/chrisalbon for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np


# ### Step 2. This is the data given as a dictionary

# In[21]:


# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}


# ### Step 3. Create a dataframe and assign it to a variable called army. 
# 
# #### Don't forget to include the columns names in the order presented in the dictionary ('regiment', 'company', 'deaths'...) so that the column index order is consistent with the solutions. If omitted, pandas will order the columns alphabetically.

# In[22]:


army = pd.DataFrame(raw_data)
army


# ### Step 4. Set the 'origin' colum as the index of the dataframe

# In[23]:


army.set_index('origin', inplace=True)


# ### Step 5. Print only the column veterans

# In[20]:


army


# ### Step 6. Print the columns 'veterans' and 'deaths'

# In[25]:


army[['veterans','deaths']]


# ### Step 7. Print the name of all the columns.

# In[26]:


army.columns


# ### Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska

# In[27]:


army.loc[['Maine' ,'Alaska'],['deaths', 'size']]


# ### Step 9. Select the rows 3 to 7 and the columns 3 to 6

# In[29]:


army.iloc[2:7,2:6]


# ### Step 10. Select every row after the fourth row and all columns

# In[30]:


army.iloc[4:,:]


# ### Step 11. Select every row up to the 4th row and all columns

# In[31]:


army.iloc[:4,:]


# ### Step 12. Select the 3rd column up to the 7th column

# In[34]:


army.iloc[:,3:7]


# ### Step 13. Select rows where df.deaths is greater than 50

# In[35]:


army[army.deaths>50]


# ### Step 14. Select rows where df.deaths is greater than 500 or less than 50

# In[38]:


army[(army.deaths>500)|(army.deaths<50)]


# ### Step 15. Select all the regiments not named "Dragoons"

# In[39]:


army[army.regiment != "Dragoons"]


# ### Step 16. Select the rows called Texas and Arizona

# In[40]:


army.loc[['Texas', 'Arizona']]


# ### Step 17. Select the third cell in the row named Arizona

# In[45]:


army.loc[['Arizona'],['deaths']]


# ### Step 18. Select the third cell down in the column named deaths

# In[46]:


army.loc[['Texas'],['deaths']] 


# In[ ]:




