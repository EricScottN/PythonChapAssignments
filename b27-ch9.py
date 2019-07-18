#!/usr/bin/env python
# coding: utf-8

# <h1>Sec 9.3</h1>

# In[1]:


get_ipython().magic(u'load_ext sql')


# In[2]:


get_ipython().magic(u'sql sqlite:///bikeshare.db')


# <h1>Sec 9.3.1</h2>

# In[3]:


get_ipython().run_cell_magic(u'sql', u'', u'SELECT\n  *\nFROM\n  trip_data\nLIMIT\n  10')


# In[4]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nLIMIT\n  10')


# In[5]:


get_ipython().magic(u'sql select name, sql from sqlite_master')


# In[6]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nWHERE\n  duration >= 3600\nLIMIT\n  10')


# In[7]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nWHERE\n  duration >= 3600\nAND\n  member_type = "Member"\nLIMIT\n  10')


# In[8]:


get_ipython().run_cell_magic(u'sql', u'', u"\nSELECT\n    bike_number, start_date, duration\nFROM\n    trip_data\nWHERE\n    duration < 900\nAND\n    bike_number = 'W01274'\nLIMIT\n    10")


# In[9]:


get_ipython().run_cell_magic(u'sql', u'', u"\nSELECT\n    bike_number, end_station, duration\nFROM\n    trip_data\nWHERE\n    duration > 28800\nAND\n    start_station = '31111'")


# In[10]:


get_ipython().run_cell_magic(u'sql', u'', u"\nSELECT\n    bike_number, end_station, duration\nFROM\n    trip_data\nWHERE\n    duration > 28800\nAND\n    start_station = '31111'\nAND\n    end_station = '31111'")


# <h1>9.5. Sorting</h1>

# In[11]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nORDER BY\n  duration\nLIMIT\n  10')


# In[12]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nORDER BY\n  duration DESC\nLIMIT\n  10')


# In[13]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, start_date, duration\nFROM\n  trip_data\nWHERE\n  member_type = "Casual"\nORDER BY\n  duration\nLIMIT\n  10')


# In[14]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  start_station, end_station, duration, bike_number\nFROM\n  trip_data\nWHERE\n  duration >= 3600\nORDER BY\n  duration DESC\nLIMIT\n  40')


# <h1>9.6. Aggregation or Group By</h1>

# In[15]:


get_ipython().run_cell_magic(u'sql', u'', u'SELECT\n  member_type, COUNT(*)\nFROM\n  trip_data\nGROUP BY\n  member_type\nORDER BY\n  COUNT(*) DESC\nLIMIT\n  10')


# In[16]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  duration, count(*)\nFROM\n  trip_data\nGROUP BY\n  member_type\nORDER BY\n  COUNT(*) DESC')


# In[17]:


get_ipython().run_cell_magic(u'sql', u'', u"\nSELECT\n  member_type, start_station, count(*)\nFROM\n  trip_data\nWHERE\n  member_type = 'Casual'\nGROUP BY\n  member_type, start_station\nORDER BY\n  COUNT(*) DESC\nLIMIT\n  20")


# In[18]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, SUM(duration)\nFROM\n  trip_data\nGROUP BY\n  member_type\nLIMIT\n  10')


# In[19]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  start_station, AVG(duration)\nFROM\n  trip_data\nGROUP BY\n    start_station\nORDER BY\n    AVG(duration) DESC\nLIMIT\n  10')


# In[20]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  bike_number, COUNT(bike_number)\nFROM\n  trip_data\nGROUP BY\n  bike_number\nORDER BY\n  COUNT(bike_number) DESC\nLIMIT\n  10')


# In[21]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  member_type, COUNT(member_type)\nFROM\n  trip_data\nGROUP BY\n  member_type\nORDER BY\n  COUNT(member_type) DESC')


# In[22]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  start_station, end_station, COUNT(*)\nFROM\n  trip_data\nWHERE\n  start_station = end_station\nGROUP BY\n  start_station\nORDER BY\n  COUNT(*) DESC')


# In[23]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  *\nFROM\n  bikeshare_stations\nLIMIT\n  10')


# In[24]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  *\nFROM\n  trip_data, bikeshare_stations\n\nLIMIT\n  10')


# In[25]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  *\nFROM\n  trip_data, bikeshare_stations\nWHERE\n  start_station = station_id\nLIMIT\n  10')


# In[26]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  COUNT(*)\nFROM\n  trip_data, bikeshare_stations\nWHERE\n  start_station = station_id')


# In[27]:


get_ipython().run_cell_magic(u'sql', u'', u'\nSELECT\n  COUNT(*)\nFROM\n  trip_data JOIN bikeshare_stations ON start_station = station_id')


# In[28]:


get_ipython().run_cell_magic(u'sql', u'', u"\nSELECT\n  station_id, COUNT(*) AS trip_count\nFROM\n  trip_data join bikeshare_stations\nON\n  start_station = station_id\nWHERE\n  duration >= 3600\n  AND status = 'open'\nGROUP BY\n  station_id\nORDER BY\n  trip_count DESC\nLIMIT\n  10")


# In[29]:


get_ipython().run_cell_magic(u'sql', u'', u"SELECT \n  station_id, AVG(duration) AS avg_duration\nFROM\n  trip_data join bikeshare_stations\nON\n  start_station = station_id\nWHERE\n  member_type = 'Member'\n  AND start_station = end_station\nGROUP BY\n  station_id\nORDER BY \n  station_id DESC")


# In[30]:


get_ipython().run_cell_magic(u'sql', u'', u'SELECT \n  station_id, name, COUNT(station_id)\nFROM\n  trip_data join bikeshare_stations\nON\n  start_station = station_id\nGROUP BY\n  station_id\nORDER BY \n  COUNT(station_id) DESC')


# In[31]:


get_ipython().run_cell_magic(u'sql', u'', u'SELECT \n  station_id, name, COUNT(station_id)\nFROM\n  trip_data join bikeshare_stations\nON\n  start_station = station_id\nGROUP BY\n  station_id\nORDER BY \n  COUNT(station_id) DESC')


# In[32]:


get_ipython().run_cell_magic(u'sql', u'', u'SELECT \n  station_id, start_station, name, COUNT(end_station) AS end_station_count\nFROM\n  trip_data join bikeshare_stations\nON\n  end_station = station_id\nWHERE\n  start_station = 31200\nGROUP BY\n  end_station\nORDER BY \n  COUNT(station_id) DESC')


# <h1>9.8. Getting SQL Data into a DataFrame</h1>

# In[1]:


import pandas as pd
stations = pd.read_sql_query("""select * from bikeshare_stations where latitude is not NULL""",'sqlite:///bikeshare.db')
stations.head()


# In[54]:


trips = pd.read_sql_query("""select * from trip_data order by start_date limit 10""",
                          'sqlite:///bikeshare.db', parse_dates = ['start_date','end_date'])


# In[55]:


trips


# In[58]:


trips['calc_duration'] = trips['end_date'] - trips['start_date']


# In[59]:


trips


# In[60]:


trips.dtypes


# In[69]:


import folium
locations = list(zip(stations.latitude, stations.longitude))
dc_center = (38.9072, -77.0369)
fig = folium.Map(location = dc_center,
                zoom_start = 12)
folium.Marker(
    location = locations
).add_to(fig)
fig


# In[1]:


def compute_y(x,m,b):
    return m*x+b
def compute_all_y(list_of_x,m,b):
    y_p = []
    for x in list_of_x:
        y_p.append(compute_y(x,m,b))
    return y_p
def compute_mse(list_of_known, list_of_predictions):
    s=0
    n=len(list_of_known)
    for i in range(n):
        s += (list_of_known[i]-list_of_predictions[i])**2
    mse=s/n
    return mse

diameter = [6,8,10,14,18]
price = [7,9,13,17.5,18]

def linear_fit(x,y):
    init_slope = 0
    init_intercept=0
    step=0.01
    init_mse=compute_mse(y,compute_all_y(x, init_slope, init_intercept))
    for i in range(1000):
        if init_mse > compute_mse(y,compute_all_y(x,init_slope+step, init_intercept)):
            new_slope = init_slope+step
        else:
            new_slope = init_slope-step
        if init_mse > compute_mse(y,compute_all_y(x,new_slope, init_intercept+step)):
            new_intercept = init_intercept+step
        else:
            new_intercept = init_intercept-step
        new_mse = compute_mse(y,compute_all_y(x,new_slope,new_intercept))
        init_slope = new_slope
        init_intercept = new_intercept
    return print("slope = ", new_slope, "intercept = ", new_intercept)


# In[ ]:




