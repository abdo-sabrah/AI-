#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[13]:


import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[17]:


chipo = pd.read_csv(url, sep="\t")
chipo


# ### Step 4. See the first 10 entries

# In[19]:


chipo.head(10)


# ### Step 5. What is the number of observations in the dataset?

# In[20]:


# Solution 1
chipo.shape


# In[21]:


# Solution 2

chipo.info


# ### Step 6. What is the number of columns in the dataset?

# In[22]:


len(chipo.columns)


# ### Step 7. Print the name of all the columns.

# In[24]:


chipo.columns


# ### Step 8. How is the dataset indexed?

# In[25]:


chipo.index


# ### Step 9. Which was the most-ordered item? 

# In[39]:


chipo.groupby('item_name')['quantity'].agg(['count']).sort_values(by='count', ascending=False).head(1)


# ### Step 10. For the most-ordered item, how many items were ordered?

# In[41]:


chipo.groupby('item_name')['quantity'].agg(['count']).sort_values(by='count',ascending =False ).head(1)


# ### Step 11. What was the most ordered item in the choice_description column?

# In[43]:


chipo.groupby('choice_description')['quantity'].agg(['count']).sort_values(by='count',ascending=False).head(1)


# ### Step 12. How many items were orderd in total?

# In[44]:


chipo['quantity'].sum()


# ### Step 13. Turn the item price into a float

# #### Step 13.a. Check the item price type

# In[51]:


chipo['item_price'].dtype


# #### Step 13.b. Create a lambda function and change the type of item price

# In[53]:


price_t = lambda x:float (x[1:-1])
chipo['item_price'] = chipo.item_price.apply(price_t)


# #### Step 13.c. Check the item price type

# In[54]:


chipo['item_price'].dtype


# ### Step 14. How much was the revenue for the period in the dataset?

# In[58]:


revenue = (chipo['quantity']*chipo['item_price']).sum()
revenue


# ### Step 15. How many orders were made in the period?

# In[74]:


chipo['order_id'].value_counts().count()


# ### Step 16. What is the average revenue amount per order?

# In[79]:


# Solution 1
chipo['revenue'] = chipo['quantity']*chipo['item_price']
o_gro = chipo.groupby(['order_id']).sum() 
o_gro.mean()['revenue']
chipo.head(10)


# In[83]:


# Solution 2
chipo.groupby(['order_id']).sum().mean()['revenue']
chipo.head(10)


# ### Step 17. How many different items are sold?

# In[86]:


chipo['item_name'].value_counts().count()


# In[ ]:




