#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to compute the inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension.

# In[10]:


import numpy as np 
arr1=np.array([11,12,13,14])
arr2=np.array([1,3,5,7])
result=np.inner(arr1,arr2)
print("inner for 1d arr")
print(result)
arr3= np.arange(9).reshape(3, 3)
arr4= np.arange(3, 12).reshape(3, 3)
result2 = np.inner(arr3,arr4)
print("inner for 2d arr")
print (result2)


# #### 2-Write a NumPy program to compute the cross product of two given vectors.
# 
# 

# In[17]:


a=[[5,6],[1,2]]
b=[[3,2],[4,7]]
result1=np.cross(a,b)
result2=np.cross(b,a)
print("cross product of two vectors(a, b):")
print(result1)
print("cross product of two vectors(b, a):")
print(result2)


# #### 3-Write a NumPy program to compute the outer product of two given vectors.
# 
# 

# In[24]:


p = [[15, 20], [10, 1]]
q = [[4, 2], [1, 1]]
print("Outer product \n",np.outer(p,q))


# #### 4-Write a NumPy program to compute the multiplication of two given matrixes.

# In[23]:


p=[[5,10],[5,5]]
q=[[4,3],[7,2]]
print("atrix multiplication: \n",np.dot(p,q))


# #### 5-Write a NumPy program to compute the determinant of an array.

# In[26]:


arr = np.array([[14,11],[5,5]])
result = np.linalg.det(arr)
print("the determinant of an array \n",result )


# #### 6-Write a NumPy program to compute the Kronecker product of two given mulitdimension arrays.
# 
# 

# In[41]:


arr1=np.array([1,5])
arr2=np.array([5,4])
result1=np.kron(arr1,arr2)
print("Kronecker product of 1d array \n",result1)
#Higher dimension
arr3=np.arange(9).reshape(3,3)
arr4=np.arange(4,13).reshape(3,3)
result2=np.kron(arr3,arr4)
print("Kronecker product  of 2d \n",result2)


# #### 7-Write a NumPy program to compute the sum of the diagonal element of a given array.
# 
# 

# In[43]:


arr=np.array([[1,2],[10,20]])
result= np.trace(arr)
print("the sum of the diagonal element:",result)


# #### 8-Write a NumPy program to compute the inverse of a given matrix.

# In[46]:


arr=np.array([[5,10],[16,4]])
result= np.linalg.inv(arr)
print(" the inverse of a given matrix: \n",result)


# In[ ]:




