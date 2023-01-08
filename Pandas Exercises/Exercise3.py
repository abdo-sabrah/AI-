#!/usr/bin/env python
# coding: utf-8

# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[58]:


import pandas as pd 
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[2]:


chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
chipo


# ### Step 4. How many products cost more than $10.00?

# In[59]:


chipo['item_price'] = chipo['item_price'].astype(str).str.replace('$', '')
chipo['item_price'] = chipo['item_price'].astype(float)
np.count_nonzero(chipo.item_price>10.00)


# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# In[78]:


chipo_g = chipo.groupby("item_name")[["item_price"]].min().reset_index()
chipo_g


# ### Step 6. Sort by the name of the item

# In[94]:


chipo.sort_values(by="item_name",ascending=True).reset_index(drop=True)


# ### Step 7. What was the quantity of the most expensive item ordered?

# In[100]:


mx_p =  np.where(chipo.item_price == chipo.item_price.max(),chipo.quantity,0)
for i in mx_p:
    if i !=0 :
        print("Quantity of the most expensive item ordered is : ",i)


# ### Step 8. How many times was a Veggie Salad Bowl ordered?

# In[103]:


count = np.count_nonzero(chipo.item_name=="Veggie Salad Bowl")
print(count,"times a Veggie Salad Bowl was ordered")


# ### Step 9. How many times did someone order more than one Canned Soda?

# In[114]:


count2 = np.count_nonzero((chipo.item_name == "Canned Soda") & (chipo.quantity > 1))
count2


# In[ ]:





# In[ ]:




