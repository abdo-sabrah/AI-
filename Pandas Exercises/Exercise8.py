#!/usr/bin/env python
# coding: utf-8

# # Regiment

# ### Introduction:
# 
# Special thanks to: http://chrisalbon.com/ for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np


# ### Step 2. Create the DataFrame with the following values:

# In[30]:


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}


# ### Step 3. Assign it to a variable called regiment.
# #### Don't forget to name each column

# In[31]:


regiment = pd.DataFrame(raw_data)
regiment


# ### Step 4. What is the mean preTestScore from the regiment Nighthawks?  

# In[9]:


regiment[regiment['regiment'] == 'Nighthawks'].groupby('regiment').mean()


# ### Step 5. Present general statistics by company

# In[12]:


regiment.groupby('company').describe()


# ### Step 6. What is the mean of each company's preTestScore?

# In[13]:


regiment.groupby('company').preTestScore.mean()


# ### Step 7. Present the mean preTestScores grouped by regiment and company

# In[14]:


regiment.groupby(['regiment','company']).preTestScore.mean()


# ### Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing

# In[15]:


regiment.groupby(['regiment','company']).preTestScore.mean().unstack()


# ### Step 9. Group the entire dataframe by regiment and company

# In[32]:


regiment.groupby(['regiment','company']).mean()


# ### Step 10. What is the number of observations in each regiment and company

# In[36]:


regiment.groupby(['regiment','company']).size()


# ### Step 11. Iterate over a group and print the name and the whole data from the regiment

# In[38]:


for name,group in regiment.groupby('regiment'):
    print(name)
    print(group)


# In[ ]:




