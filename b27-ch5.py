#!/usr/bin/env python
# coding: utf-8

# <h1> Sec 5.2. Pandas Exercises </h1>

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


pwd


# In[3]:


ls


# In[4]:


df1 = pd.read_csv('the-movies-dataset/movies_metadata.csv')
df1.head(2)


# In[5]:


df1.shape


# In[6]:


df1.columns


# In[7]:


df1.index


# In[8]:


df1.dtypes


# In[9]:


print(df1.describe())


# <h1>5.3. Filtering the Data</h1>

# In[10]:


df1['budget'] = pd.to_numeric(df1['budget'],errors='coerce')
budget_df = df1[df1['budget']>1000000]
budget_df


# <b>Create a Series object called budget_lookup such that you are able to use a call to budget_lookup['Dead Presidents'] to find the budget of that movie.</b>

# In[11]:


budget_lookup = budget_df['budget']
budget_lookup.index = budget_df['title']
budget_lookup['Dead Presidents']


# In[12]:


budget_lookup[budget_lookup.index.str.startswith('A')].sort_index()[[0]]


# In[13]:


budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]]


# In[14]:


budget_lookup_as_and_bs = budget_lookup.sort_index()['A Bag of Hammers':'Byzantium']
budget_lookup_as_and_bs.shape


# <h1>5.4. Numbers as indices</h1>

# <h3>Create a Series called time_scheduler that is indexed by runtime and has the movie’s title as its values. Note that you will need to use sort_index() in order to be able to look up movies by their duration. Base yourself on df rather than budget_df.</h3>

# In[15]:


df1['runtime'] = pd.to_numeric(df1['runtime'],errors='coerce')
runtime_df = df1[(df1['runtime']<=180) & (df1['runtime']>= 10)]
time_scheduler = runtime_df['title']
time_scheduler.index = runtime_df['runtime']


# <h2>But what is the 154th shortest movie in this collection?</h2>

# In[16]:


movie_number_154 = time_scheduler.sort_index().iloc[154]
movie_number_154


# <h1>5.5. Dealing with multiple DataFrames</h1>

# Let’s create a variable called df_high_rated that only contains movies that have received more than 20 votes and whose average score is greater than 8.

# In[17]:


df1['vote_average'] = pd.to_numeric(df1['vote_average'],errors='coerce')
df1['vote_count'] = pd.to_numeric(df1['vote_count'], errors='coerce')


# In[18]:


df_high_rated = df1[(df1['vote_average'] > 8) & (df1['vote_count'] > 20)]


# In[19]:


df_high_rated.shape


# Here are my favorite movies and their relative scores. Create a DataFrame called compare_votes that contains the title as an index and both the vote_average and my_vote as its columns. Also only keep the movies that are both my favorites and popular favorites.
# 
# HINT: You’ll need to create two Series, one for my ratings and one that maps titles to vote_average.

# In[20]:


my_ratings = pd.Series({
    "Star Wars": 9,
    "Paris is Burning": 8,
    "Dead Poets Society": 7,
    "The Empire Strikes Back": 9.5,
    "The Shining": 8,
    "Return of the Jedi": 8,
    "1941": 8,
    "Forrest Gump": 7.5,
})


# In[42]:


their_votes = df1['vote_average']
their_votes.index = df1['title']
their_votes = their_votes.loc[my_ratings.index]


# In[39]:


compare_votes = pd.DataFrame({'My Vote': my_ratings, 'Their Vote':their_votes})


# In[49]:


compare_votes['% Difference'] = (compare_votes['Their Vote'] - compare_votes['My Vote']) / compare_votes['Their Vote']


# In[50]:


compare_votes


# In[ ]:




