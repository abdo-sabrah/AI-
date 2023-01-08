#!/usr/bin/env python
# coding: utf-8

# # Scores

# ### Introduction:
# 
# This time you will create the data.
# 
# ***Exercise based on [Chris Albon](http://chrisalbon.com/) work, the credits belong to him.***
# 
# ### Step 1. Import the necessary libraries

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ### Step 2. Create the DataFrame that should look like the one below.

# In[5]:


data = {'first_name' :['Jason','Molly','Tina','Jake','Amy'],
     'last_name':['Miller','Jacobson','Ali','Milner','Cooze'],
     'age':[42,52,36,24,73],
     'female': [0, 1, 1, 0, 1],
     'preTestScore': [4, 24, 31, 2, 3],
     'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data)
df


# ### Step 3. Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
# #### Hint: Don't forget to place the labels

# In[17]:


plt.scatter(df.preTestScore,df.postTestScore,s=df.age)
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')


# ### Step 4. Create a Scatterplot of preTestScore and postTestScore.
# ### This time the size should be 4.5 times the postTestScore and the color determined by sex

# In[20]:


plt.scatter(df.preTestScore,df.postTestScore,s=df.postTestScore*4.5,c=df.female)
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')


# ### BONUS: Create your own question and answer it.

# In[ ]:




