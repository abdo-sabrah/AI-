#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
from sklearn.datasets import load_digits
digits = load_digits()


# In[4]:


digits.target_names


# In[6]:


df = pd.DataFrame(digits.data,digits.target)


# In[9]:


df['target'] = digits.target


# In[11]:


df.describe()


# In[12]:


df.info()


# In[17]:


X= df.drop(['target'], axis='columns')
y = df.target


# In[18]:


from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=5)


# In[38]:


from sklearn.svm import SVC 
modelc = SVC(kernel="rbf")
modelc.fit(X_train,y_train)


# In[39]:


print(modelc.score(X_test, y_test))
print(modelc.score(X_train, y_train))


# In[40]:


model_2 =SVC(C= 10)
model_2.fit(X_train,y_train)
print(model_2.score(X_test, y_test))
print(model_2.score(X_train, y_train))


# In[44]:


_model = SVC(kernel='linear')
_model.fit(X_train,y_train)


# In[45]:


print(_model.score(X_test, y_test))
print(_model.score(X_train, y_train))


# In[ ]:





# In[ ]:





# In[ ]:




