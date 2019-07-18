#!/usr/bin/env python
# coding: utf-8

# <h1>8.1. UN General Debates</h1>

# In[1]:


get_ipython().magic(u'matplotlib inline')
import string
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sbn
from altair import Chart, X, Y, Color, Scale
import altair as alt
from vega_datasets import data
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
matplotlib.style.use('ggplot')


# In[2]:


pwd


# In[3]:


undf = pd.read_csv('un-general-debates.csv')


# In[4]:


len(undf)


# In[5]:


undf.sort_values('year', ascending=False).head()


# In[6]:


pd.set_option('display.max_colwidth', -1)
print(undf[(undf.year == 1970) & (undf.country == 'USA')].text)
pd.set_option('display.max_colwidth', 50)


# In[7]:


by_year = undf.groupby('year', as_index=False)['text'].count()
by_year.head()


# In[8]:


alt.Chart(by_year).mark_bar().encode(x='year:N',y='text')


# In[9]:


by_country = undf.groupby('country',as_index=False)['text'].count()
by_country.head()


# alt.Chart(by_country,title='speech distribution').mark_bar().encode(x=alt.X('text',bin=True),y='count()')

# In[11]:


by_country.loc[by_country.text.idxmax()]


# In[12]:


by_country.loc[by_country.text.idxmin()]


# In[13]:


c_codes = pd.read_csv('country_codes.csv', encoding = 'iso-8859-1')
c_codes.head()


# In[14]:


topics = [' nuclear', ' weapons', ' nuclear weapons', ' chemical weapons',
          ' biological weapons', ' mass destruction', ' peace', ' war',
          ' nuclear war', ' civil war', ' terror', ' genocide', ' holocaust',
          ' water', ' famine', ' disease', ' hiv', ' aids', ' malaria', ' cancer',
          ' poverty', ' human rights', ' abortion', ' refugee', ' immigration',
          ' equality', ' democracy', ' freedom', ' sovereignty', ' dictator',
          ' totalitarian', ' vote', ' energy', ' oil',  ' coal',  ' income',
          ' economy', ' growth', ' inflation', ' interest rate', ' security',
          ' cyber', ' trade', ' inequality', ' pollution', ' global warming',
          ' hunger', ' education', ' health', ' sanitation', ' infrastructure',
          ' virus', ' regulation', ' food', ' nutrition', ' transportation',
          ' violence', ' agriculture', ' diplomatic', ' drugs', ' obesity',
          ' islam', ' housing', ' sustainable', 'nuclear energy']


# In[15]:


undf.head()


# In[16]:


year_summ = undf.groupby('year', as_index=False)['text'].sum()


# In[17]:


year_summ.head()


# In[18]:


year_summ['gw'] = year_summ.text.str.count('global warming')
year_summ['cc'] = year_summ.text.str.count('climate change')
year_summ


# In[19]:


alt.Chart(year_summ[['year', 'gw', 'cc']]).mark_line().encode(x='year',y='gw')


# In[20]:


alt.Chart(year_summ[['year', 'gw', 'cc']].melt(id_vars='year', value_vars=['cc','gw'])
         ).mark_line().encode(x='year:O',y='value', color='variable')


# In[21]:


year_summ['pollution'] = year_summ.text.str.count('pollution')


# In[22]:


year_summ['terror'] = year_summ.text.str.count('terror')


# In[23]:


alt.Chart(year_summ[['year','terror']]).mark_line().encode(x='year:O', y='terror')


# In[24]:


import numpy as np
nrows, ncols = 100000, 100
rng = np.random.RandomState(43)
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows,ncols)) for i in range(4))


# In[25]:


get_ipython().magic(u'timeit df1 + df2 + df3 + df4')


# In[26]:


get_ipython().magic(u"timeit pd.eval('df1 + df2 + df3 + df4')")


# In[27]:


undf['text_len'] = undf.text.map(lambda x : len(x.split()))


# In[28]:


undf.head()


# In[29]:


undf.groupby('country', as_index=False)['text_len'].mean().head()


# In[30]:


alt.Chart(undf.groupby('country', as_index=False)['text_len'].mean()).mark_bar().encode(
alt.X('text_len', bin=True), y='count()')


# In[31]:


undf.groupby('country', as_index=False)['text_len'].mean().sort_values('text_len').head()


# In[32]:


undf.groupby('country', as_index=False)['text_len'].mean().sort_values('text_len').tail()


# <h1>8.1.2. Exploratory Questions</h1>

# <ol>
#     <li>How many speeches were given each year?</li>
#     <li>Make a bar graph of the number of speeches each year</li>
#     <li>Which country and what year has given the longest speech (by number of words)</li>
#     <li>Which country has spoken the most times?</li>
#     <li>Which country has spoken the least times?</li>
#     <li>Make a graph to illustrate the distribution of the number of times each country has spoken</li>
#     <li>What were the 25 most commonly used words in the 1970 session?</li>
#     <li>What were the 25 most commonly used words in the 2015 session?</li>
# </ol>
# 

# <h4>How many speeches were given each year?</h4>

# In[33]:


by_year


# <h2>Make a bar graph of the number of speeches each year</h2>

# In[34]:


alt.Chart(by_year).mark_bar().encode(x='year:N',y='text')


# <h2>Which country and what year has given the longest speech (by number of words)

# In[35]:


undf.sort_values('text_len', ascending=False).head()


# <h2>Which country has spoken the most times?</h2>

# In[36]:


undf.groupby('country').count().sort_values('text', ascending = False)


# <h2>Which country has spoken the least times?</h2>

# In[37]:


undf.groupby('country').count().sort_values('text')


# <h2>Make a graph to illustrate the distribution of the number of times each country has spoken</h2>

# In[38]:


alt.Chart(by_country,title='speech distribution').mark_bar().encode(x=alt.X('country'),y=('text'))


# <h1>8.2. Merging and Tidying Data</h1>

# In[39]:


c_codes = pd.read_csv('country_codes.csv', encoding='iso-8859-1')
c_codes.head()


# In[40]:


undf.head()


# In[41]:


undf.columns = ['session', 'year', 'code_3', 'text','text_len']
undf.head()


# In[42]:


undfe = undf.merge(c_codes[['code_3', 'country', 'continent', 'sub_region']])
undfe.head()


# In[43]:


undfe[undf.code_3 == 'EU ']


# In[44]:


undfe = undf.merge(c_codes[['code_3', 'country', 'continent', 'sub_region']], how='outer')
undfe.head()


# In[45]:


undfe[undfe.country.isna()].code_3.unique()


# In[46]:


undfe[undfe.text.isna()].code_3.unique()


# In[47]:


undfe[undfe.text.isna()].country.unique()


# In[48]:


undfe.loc[undfe.code_3 == 'EU', 'country'] = 'European Union'


# In[49]:


by_country = undfe.groupby('country',as_index=False)['text'].count()
by_country.loc[by_country.text.idxmin()]


# In[50]:


c_codes[c_codes.code_2 == 'EU']


# In[51]:


len(undfe)


# In[52]:


len(undf.code_3.unique())


# In[53]:


len(undfe.code_3.unique())


# In[54]:


set(undf.code_3.unique()) - set(undfe.code_3.unique())


# In[55]:


speeches_1970 = undf[undf.year == 1970].copy()
speeches_1970


# In[56]:


speeches_1970['text'] = speeches_1970.text.apply(lambda x: x.lower())
speeches_1970


# In[57]:


speeches_1970['text'] = speeches_1970.text.apply(lambda x: x.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))))


# In[58]:


speeches_1970['word_list'] = speeches_1970.text.apply(nltk.word_tokenize)


# In[59]:


from collections import Counter


# In[60]:


c = Counter(speeches_1970.word_list.sum())


# <h1>8.8.2. Using NLTK to score the speeches</h1>

# In[61]:


import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')


# In[62]:


from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def score_text(text, analyzer):
    sentence_list = tokenize.sent_tokenize(text)
    cscore = 0.0
    for sent in sentence_list:
        ss = analyzer.polarity_scores(sent)['compound']
        cscore += ss
    return cscore / len(sentence_list)


# In[63]:


undf['sentiment'] = undf.text.map(lambda t : score_text(t, analyzer))


# In[64]:


alt.data_transformers.enable('json')
alt.Chart(undf).mark_bar().encode(x=X('sentiment', bin=True), y='count()')


# In[66]:


undf.groupby('code_3', as_index=False)['text'].count()


# In[67]:


alt.Chart(undf).mark_bar().encode(x=X('code_3'), y='sentiment')


# In[ ]:


alt.Chart(undf).mark_bar().encode(x=X('year'), y='sentiment')


# In[ ]:


undf1 = undf.groupby('country', as_index=False).agg({'sentiment':'mean'})
undf1.nlargest(5,'sentiment')


# In[ ]:


undf1.columns = ['code_3, country']


# In[ ]:


alldf = pd.merge(c_codes[['country','code_3']], undf1, left_on='code_3',right_on='code_3')


# In[ ]:




