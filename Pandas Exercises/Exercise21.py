#!/usr/bin/env python
# coding: utf-8

# # Pokemon

# ### Introduction:
# 
# This time you will create the data.
# 
# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Create a data dictionary that looks like the DataFrame below

# In[15]:


data = {'evolution':['Ivysaur','Charmeleon','Wartortle','Metapod'],
        'hp':[45,39,44,45],
        'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
        'pokedex':['yes','no','yes','no'],
        'type':['grass','fire','water','bug']
    
}


# ### Step 3. Assign it to a variable called pokemon

# In[16]:


pokemon = pd.DataFrame(data)
pokemon


# ### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex

# In[17]:


pokemon = pokemon[['name', 'type', 'hp', 'evolution','pokedex']]
pokemon 


# ### Step 5. Add another column called place, and insert what you have in mind.

# In[18]:


pokemon['place']= ['desert','sea','swamp','forest']
pokemon


# ### Step 6. Present the type of each column

# In[23]:


pokemon.dtypes


# ### BONUS: Create your own question and answer it.

# In[ ]:




