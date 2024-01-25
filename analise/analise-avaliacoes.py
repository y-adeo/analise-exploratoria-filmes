#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd




# In[3]:


notas = pd.read_csv('ratings.csv')
notas.head()


# In[4]:


notas.columns=["usuario.ID", "felmeID", "nota", 'momento']
notas.head()


# In[5]:


notas['nota']


# In[6]:


notas['nota'].value_counts()


# In[7]:


notas['nota'].mean()


# In[8]:


notas.nota.head()


# In[9]:


notas.nota.plot()


# In[10]:


notas.nota.plot(kind='hist')


# In[14]:


print("Media:",notas['nota'].mean())
print("Mediana:",notas['nota'].median())


# In[15]:


notas.nota.describe()


# In[16]:


import seaborn as sns

sns.boxplot(notas.nota)


# In[ ]:




