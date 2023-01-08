#!/usr/bin/env python
# coding: utf-8

# # Online Retails Purchase

# ### Introduction:
# 
# 
# 
# ### Step 1. Import the necessary libraries

# In[53]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv). 

# ### Step 3. Assign it to a variable called online_rt
# Note: if you receive a utf-8 decode error, set `encoding = 'latin1'` in `pd.read_csv()`.

# In[5]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv'

online_rt = pd.read_csv(url,encoding = 'latin1')

online_rt.head()


# ### Step 4. Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK

# In[15]:


countries = online_rt.groupby('Country').sum()
countries = countries.sort_values(by = 'Quantity',ascending = False)[1:11]
countries['Quantity'].plot(kind = 'bar')
plt.xlabel('Contries')
plt.ylabel('Quantity')
plt.show()


# ### Step 5.  Exclude negative Quantity entries

# In[18]:


online_rt = online_rt[online_rt.Quantity>0].reset_index(drop=True)
online_rt.head()


# ### Step 6. Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries (except UK)

# In[59]:


customer = online_rt.groupby(['CustomerID','Country']).sum()
customer['Country'] = customer.index.get_level_values(1)
top_countries = ['Netherlands', 'EIRE', 'Germany']
customer = customer[customer['Country'].isin(top_countries)]
S = sns.FacetGrid(customer,col='Country')
S.map(plt.scatter,'Quantity','UnitPrice')
S.add_legend()


# ### Step 7. Investigate why the previous results look so uninformative.
# 
# This section might seem a bit tedious to go through. But I've thought of it as some kind of a simulation of problems one might encounter when dealing with data and other people. Besides there is a prize at the end (i.e. Section 8).
# 
# (But feel free to jump right ahead into Section 8 if you want; it doesn't require that you finish this section.)
# 
# #### Step 7.1 Look at the first line of code in Step 6. And try to figure out if it leads to any kind of problem.
# ##### Step 7.1.1 Display the first few rows of that DataFrame.

# In[61]:


customer = online_rt.groupby(['CustomerID','Country']).sum()
customer.head()


# ##### Step 7.1.2 Think about what that piece of code does and display the dtype of `UnitPrice`

# In[63]:


customer.UnitPrice.dtype


# ##### Step 7.1.3 Pull data from `online_rt`for `CustomerID`s 12346.0 and 12347.0.

# In[70]:


display(online_rt[online_rt.CustomerID==12346.0].sort_values(by='UnitPrice',ascending = False).head())
display(online_rt[online_rt.CustomerID==12347.0].sort_values(by='UnitPrice',ascending= False).head())


# #### Step 7.2 Reinterpreting the initial problem.
# 
# To reiterate the question that we were dealing with:  
# "Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries"
# 
# The question is open to a set of different interpretations.
# We need to disambiguate.
# 
# We could do a single plot by looking at all the data from the top 3 countries.
# Or we could do one plot per country. To keep things consistent with the rest of the exercise,
# let's stick to the latter oprion. So that's settled.
# 
# But "top 3 countries" with respect to what? Two answers suggest themselves:
# Total sales volume (i.e. total quantity sold) or total sales (i.e. revenue).
# This exercise goes for sales volume, so let's stick to that.
# 
# ##### Step 7.2.1 Find out the top 3 countries in terms of sales volume.

# In[85]:


sales_volume = online_rt.groupby('Country').Quantity.sum().sort_values(ascending =False)
top3 = sales_volume.index[1:4]
top3


# ##### Step 7.2.2 
# 
# Now that we have the top 3 countries, we can focus on the rest of the problem:  
# "Quantity per UnitPrice by CustomerID".  
# We need to unpack that.
# 
# "by CustomerID" part is easy. That means we're going to be plotting one dot per CustomerID's on our plot. In other words, we're going to be grouping by CustomerID.
# 
# "Quantity per UnitPrice" is trickier. Here's what we know:  
# *One axis will represent a Quantity assigned to a given customer. This is easy; we can just plot the total  Quantity for each customer.  
# *The other axis will represent a UnitPrice assigned to a given customer. Remember a single customer can have any number of orders with different prices, so summing up prices isn't quite helpful. Besides it's not quite clear what we mean when we say "unit price per customer"; it sounds like price of the customer! A reasonable alternative is that we assign each customer the average amount each has paid per item. So let's settle that question in that manner.
# 
# #### Step 7.3 Modify, select and plot data
# ##### Step 7.3.1 Add a column to online_rt called `Revenue` calculate the revenue (Quantity * UnitPrice) from each sale.
# We will use this later to figure out an average price per customer.

# In[88]:


online_rt['Revenue'] = online_rt.Quantity * online_rt.UnitPrice
online_rt.head()


# ##### Step 7.3.2 Group by `CustomerID` and `Country` and find out the average price (`AvgPrice`) each customer spends per unit.

# In[112]:


G = online_rt[online_rt.Country.isin(top3)].groupby(['CustomerID','Country'])
plot = G['Quantity','Revenue'].agg('sum')
plot['AvgPrice'] = plot.Revenue /plot.Quantity
plot['Country'] = plot.index.get_level_values(1)
plot.head()


# ##### Step 7.3.3 Plot

# In[115]:


G2 = sns.FacetGrid(plot,col = 'Country')
G2.map(plt.scatter,'Quantity','AvgPrice',alpha=1)
G2.add_legend()


# #### Step 7.4 What to do now?
# We aren't much better-off than what we started with. The data are still extremely scattered around and don't seem quite informative.
# 
# But we shouldn't despair!
# There are two things to realize:
# 1) The data seem to be skewed towaards the axes (e.g. we don't have any values where Quantity = 50000 and AvgPrice = 5). So that might suggest a trend.
# 2) We have more data! We've only been looking at the data from 3 different countries and they are plotted on different graphs.
# 
# So: we should plot the data regardless of `Country` and hopefully see a less scattered graph.
# 
# ##### Step 7.4.1 Plot the data for each `CustomerID` on a single graph

# In[125]:


G3 = online_rt.groupby(['CustomerID'])
plot = G3['Quantity','Revenue'].agg('sum')
plot['AvgPrice'] = plot.Revenue/plot.Quantity
plt.scatter(plot.Quantity,plot.AvgPrice)
plt.plot


# ##### Step 7.4.2 Zoom in so we can see that curve more clearly

# In[127]:


G3 = online_rt.groupby(['CustomerID'])
plot = G3['Quantity','Revenue'].agg('sum')
plot['AvgPrice'] = plot.Revenue/plot.Quantity
plt.scatter(plot.Quantity,plot.AvgPrice)
plt.plot
plt.xlim(-40,2000) 
plt.ylim(-1,80)

plt.plot()


# ### 8. Plot a line chart showing revenue (y) per UnitPrice (x).
# 
# Did Step 7 give us any insights about the data? Sure! As average price increases, the quantity ordered decreses.  But that's hardly surprising. It would be surprising if that wasn't the case!
# 
# Nevertheless the rate of drop in quantity is so drastic, it makes me wonder how our revenue changes with respect to item price. It would not be that surprising if it didn't change that much. But it would be interesting to know whether most of our revenue comes from expensive or inexpensive items, and how that relation looks like.
# 
# That is what we are going to do now.
# 
# #### 8.1 Group `UnitPrice` by intervals of 1 for prices [0,50), and sum `Quantity` and `Revenue`.

# In[145]:


price_start = 0 
price_end = 50
price_interval = 1

bucket = np.arange(price_start,price_end,price_interval)

revenue_per_price = online_rt.groupby(pd.cut(online_rt.UnitPrice, bucket)).Revenue.sum()
revenue_per_price.head()


# #### 8.3 Plot.

# In[146]:


revenue_per_price.plot()
plt.xlabel('Unit Price (in intervals of '+str(price_interval)+')')
plt.ylabel('Revenue')
plt.show()


# #### 8.4 Make it look nicer.
# x-axis needs values.  
# y-axis isn't that easy to read; show in terms of millions.

# In[150]:


revenue_per_price.plot()
plt.xlabel('Unit Price (in intervals of '+str(price_interval)+')')
plt.ylabel('Revenue')
plt.xticks(np.arange(price_start,price_end,3),
          np.arange(price_start,price_end,3))
plt.yticks([0, 500000, 1000000, 1500000, 2000000, 2500000],
           ['0', '$0.5M', '$1M', '$1.5M', '$2M', '$2.5M'])


# ### BONUS: Create your own question and answer it.

# In[ ]:




