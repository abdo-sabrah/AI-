#!/usr/bin/env python
# coding: utf-8

# In[26]:


#1
for i in range (1499,2699,5):
    if (i%7==0):
        
        print (i) 


# In[1]:


#2
def Isfahrenheit():
    print ( "is your numb Celsius OR Fahrenheit")
    kind = input () 
    if kind == "Fahrenheit" :
        return True
    else:
        return False
     


# In[107]:




    if Isfahrenheit() : 
        print("please enter your num")
        num = float(input())
        sum =  ( (num-32) * 5 ) /9
        print ("your number after convert is " + str (sum))
       
    else:
        print("please enter your num")
        num = float(input())
        sum = (num*9) /5 +32 
        print ("your number after convert is =" + str(sum))

 


# In[2]:


#3

for i in range(6) :   
    
    for x in range (i):
        print("*",end="")
    print()
for i in range(6) :   
    
    for x in range (i,6):
        print("*",end="")
    print()


# In[3]:


#4
print ("please enter a name")
name= input()
for i in range (len(name)-1 ,-1, -1 ):
    print(name[i],end="")


# In[ ]:


#5
def findmax (x ,y ,z):
    max=0
    if(x >=y) and (x>=z) :
         maxnum =x
    elif(y>=x) and( y >= z):
        maxnum=y
    else:
        maxnum=z
    return maxnum
x = 1661
y = 42564
z = 54354
print(findmax(x, y, z))


# In[ ]:


#6
def sum_all (num):
    total=0
    for i in num :
        total+=i
    return total
print(sum_all([10,20,30]))


# In[ ]:


#7
for i in range (0,6) :
    if i == 3 :
        continue
    print(i)


# In[32]:


#8
def factorial(num):
    fact=1
    for i in range(1 , num+1):
        fact= fact*i
    return fact
print ("enter number")
x=int(input())
if x <= 0 :
    print("Wrong input")
print(factorial(x))
    


# In[30]:


#9
def unique_elements (l) :
    ul = []
    for i in l :
        if i not in ul :
            ul.append(i)
    return ul
print (unique_elements ([15,20,20,15,13,14,13]))
    


# In[37]:


#10
add15 = lambda num : num + 15
multiply = lambda x,y:  x * y
print (add15(10))
print(multiply(9,10)) 
 


# In[35]:



r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
Sample Output:


# In[ ]:




