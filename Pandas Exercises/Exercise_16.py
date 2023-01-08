#!/usr/bin/env python
# coding: utf-8

# # Visualizing Chipotle's Data
# 
# Check out [Chipotle's Visualization Exercises Video Tutorial](https://youtu.be/BLD2mAB3kaw) to watch a data scientist go through the exercises

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# set this so the 
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[3]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')


# ### Step 4. See the first 10 entries

# In[4]:


chipo.head(10)


# ### Step 5. Create a histogram of the top 5 items bought

# In[15]:


x= chipo.item_name
letter_count = Counter(x) 
df = pd.DataFrame.from_dict(letter_count, orient='index')
df = df[0].sort_values(ascending = True)[45:50]
df.plot(kind='bar')
plt.xlabel('Items')
plt.ylabel('Number of Times Ordered')
plt.title('Most ordered Chipotle\'s Items')
plt.show()


# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis

# In[ ]:


chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space

orders = chipo.groupby('order_id').sum()


plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')

plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)


# ### BONUS: Create a question and a graph to answer your own question.

# In[ ]:




