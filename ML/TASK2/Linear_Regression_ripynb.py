#!/usr/bin/env python
# coding: utf-8

# # follow up  template after that write the code
# 
# 
# 
# 
# 

# ## 1. Let's Now Import library of pandas and numpy
# 
# 
# 

# In[38]:


import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# ## 2. Load The Data into a Pandas Frame , hint  use **pd.read_csv**

# In[3]:


df = pd.read_csv("kc_house_data.csv")
df


# ## 3. define x is the features of dataframe and y is label , hint use **df.iloc**

# In[39]:


a = df.iloc[:,:]
y = df.iloc[:,2]


# ### 4.Drop (id,date) column from x(independent variables ),  hint use **drop()** function

# In[44]:


a = df.drop("date",axis ="columns")
x = a.drop("id",axis = "columns")


# ## 5. Splitting the dataset into the Training set and Test set and put **random_state=2**
# 

# In[45]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 2)


# ## 6. Fitting Linear Regression to the dataset and count regression.score

# In[48]:


reg = LinearRegression()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
score = r2_score(y_test,y_pred)
score


# In[ ]:




