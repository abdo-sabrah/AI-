#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to add, subtract, multiply, divide arguments element-wise.
# 

# In[9]:


import numpy as np
print("add \n",np.add(1.5,1))
print("substract \n",np.subtract(1.5, 10))
print("multipy\n" ,np.multiply(1.0, 4.0))
print("divide \n", np.divide(15, 5.5))


# #### 2-Write a NumPy program to get true division of the element-wise array inputs.
# 
# 

# In[13]:


arr = np.arange(10)
print("original arr \n",arr)
result = np.true_divide(arr,2)
print("true division of the element-wise array inputs \n",result)


# #### 3-Write a NumPy program to get the largest integer smaller or equal to the division of the inputs.
# 
# 

# In[18]:


arr = np.arange(10)
print("original arr ",arr)
result = np.floor_divide(arr,2)
print(" largest integer smaller or equal to the division of the inputs \n",result)


# #### 4-Write a NumPy program to get the powers of an array values element-wise.
# 

# In[19]:


arr = np.arange(10)
print("original arr",arr)
result = np.power(arr,3)
print("the powers of an array values element-wise \n",result)


# #### 5-Write a NumPy program to get the element-wise remainder of an array of division.
# 
# 

# In[21]:


arr = np.arange(14)
print("original arr",arr)
result = np.remainder(arr,4) 
print(" element-wise remainder of an array of division \n",result)


# #### 6-Write a NumPy program to round elements of the array to the nearest integer.
# 
# 

# In[22]:


arr = np.array([0.7,0.5,1.5,10.14,5.05,7.80,4.002])
print("original arr",arr)
result = np.rint(arr)
print("ound elements of the array to the nearest integer.\n",result)


# #### 7-Write a NumPy program to round array elements to the given number of decimals.
# 
# 

# In[31]:


arr1 = np.round([1.5,5.2,5.05])
print(arr1)
arr2=np.round([0.1,0.5,0.05,0.6],decimals=1)
print(arr2)
arr3 = np.round([.5, 1.5, 2.5, 3.5, 4.5])
print(arr3)


# #### 8-Write a NumPy program to multiply a 5x3 matrix by a 3x2 matrix and create a real matrix product.
# 
# 

# In[34]:


arr1 = np.random.random((5,3))
print("first arr : \n",arr1)
arr2 = np.random.random((3,2))
print("sec arr : \n",arr2)
result=np.dot(arr1,arr2)
print("the result is : \n",result)


# #### 9-Write a NumPy program to calculate mean across dimension, in a 2D numpy array.
# 
# 

# In[37]:


arr = np.array([[10,20],[30,40]])
print("original arr : \n",arr)
m1 = arr.mean(axis=0)
print("Mean of each column: \n" ,m1)
m2 =  arr.mean(axis=1)
print("Mean of each row: \n" ,m2)


# #### 10-Write a NumPy program to calculate the difference between neighboring elements, element-wise of a given array.
# 
# 

# In[41]:


arr = np.array([1,5,3,14,10])
print("Original array:", arr)
dif = np.diff(arr)
print("Difference between neighboring elements, element-wise of the said array. \n",dif)


# In[ ]:




