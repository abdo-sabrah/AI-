#!/usr/bin/env python
# coding: utf-8

# # Tips

# ### Introduction:
# 
# This exercise was created based on the tutorial and documentation from [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/index.html)  
# The dataset being used is tips from Seaborn.
# 
# ### Step 1. Import the necessary libraries:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv). 

# ### Step 3. Assign it to a variable called tips

# In[6]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv'
tips = pd.read_csv(url)


# ### Step 4. Delete the Unnamed 0 column

# In[11]:


del tips['Unnamed: 0']
tips.head()


# ### Step 5. Plot the total_bill column histogram

# In[22]:


t_bill = sns.distplot(tips.total_bill)
t_bill.set(xlabel = 'value',ylabel = 'Frequency',title = 'Total Bill')
sns.despine()


# ### Step 6. Create a scatter plot presenting the relationship between total_bill and tip

# In[24]:


sns.jointplot(x = 'total_bill',y = 'tip',data = tips)


# ### Step 7.  Create one image with the relationship of total_bill, tip and size.
# #### Hint: It is just one function.

# In[25]:


sns.pairplot(tips)


# ### Step 8. Present the relationship between days and total_bill value

# In[35]:


sns.stripplot(x = "day", y = "total_bill", data = tips, jitter = True);


# ### Step 9. Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex

# In[36]:


sns.stripplot(x = 'tip',y = 'day',hue = 'sex',data = tips,jitter=True)


# ### Step 10.  Create a box plot presenting the total_bill per day differetiation the time (Dinner or Lunch)

# In[39]:


sns.boxplot(x = "day", y = "total_bill", hue = "time", data = tips);


# ### Step 11. Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.

# In[44]:


G = sns.FacetGrid(tips,col='time')
G.map(plt.hist,'tip')


# ### Step 12. Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip relationship, differing by smoker or no smoker
# ### They must be side by side.

# In[51]:


G2 = sns.FacetGrid(tips,col='sex',hue='smoker')
G2.map(plt.scatter,'total_bill','tip',alpha = 0.8)
G2.add_legend()


# ### BONUS: Create your own question and answer it using a graph.

# In[ ]:




