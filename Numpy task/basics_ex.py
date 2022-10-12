#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to test whether any of the elements of a given array is non-zero.

# In[11]:


import numpy as np
arr1 = np.array([5,0,15,0,5,0])
print(np.any(arr1))
arr2 = np.array([0,0,0,0,0])
print (np.any(arr2))


# #### 2-Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
# 
# 

# In[15]:


arr= np.array([1,2,3,np.nan,np.inf])
print(np.isfinite(arr))


# #### 3-Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
# 
# 

# In[21]:


a1=np.array([1,2,3,4])
a2=np.array([1,3,5,4])
#greater
print(np.greater(a2,a1))
#greater or equal
print(np.greater_equal(a1,a2))
#less
print(np.less(a1,a2))
#less or equal 
print (np.less_equal(a2,a1))


# #### 4-Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

# In[28]:


e1= np.array([1,2,3,4,5,6,7,8,9])
e2= np.array([1,2,3,4,5,6,7.000001,8,9])
#is equal
print(np.equal(e1,e2))
#equal within a tolerance
print(np.allclose(e1,e2))


# #### 5-Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array. 

# In[35]:


S=np.array([1, 7, 13, 105])
print( "the size of the memory occupied by the array :"+str( S.size * S.itemsize))


# #### 6-Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

# In[36]:


#zeros
Zarr = np.zeros(10)
print(Zarr)
#ones
Oarr = np.ones(10)
print(Oarr)
#fives
Farr=np.ones(10)*5
print(Farr)


# #### 7-Write a NumPy program to create an array of the integers from 30 to 70.
# 
# 

# In[38]:


ar=np.arange(30,71)
print(ar)


# #### 8-Write a NumPy program to create an array of the integers from 30 to 70.
# 
# 

# In[39]:


ar2=np.arange(30,71,2)
print(ar2)


# #### 9-Write a NumPy program to create a 3x3 identity matrix.
# 
# 

# In[44]:


arrI=np.identity(3)  #or arrI =np.eye(3)
print(arrI)


# #### 10-Write a NumPy program to create a vector with values ​​ranging from 15 to 55 and print all values ​​except the first and last.
# 
# 

# In[47]:


V=np.arange(15,55)
print(V[1:-1])


# #### 11-Write a NumPy program to create a 3X4 array using and iterate over it.

# In[59]:


a= np.arange(10,22).reshape((3,4))
print(a)
#iterate
for i in np.nditer (a):
    print(i,end=" ")


# In[ ]:




