#!/usr/bin/env python
# coding: utf-8

# # Visualizing the Titanic Disaster

# ### Introduction:
# 
# This exercise is based on the titanic Disaster dataset avaiable at [Kaggle](https://www.kaggle.com/c/titanic).  
# To know more about the variables check [here](https://www.kaggle.com/c/titanic/data)
# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv)

# ### Step 3. Assign it to a variable titanic 

# In[4]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv'
titanic = pd.read_csv(url)
titanic.head(5)


# ### Step 4. Set PassengerId as the index 

# In[8]:


titanic.set_index('PassengerId',inplace= True)
titanic.head()


# ### Step 5. Create a pie chart presenting the male/female proportion

# In[19]:


male = (titanic['Sex']=='male').sum()
female = (titanic['Sex']=='female').sum()
Type = [male,female]
plt.pie(Type, labels = ['Males', 'Females'],
        explode = (0.15,0),
        autopct = '%1.1f%%')
plt.axis('equal')
plt.title("Sex Proportion")
plt.show()


# ### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender

# In[27]:


S = sns.lmplot(x = 'Fare',y='Age',hue = 'Sex',data = titanic,fit_reg=False)
#S=sns.jointplot(x = 'Fare',y='Age',hue = 'Sex',data = titanic)


# ### Step 7. How many people survived?

# In[30]:


titanic.Survived.sum()


# ### Step 8. Create a histogram with the Fare payed

# In[38]:


df = titanic.Fare.sort_values(ascending=False)
bins = np.arange(0,400,10)
plt.hist(df,bins=bins)
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')


# ### BONUS: Create your own question and answer it.

# In[ ]:




