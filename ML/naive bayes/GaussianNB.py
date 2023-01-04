#!/usr/bin/env python
# coding: utf-8

# In[18]:


from sklearn import datasets
import pandas as pd
wine = datasets.load_wine()
df = pd.DataFrame(wine.data,columns = wine.feature_names)
df.describe


# In[28]:


df['target'] = wine.target
df


# In[26]:


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
X_train,X_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size=0.5,random_state=3)
model = GaussianNB()
model.fit(X_train,y_train)


# In[27]:


print(model.score(X_train,y_train))
print(model.score(X_test,y_test))


# In[ ]:




