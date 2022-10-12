#!/usr/bin/env python
# coding: utf-8

# #### 1-Write a NumPy program to concatenate element-wise two arrays of string.
# 
# 

# In[7]:


import numpy as np
arr1 = np.array(['A', 'B'], dtype= np.str)
arr2 = np.array(['C', ' D'], dtype=np.str)
print("Array1:",arr1)
print("Array2:",arr2)
new_array = np.char.add(arr1, arr2)
print("new array:")
print(new_array)


# #### 2-Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the elements of a given array.
# 
# 

# In[15]:


arr = np.array(['ali', 'alaa', 'syed', 'abdo'], dtype=str)
print("Original Array: \n",arr)
c = np.char.capitalize(arr)
l = np.char.lower(arr)
u = np.char.upper(arr)
t = np.char.title(arr)
s = np.char.swapcase(arr)
print("\nCapitalized: ", c)
print("Lowered: ", l)
print("Uppered: ", u)
print("Swapcased: ", s)
print("Titlecased: ", t)


# #### 3-Write a NumPy program to make the length of each element 15 of a given array and the string centered / left-justified / right-justified with paddings of _.
# 
# 

# In[19]:


arr = np.array(['book', 'cat', 'dog', 'fish'], dtype=str)
print("Original Array: \n",arr)
c = np.char.center(arr, 15, fillchar='_')
l = np.char.ljust(arr,15,fillchar= "_")
r = np.char.rjust(arr,15,fillchar= "_")
print("\nCentered =", c)
print("Left =", l)
print("Right =", r)


# #### 4-Write a NumPy program to insert a space between characters of all the elements of a given array.
# 
# 

# In[22]:


arr = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype= str)
print("Original Array: \n",arr)
arr2= np.char.join(" ", arr)
print(arr2)


# #### 5-Write a NumPy program to encode all the elements of a given array in cp500 and decode it again.
# 
# 

# In[28]:


arr = np.array(['book', 'cat', 'dog', 'fish'], dtype=str)
print("Original Array: \n",arr)
encode = np.char.encode(arr,'cp500') 
decode = np.char.decode(encode,'cp500')
print("\nencoded =", encode)
print("decoded =", decode)


# #### 6-Write a NumPy program to remove the leading and trailing whitespaces of all the elements of a given array.
# 
# 

# In[31]:


arr = np.array(['   abc  ','  ABC', '  NO      '])
print("Original Array: \n",arr)
stripped = np.char.strip(arr)
print("\nRemove the leading and trailing whitespaces: ", stripped)


# #### 7- Write a NumPy program to remove the leading whitespaces of all the elements of a given array.
# 
# 

# In[34]:


arr = np.array(['   abc  ','  ABC', '     NO      '])
print("Original Array: \n",arr)
lstripped_char = np.char.lstrip(arr)
print("Remove the leading whitespaces : ", lstripped_char)


# #### 8-Write a NumPy program to remove the trailing whitespaces of all the elements of a given array.
# 
# 

# In[37]:


arr = np.array(['   abc  ','  ABC', '     NO      '])
print("Original Array: \n",arr)
fstripped_char = np.char.rstrip(arr)
print("Remove the leading whitespaces : ", fstripped_char)


# #### 9-Write a NumPy program to split the element of a given array with spaces.
# 
# 

# In[40]:


arr = np.array(["Easy to get easy to go"])
print("Original Array: \n",arr)
r = np.char.split(arr)
print("\nSplit the element of the said array with spaces: ",r)


# #### 10-Write a NumPy program to split the element of a given array to multiple lines.

# In[52]:


arr = np.array(['Python\ , Practice, Solution'],dtype = str)
print("Original Array: \n",arr)
r = np.char.splitlines(arr)
print(r)


# In[ ]:




