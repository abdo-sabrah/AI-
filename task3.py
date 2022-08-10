#!/usr/bin/env python
# coding: utf-8

# In[32]:





# In[31]:


def binary_search( blist , n ) :
    l = 0 
    h = len (blist) - 1 
    mid = 0 
    while l <= h :
        mid = (l  + h ) // 2
        if blist[mid] < n :
            l = mid + 1 
        elif blist[mid] > n : 
            h = mid - 1 
        else :
            return mid
    return -1
blist = [1,2,3,4,5,6,7,8,9,10]
n = 8 
r = binary_search (blist,n)
if (r!= -1) :
    print("element found at pos " ,str(r))
else :
    print ("element not found ")
        


# In[29]:


#iterative
def sum1 (num) :
    sum =0
    for i in range (0,num+1) :
        sum =sum + i 
    return sum
r = sum1 (10)
print (str(r))

    


# In[23]:


#recursion
def sum2 (num):
    if num <= 1 :
        return num
    else:
        return num + sum2 (num-1)

r =sum2(10)
print (r)


# In[6]:





# In[ ]:




