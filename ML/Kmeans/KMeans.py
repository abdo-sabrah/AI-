#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


iris = load_iris()


# In[28]:


df = pd.DataFrame(iris.data,columns=iris.feature_names)
df


# In[29]:


df['flower'] = iris.target
df


# In[30]:


df.drop(['sepal length (cm)', 'sepal width (cm)', 'flower'],axis='columns',inplace=True)


# In[36]:


k = KMeans(n_clusters=3)
Clusters = k.fit_predict(df)
Clusters


# In[38]:


df["cluster"]=Clusters
df


# In[42]:


df1 = df[df.cluster==0]
df2 = df [df.cluster==1]
df3 = df [df.cluster==2]


# In[44]:


plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color= "black")
plt.scatter(df2['petal length (cm)'],df2['petal width (cm)'],color='red')
plt.scatter(df3['petal length (cm)'],df3['petal width (cm)'],color='blue')


# In[62]:


sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df)
    sse.append(km.inertia_)


# In[64]:


plt.xlabel('K')
plt.ylabel('Sum of squared error')
k_rng = range(1,10)
plt.plot(k_rng,sse)


# In[57]:





# In[ ]:




