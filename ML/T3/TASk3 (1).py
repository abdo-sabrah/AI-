#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import numpy as np 
df = pd.read_csv("titanic.csv")
df.dropna(inplace=True)
df2 = df[["Pclass","Sex","Age","Fare"]]
target = df ["Survived"]
sex = LabelEncoder()

df2['sex_n'] = sex.fit_transform(df2['Sex'])
df3 = df2.drop('Sex',axis=1)
faverage = df2 [df2['Sex']=='female']['Age'].mean()
maverage = df2[df2['Sex']=='male']['Age'].mean()
df3[df3['sex_n']==0]['Age']=df3[df3['sex_n']==0]['Age'].isna().replace(0,faverage)
df3[df3['sex_n']==1]['Age']= df3[df3['sex_n']==1]['Age'].isna().replace(1,maverage)


# In[41]:


from sklearn import tree
from sklearn.model_selection import train_test_split 
model = tree.DecisionTreeClassifier()
xtrain,xtest,ytrain,ytest = train_test_split (df3,target,test_size= 0.25,random_state = 0)
model.fit(xtrain,ytrain)
y_pred = model.predict(xtest)
print (model.score(xtrain,ytrain))
print(model.score(xtest,ytest))


# In[50]:


model.predict([[3,22,7.2500,0]])


# In[ ]:




