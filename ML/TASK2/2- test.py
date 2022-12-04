#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all the lib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# In[2]:


# read the dataset using pandas
data = pd.read_csv('Salary_Data.csv')


# In[3]:


# This displays the top 5 rows of the data
data.head()


# In[4]:


# Provides some information regarding the columns in the data
data.info()


# In[5]:


# this describes the basic stat behind the dataset used 
data.describe()


# In[55]:


# These Plots help to explain the values and how they are scattered
plt.scatter(x, y)
plt.show()
# Plot a scatter plot 


# In[7]:


# Cooking the data
X = data['YearsExperience']
X.head()


# In[8]:


# Cooking the data
y = data['Salary']
y.head()


# In[35]:


# Split the data for train and test (70% for training)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)


# In[36]:


# Create new axis for x column
X_train = X_train[:,np.newaxis]
X_test = X_test[:,np.newaxis]


# In[44]:


# Importing Linear Regression model from scikit learn
from sklearn.linear_model import LinearRegression


# In[45]:


# Fitting the model
reg = LinearRegression()
reg.fit(x_train,y_train)


# In[46]:


# Predicting the Salary for the Test values
y_pred =  reg.predict(x_test)


# In[15]:


# Plotting the actual and predicted values

c = [i for i in range (1,len(y_test)+1,1)]
plt.plot(c,y_test,color='r',linestyle='-')
plt.plot(c,y_pred,color='b',linestyle='-')
plt.xlabel('Salary')
plt.ylabel('index')
plt.title('Prediction')
plt.show()


# In[16]:


# plotting the error
c = [i for i in range(1,len(y_test)+1,1)]
plt.plot(c,y_test-y_pred,color='green',linestyle='-')
plt.xlabel('index')
plt.ylabel('Error')
plt.title('Error Value')
plt.show()


# In[50]:


# Importing r2_score and mean_squared_error for the evaluation of the model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# In[51]:


# calculate Mean square error
mean_squared_error(y_test,y_pred)


# In[53]:


# Calculate R square vale
score = r2_score(y_pred,y_test)


# In[54]:


# Just plot actual and predicted values for more insights
plt.figure(figsize=(12,6))
plt.scatter(y_test,y_pred,color='r',linestyle='-')
plt.show()


# In[22]:


# Intecept and coeff of the line
print('Intercept of the model:',lr.intercept_)
print('Coefficient of the line:',lr.coef_)


# ![](http://)Then it is said to form a line with
# # y = 25202.8 + 9731.2x
