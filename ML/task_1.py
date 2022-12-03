#!/usr/bin/env python
# coding: utf-8

# <h3>Exercise</h3>

# <p >Predict canada's per capita income in year 2020. There is an exercise folder here on github at same level as this notebook, download that and you will find canada_per_capita_income.csv file. Using this build a regression model and predict the per capita income fo canadian citizens in year 2020</p>

# In[106]:


import pandas as pd
from warnings import simplefilter
simplefilter(action='ignore')
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df = pd.read_csv("canada_per_capita_income.csv")
income = df.drop("per capita income (US$)",axis="columns")
year =df["per capita income (US$)"]
reg = linear_model.LinearRegression()
reg.fit(income,year)
reg.predict([[2020]])


# <h3>Exercise<h3>

# In exercise folder (same level as this notebook on github) there is **hiring.csv**. This file contains hiring statics for a firm such as experience of candidate, his written test score and personal interview score. Based on these 3 factors, HR will decide the salary. Given this data, you need to build a machine learning model for HR department that can help them decide salaries for future candidates. Using this predict salaries for following candidates,
# 
# 
# **2 yr experience, 9 test score, 6 interview score**
# 
# **12 yr experience, 10 test score, 10 interview score**
# 

# In[110]:


from word2number import w2n
import math
data = pd.read_csv("hiring.csv")
data.experience = data.experience.fillna("zero")
data.experience = data.experience.apply(w2n.word_to_num)
median_test_score = math.floor(data["test_score(out of 10)"].mean()) 
data["test_score(out of 10)"] = data["test_score(out of 10)"].fillna(median_test_score) 
a = data.drop("salary($)",axis='columns')
b = data['salary($)']
reg2 = linear_model.LinearRegression()
reg2.fit(a,b)
reg2.predict([[2,9,6]])


# In[111]:


reg2.predict([[12,10,10]])

