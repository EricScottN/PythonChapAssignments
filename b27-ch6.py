#!/usr/bin/env python
# coding: utf-8

# <h1>6.2. World Factbook: Exploratory Data Analysis</h1>

# <h2>6.2.1. Loading data into a DataFrame from a CSV file</h2>

# In[1]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from altair import Chart, X, Y, Color, Scale
import altair as alt


# pwd

# In[2]:


wd = pd.read_csv('world_countries.csv')


# In[3]:


wd.head()


# In[4]:


c = Chart(wd) 
m = c.mark_bar()
e = m.encode(X('Birthrate',bin=True),y='count()')
e.display()


# In[5]:


Chart(wd).mark_bar().encode(x=X('Birthrate', bin=True), y='count()')


# In[6]:


Chart(wd).mark_bar().encode(x=X('Literacy', bin=True), y='count()')


# In[7]:


Chart(wd).mark_bar().encode(x=X('Service', bin=True), y='count()')


# In[8]:


Chart(wd).mark_point().encode(x='Population', y='Area', tooltip='Country')


# In[9]:


(wd.Population < 150000000).head(20)


# In[10]:


wd[wd.Population < 150000]


# In[11]:


Chart(wd[wd.Population < 150000]).mark_point().encode(x='Population', y='Area', tooltip='Country').interactive()


# In[12]:


wd[(wd.Population < 150000) & (wd.Area < 200000)]


# In[13]:


Chart(wd[(wd.Population < 150000) & (wd.Area < 200000)]).mark_point().encode(x='Population', y='Area', tooltip='Country').interactive()


# In[14]:


wd[wd.Country == 'Malta']


# In[15]:


wd[wd.Country == 'Malta ']


# In[16]:


wd.Country.str.strip()


# In[17]:


wd['Country'] = wd.Country.str.strip()


# In[18]:


wd[wd.Country == 'Malta']


# <h2>6.2.5.1. Power Tools – Scatter Matrix</h2>

# In[19]:


alt.Chart(wd).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='Region:N'
).properties(
    width=150,
    height=150
).repeat(
    row=['Birthrate', 'Deathrate', 'Infant mortality', 'GDP'],
    column=['Birthrate', 'Deathrate', 'Infant mortality', 'GDP']
).interactive()


# In[20]:


list(reversed(['a','b']))


# <h2>6.2.6. Developing Fluency</h2>

# <h3>6.2.6.1. Practice Questions</h3>

# 1. What are the top 10 countries with the largest GDP?

# In[21]:


wd.sort_values(by=['GDP'], ascending = False).head(5)


# <h2>6.3. Graphing Infant Mortality on a map</h2>

# In[22]:


import altair as alt
from vega_datasets import data
counties = alt.topo_feature(data.us_10m.url, 'counties')
unemp_data = data.unemployment.url


alt.Chart(counties).mark_geoshape().project(
    type='albersUsa').properties(
    width=500,
    height=300
)


# In[23]:


unemp_data = pd.read_csv('http://vega.github.io/vega-datasets/data/unemployment.tsv',sep='\t')
unemp_data.head()


# In[24]:


alt.Chart(counties).mark_geoshape(
).encode(
    color='rate:Q'
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(unemp_data, 'id', ['rate'])
).project(
    type='albersUsa'
).properties(
    width=500,
    height=300,
    title='Unemployment by County'
)


# <h3>6.3.1. Using a Web API to get Country Codes</h3>

# In[25]:


import requests
res = requests.get('https://restcountries.eu/rest/v2/alpha/usa')
res.status_code


# In[26]:


res.text


# In[27]:


usa_info = res.json()
usa_info


# In[28]:


res = requests.get('https://restcountries.eu/rest/v2/alpha/per')


# In[29]:


peru_info = res.json()
peru_info


# In[30]:


len(peru_info)


# In[31]:


def get_num_code(country_code):
    address = 'https://restcountries.eu/rest/v2/alpha/'
    result = requests.get(address + country_code)
    country_info = result.json()
    return int(country_info['numericCode'])
    
wd['CodeNum'] = wd.Code.map(get_num_code)
wd.head()


# In[32]:


countries = alt.topo_feature(data.world_110m.url, 'countries')

alt.Chart(countries).mark_geoshape(
    fill='#666666',
    stroke='white'
).properties(
    width=750,
    height=450
).project('equirectangular')


# In[33]:


base = alt.Chart(countries).mark_geoshape(
    fill='#666666',
    stroke='white'
).encode( #your code here
    color='Infant mortality:Q'
).transform_lookup( # your code here
    lookup='id',
    from_=alt.LookupData(wd, 'CodeNum', ['Infant mortality'])
).properties(
    width=750,
    height=450
).project('equirectangular')

base


# <h1>6.4. Challenge: Screen Scraping the CIA</h1>

# In[34]:


import os
files = os.listdir('factbook/fields')
print(sorted(files)[:10])


# In[35]:


pwd


# In[36]:


from bs4 import BeautifulSoup
page = open('factbook/docs/notesanddefs.html',encoding="utf-8").read()
page[:200]


# In[37]:


page = BeautifulSoup(page)
print(page.prettify()[:1000])


# In[38]:


links = page.select('a')
print(len(links))
links[-1]


# In[39]:


divs = page.select('div')
print(len(divs))
divs[-1]


# In[40]:


cols = page.select("span.category")
for col in cols:
    cells = col.select('td')
    col_name = cells[0].text
    print(col_name)


# In[41]:


cols = page.select("span.category")
for col in cols:
    cells = col.select('td')
    colname = cells[0].text
    links = cells[1].select('a')
    if len(links) > 0:
        fpath = links[0]['href']
        print(colname, fpath)


# <h1>6.4.2. Loading all the data in rough form</h1>

# In[42]:


page = BeautifulSoup(open('factbook/fields/2001.html').read())


# In[43]:


page_list = [
    'Country – name',
    'Code2',
    'Code3',
    'CodeNum',
    'Population',
    'Area',
    'Coastline',
    'Climate',
    'Net migration',
    'Birth rate',
    'Death rate',
    'Infant mortality rate',
    'Literacy',
    'GDP',
    'Government type',
    'Inflation rate',
    'Health expenditures',
    'GDP - composition, by sector of origin',
    'Land use',
    'Internet users',
]


# In[44]:


file_list=[]
for col in cols:
    for field in page_list:
        cells = col.select('td')
        colname = cells[0].text
        links=cells[1].select('a')
        if len(links) > 0:
            fpath = links[0]['href'].split('/')[2].split("#")[0]
            #print(colname, fpath)
            if colname == field:
                file_list.append(fpath)
file_list


# In[47]:


all_data={}
for file in file_list:
    page = open('factbook/fields/' + file).read()
    page = BeautifulSoup(page)
    
    rows=page.select('tr')
    len_rows=len(rows)
    fieldn=rows[0].select('th')[1].text
    val={}
    for i in range(1, len_rows):
        val[rows[i]['id']]=rows[i].select('td')[1].text.strip().split("\n")
    all_data[fieldn]=val
#print(all_data)
df=pd.DataFrame(all_data)
df.head()


# <h1>6.4.3. Cleaning the data</h1>

# In[49]:


infant_mortality_df = pd.DataFrame({'Infant Mortality':df['INFANT MORTALITY RATE(DEATHS/1,000 LIVE BIRTHS)']})
infant_mortality_df.head()


# In[50]:


df1 = infant_mortality_df[infant_mortality_df['Infant Mortality'].apply(type)!=float]
df1


# In[51]:


df2=df1['Infant Mortality'].map(lambda x: x[0]).map(lambda x: (x.split()[1]))
df2[df2.map(len)==2]


# In[52]:


pd.to_numeric(df2[df2!='NA']).mean()


# ## 6.4.4. Saving the data

# In[53]:


df.to_csv(index=False)


# <h1>6.5. Comparing forms of Government</h1>

# In[54]:


wd.pivot_table(index='Region', columns='Climate', values='Agriculture')


# In[ ]:




