#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv("datasets/missinggrade.csv")
df.head()

df_no_missing = df.dropna()
df_no_missing


# In[4]:


df.fillna(0)


# In[9]:


import numpy as np
df['newcol'] = np.nan
df.head()


# In[10]:


df.fillna(0)


# In[20]:


df['grade'] = df['grade'].astype(float)


# In[21]:


df['grade'].unique()


# In[25]:


df['grade'].replace(' ', 0, inplace=True)


# In[26]:


df['grade'] = df['grade'].astype(float)


# In[27]:


df['grade'] = df['age'].astype(float)


# In[29]:


df.dtypes


# In[32]:


df.loc[(df['grade'] <= 0,'grade')] = 0
df.head()

