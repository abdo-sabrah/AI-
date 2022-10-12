#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.

# In[11]:


import numpy as np
arr =np.array([[10,40],[30,20]])
print("original arr \n",arr)
arr1= np.sort(arr,axis =0)
print("sort arr along first axis \n",arr1)
arr2 = np.sort(arr)
print("sort arr along lasr axis \n",arr2)
arr3=np.sort(arr,axis=None)
print("Sort the flattened arr \n",arr3)


# #### 2-Write a NumPy program to partition a given array in a specified position and move all the smaller elements values to the left of the partition, and the remaining values to the right, in arbitrary order (based on random choice).
# 
# 
# 

# In[45]:


arr = np.array([10,20,30,40,-10,50,-60])
print("the original arr \n",arr)
arr2 = np.partition(arr,5)
print(arr2)


# #### 3-Write a NumPy program to sort the specified number of elements from beginning of a given array.
# 
# 

# In[34]:


arr = np.random.rand(10)
print("the original arr \n",arr)
arr2 = arr[np.argpartition(arr,range(5))]
print("the sorted arr \n",arr2)


# #### 4-Write a NumPy program to sort a given complex array using the real part first, then the imaginary part.
# 
# 

# In[47]:


complex_num = [1 + 2j, 3 - 1j, 3 - 2j, 4 - 3j, 3 + 5j]
print(complex_num)

print("complex num after sort \n",np.sort_complex(complex_num))


# #### 5-Write a NumPy program to get the indices of the sorted elements of a given array.
# 
# 

# In[50]:


arr = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
print("original arr \n",arr)
arr1= np.argsort(arr)
print("the indices \n ",arr1)


# #### 6-Write a NumPy program to sort the student id with increasing height of the students from given students id and height. Print the integer indices that describes the sort order by multiple columns and the sorted data.
# 
# 

# In[56]:


student_id = [1030,4030,2100,1200,7000,4000,5040]
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
indices = np.lexsort((student_id, student_height))
print("the indices ",indices)
print("sorted array \n")
for i in indices:
    print(student_id[i],student_height[i])


# #### 7-Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal.
# 
# 

# In[64]:


data_type= [('name' , 'S15'),('class' , 'int'),('height' , 'float')]
student_details = [('ali', 4, 48.5), ('ahmed', 6, 52.5),('salah', 5, 42.10), ('ola', 7, 50.11)]
student = np.array(student_details,dtype=data_type)
print("student : \n",student)
arr1 = np.sort(student, order=['class', 'height'])
print ("student after sort : \n",arr1)


# #### 8-Write a NumPy program to sort an given array by the nth column.
# 
# 

# In[66]:


arr = np.random.randint(0,10,(3,3))
print(arr)
print("Sort the said array by the nth column: \n")
print(arr[arr[:,1].argsort()])


# In[ ]:




