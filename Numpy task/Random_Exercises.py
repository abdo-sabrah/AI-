#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to generate six random integers between 10 and 30.

# In[5]:


import numpy as np
arr = np.random.randint(low = 10, high = 30, size = 6)
print(arr)


# #### 2-Write a NumPy program to create a 3x3x3 array with random values.
# 
# 

# In[7]:


arr = np.random.random((3,3,3))
arr


# #### 3-Write a NumPy program to create a random 10x4 array and extract the first five rows of the array and store them into a variable.
# 
# 

# In[12]:


arr=np.random.random((10,4))
print(arr)
y=arr[:5,:]
print("the first 5 rows \n" , y)


# #### 4-Write a NumPy program to shuffle numbers between 0 and 10 (inclusive).
# 
# 

# In[17]:


arr = np.arange(10)
print(arr)
np.random.shuffle(arr)
print("arr after shuffle \n",arr)


# #### 5-Write a NumPy program to normalize a 3x3 random matrix.
# 
# 

# In[ ]:


arr= np.random.random((3,3))
print(arr)
arrmx,arrmn = arr.max(),arr.min()
arr = (arr-arrmn)/(arrmx-arrmn)
print("arr after normalization \n",arr)


# #### 6-Write a NumPy program to find the nearest value from a given value in an array.
# 

# In[37]:


arr=np.random.uniform(1,12,5)
value = 10
nearest = arr.flat[(np.abs(arr-value).argmin())]
print(nearest)


# #### 7-Write a NumPy program to create random vector of size 15 and replace the maximum value by -1.
# 
# 
# 

# In[41]:


arr = np.random.random(10)
print(arr)
arr[arr.argmax()]=-1
print("arr after replace max value; \n",arr)


# #### 8-Write a NumPy program to check two random arrays are equal or not.
# 
# 

# In[51]:


arr1 = np.random.randint(0,10,5)
print("1-",arr1,"\n")
arr2 = np.random.randint(0,10,5)
print("2-",arr1,"\n")
array_equal = np.allclose (arr1,arr2)
array_equal


# #### 9-Write a NumPy program to find the closest value (to a given scalar) in an array.

# In[59]:


arr1 = np.arange(100)
print("original arr \n",arr1)
arr2 = np.random.uniform(0,100)
print("Value to compare: \n",arr2)
index = (np.abs(arr1-arr2)).argmin()
print("closest value in index \n",arr1[index])


# #### 10-Write a NumPy program to find the most frequent value in an array.
# 
# 

# In[66]:


arr = np.random.randint(0,20,15)
print ("the arr \n",arr)
x=np.bincount(arr).argmax()
x


# In[ ]:




