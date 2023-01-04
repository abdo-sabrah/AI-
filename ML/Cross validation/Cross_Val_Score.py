#!/usr/bin/env python
# coding: utf-8

# In[17]:


from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# In[2]:


iris = load_iris()


# In[29]:


l_scores = cross_val_score(LogisticRegression(), iris.data, iris.target,cv=4)
np.average(l_scores)


# In[28]:


d_score = cross_val_score(DecisionTreeClassifier(),iris.data,iris.target,cv=4)
np.average(d_score)


# In[26]:


s_scores = cross_val_score(SVC(), iris.data, iris.target,cv= 4)
np.average(s_scores)


# In[38]:


r_score = cross_val_score(RandomForestClassifier(n_estimators=10),iris.data, iris.target,cv= 4)
np.average(r_score)


# In[ ]:




