#!/usr/bin/env python
# coding: utf-8

# <h1>7.2. Finding the Cheaters</h1>

# In[2]:


import pandas as pd


# In[5]:


data = pd.read_csv('puzzle_anon.csv')
data


# In[6]:


data['Difference'] = data['start odds'] - data['end odds']


# In[7]:


data


# In[ ]:




