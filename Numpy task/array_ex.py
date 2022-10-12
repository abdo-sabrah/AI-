#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.
# 
# 

# In[1]:


import numpy as np
l = [1,2,3,4,5,4]
print(l)
darr=np.array(l)
print(darr)


# #### 3-Write a NumPy program to convert an array to a float type

# In[8]:


arr=np.array([1,2,3,4,5,6],dtype="int16")
print(arr.dtype)
arr=arr.astype(np.float32)
print ("arr after convert:"+str(arr)) #or print(np.asfarray(arr))


# #### 4-Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
# 
# 

# In[20]:


arr=np.ones((5,5))
print(arr)
arr[1:-1,1:-1]=0
print("2d array with 1 on the border and 0 inside \n"+ str(arr))


# #### 5-Write a NumPy program to convert the values of Fahrenheit degrees into Centigrade degrees . Values are stored into a NumPy array.

# In[28]:


fvalues = [0, 12, 45.21, 34, 99.91, 32]
F=np.array(fvalues)
C=np.round((5*F/9 - 5*32/9),2)
print("Values in  Centigrade degrees"+str(C))


# #### 6-Write a NumPy program to create an empty and a full array.
# 
# 

# In[36]:


arr =np.empty((3,4))
print(arr)
f=np.full((3,4) , 10)
print(" full arr :")
print (f)


# #### 7-Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
# 

# In[37]:


arr1=np.array([1,2,3,4,5,6])
arr2=np.array([1,4,6,5])
print(np.in1d(arr1,arr2))


# #### 8-Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
# 
# 

# In[39]:


arr1=np.array([1,2,3,4,5])
arr2=np.array([2,4,6,8])
print(np.setdiff1d(arr1,arr2))


# #### 9-Write a NumPy program to test whether all elements in an array evaluate to True.
# 

# In[46]:


print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([[False,False],[False,0]]))
print(np.all([10,20,30,0]))
print(np.all([10,20,30,40]))


# #### 10-Write a NumPy program to construct an array by repeating.
# 

# In[50]:


arr=[10,20,30,40,60]
arr=np.tile(arr,5)
print ("Repeating 5 times",arr)


# #### 11-Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.
# 
# 

# In[52]:


arr=np.array([10,20,30,40,50,60])
print("max value is in ",np.argmax(arr))
print("min value is in ",np.argmin(arr))


# In[ ]:




