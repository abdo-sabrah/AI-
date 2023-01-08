#!/usr/bin/env python
# coding: utf-8

# # Wind Statistics

# ### Introduction:
# 
# The data have been modified to contain some missing values, identified by NaN.  
# Using pandas should make this exercise
# easier, in particular for the bonus question.
# 
# You should be able to perform all of these operations without using
# a for loop or other looping construct.
# 
# 
# 1. The data in 'wind.data' has the following format:

# In[434]:


"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""


#    The first three columns are year, month and day.  The
#    remaining 12 columns are average windspeeds in knots at 12
#    locations in Ireland on that day.   
# 
#    More information about the dataset go [here](wind.desc).

# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd
import datetime


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data)

# ### Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

# In[5]:


data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(data_url, sep = "\s+", parse_dates = [[0,1,2]]) 
data.head()


# ### Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.

# In[12]:


def EditCentury(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(EditCentury)

data.head()


# ### Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

# In[28]:


data.index = pd.to_datetime(data.index)
month_index = data.index.to_period('M')
data.head()


# ### Step 6. Compute how many values are missing for each location over the entire record.  
# #### They should be ignored in all calculations below. 

# In[14]:


data.isnull().sum()


# ### Step 7. Compute how many non-missing values there are in total.

# In[15]:


data.notnull().sum()


# ### Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
# #### A single number for the entire dataset.

# In[16]:


data.sum().sum() / data.notna().sum().sum()


# ### Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
# 
# #### A different set of numbers for each location.

# In[17]:


data.describe(percentiles=[])


# ### Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# 
# #### A different set of numbers for each day.

# In[18]:


day_stats = pd.DataFrame()

day_stats['min'] = data.min(axis = 1) 
day_stats['max'] = data.max(axis = 1) 
day_stats['mean'] = data.mean(axis = 1)
day_stats['std'] = data.std(axis = 1) 

day_stats.head()


# ### Step 11. Find the average windspeed in January for each location.  
# #### Treat January 1961 and January 1962 both as January.

# In[33]:


data.loc[data.index.month == 1].mean()


# ### Step 12. Downsample the record to a yearly frequency for each location.

# In[34]:


data.groupby(data.index.to_period('A')).mean()


# ### Step 13. Downsample the record to a monthly frequency for each location.

# In[32]:


data.groupby(data.index.to_period('M')).mean()


# ### Step 14. Downsample the record to a weekly frequency for each location.

# In[30]:


data.groupby(data.index.to_period('W')).mean()


# ### Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

# In[31]:


weekly = data.resample('W').agg(['min','max','mean','std'])

weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10)


# In[ ]:





# In[ ]:





# In[ ]:




