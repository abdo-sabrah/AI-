#!/usr/bin/env python
# coding: utf-8

# In[34]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
data = load_iris()
df = pd.DataFrame(data.data,columns = data.feature_names)
df['target'] = data.target
x = df.drop('target',axis= 'columns')
y = data.target  
xtrain,xtest,ytrain,ytest = train_test_split (x,y,test_size= 0.25,random_state = 0)
model = RandomForestClassifier(n_estimators=5)
model.fit(xtrain, ytrain)
model.score(xtest,ytest)


# In[ ]:




