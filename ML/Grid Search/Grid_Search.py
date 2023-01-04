#!/usr/bin/env python
# coding: utf-8

# In[28]:


from sklearn import datasets
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd


# In[8]:


digits = datasets.load_digits()


# In[24]:


models_param = {
    'svm': {
        'model': svm.SVC(gamma='auto'),
        'params' : {
            'C': [1,10,20],
            'kernel': ['rbf','linear']
        }  
    },
    'random_forest':{
        'model':RandomForestClassifier(),
         'params':{
          'n_estimators':[5,10,15]
         }
    },
    'logistic_regression':{
        'model': LogisticRegression(solver='liblinear',multi_class='auto'),
        'params':{
            "c":[1,2,3]
        }
    },
    'naive_bayes_gussian':{
        'model':GaussianNB(),
        'params':{}
    },
    'naive_base_Multinomail':{
        'model':MultinomialNB(),
         'params':{}
    },
    'Decision_tree':{
        'model':DecisionTreeClassifier(),
         'params':{
             'creterion':['gini','entropy'],
         }
    }
    
    
}


# In[43]:


score = []
for model_name, mod in model_params.items():
    mo =  GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
    mo.fit(digits.data, digits.target)
    score.append({
        'model': model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    
df = pd.DataFrame(score,columns=['model','best_score','best_params'])
df


# In[ ]:





# In[ ]:




