#!/usr/bin/env python
# coding: utf-8

# # Apple Stock

# ### Introduction:
# 
# We are going to use Apple's stock price.
# 
# 
# ### Step 1. Import the necessary libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)

# In[4]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'


# ### Step 3. Assign it to a variable apple

# In[26]:


apple = pd.read_csv(url)
apple.head()


# ### Step 4.  Check out the type of the columns

# In[27]:


apple.dtypes


# ### Step 5. Transform the Date column as a datetime type

# In[38]:


apple ['Date'] = apple['Date'].apply(pd.Timestamp)
apple.dtypes


# ### Step 6.  Set the date as the index

# In[40]:


apple.set_index('Date')
apple.head()


# ### Step 7.  Is there any duplicate dates?

# In[41]:


apple.Date.duplicated # or apple.index.is_unique


# ### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.

# In[62]:


apple = apple.sort_values(by="Date",ascending=True).reset_index(drop=True)
apple.head()


# ### Step 9. Get the last business day of each month

# In[54]:


apple['month']= pd.DatetimeIndex(apple.Date).month
apple['end date'] = pd.DatetimeIndex(apple.Date).day
apple.groupby(by='month')[['end date']].max().reset_index()


# ### Step 10.  What is the difference in days between the first day and the oldest

# In[58]:


differnce = apple.Date.max() - apple.Date.min() 
str (differnce)


# ### Step 11.  How many months in the data we have?

# In[60]:


months = apple.month.count()
months


# ### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches

# In[71]:


plt.hist(apple['Adj Close'])
plt.figure(figsize= (13.5 , 9) )
plt.show
import seaborn as sns
x = sns.displot(apple['Adj Close'])


# ### BONUS: Create your own question and answer it.

# In[ ]:




