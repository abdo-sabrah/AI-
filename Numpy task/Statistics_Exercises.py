#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a Python program to find the maximum and minimum value of a given flattened array.
# 

# In[5]:


import numpy as np 
arr = np.arange(4).reshape((2,2))
print("original arr \n ,",arr)
mn= np.amin(arr)
mx = np.amax(arr)
print("arr min \n",mn)
print("arr max \n ",mx)


# #### 2-Write a NumPy program to get the minimum and maximum value of a given array along the second axis.
# 
# 

# In[7]:


arr = np.arange(4).reshape((2, 2))
print("Original array: \n",arr)
mx =  np.amax(arr, 1)
print("\nMaximum value along the second axis:",mx)
mn = np.amin(arr, 1)
print("Minimum value along the second axis",mn)


# #### 3-Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis

# In[20]:


arr = np.arange(12).reshape((2, 6))
print("Original array: \n",arr)

r1 = np.ptp(arr, 1)
result = np.amax(arr,1) - np.amin(arr,1)
assert np.allclose(r1,result)
print("Difference between the maximum and the minimum values of the said array: \n",r1)


# #### 4-Write a NumPy program to compute the 80th percentile for all elements in a given array along the second axis.
# 
# 

# In[26]:


arr = np.arange(12).reshape((2, 6))
print("Original array: \n",arr)
result = np.percentile(arr, 80, 1)
print("the 80th percentile for all elements in a given array : \n",result)


# #### 5-Write a NumPy program to compute the median of flattened given array.
# 

# In[29]:


arr = np.arange(12).reshape((2, 6))
print("Original array: \n",arr)
result = np.median(arr)
print ("the median of flattened given array : \n",result)


# #### 6-Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.
# 
# 

# In[33]:


arr = np.arange(6)
print("Original array: \n",arr)
r1 = np.mean(arr)
r2 = np.average(arr)
assert np.allclose(r1,r2)
print("mean \n ",r1)
r1 = np.std(arr)
r2 =  np.sqrt(np.mean((arr - np.mean(arr)) ** 2 ))
assert np.allclose(r1,r2)
print("std \n",r1)
r1 = np.var(arr)
r2 = np.mean((arr - np.mean(arr)) ** 2 )
assert np.allclose(r1,r2)
print("var \n",r1)


# #### 7-Write a NumPy program to compute the covariance matrix of two given arrays.
# 
# 

# In[37]:


arr1 = np.array([1,2,3,5,7])
print("arr 1 : \n",arr1)
arr2 = np.array ([1,2,4,6,9])
print("arr 2 : \n",arr2)
print("Covariance matrix : \n",np.cov(arr1, arr2))


# #### 8-Write a NumPy program to compute cross-correlation of two given arrays.
# 
# 

# In[39]:


arr1= np.array([0, 1, 3])
arr2= np.array([2, 4, 5])
print("array 1:")
print(arr1)
print(" array 2:")
print(arr2)
print("\nCross-correlation of the said arrays:\n",np.cov(arr1, arr2))


# #### 9-Write a NumPy program to compute pearson product-moment correlation coefficients of two given arrays.
# 
# 

# In[40]:


arr1 = np.array([1,2,3,5,7])
arr2 = np.array ([1,2,4,6,9])
print("array 1:")
print(arr1)
print(" array 2:")
print(arr2)
print("Pearson product-moment correlation coefficients of the said arrays:\n",np.corrcoef(arr1, arr2))


# #### 10-Write a NumPy program to compute the weighted of a given array.
# 
# 

# In[44]:


x = np.arange(5)
print("\nOriginal array:")
print(x)
weights = np.arange(1, 6)
r1 = np.average(x, weights=weights)
r2 = (x*(weights/weights.sum())).sum()
assert np.allclose(r1, r2)
print("\nWeighted average of the said array:")
print(r1)


# In[ ]:




