#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = ''


# In[2]:


# First, import the relevant modules
import requests
from statistics import median


# In[3]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
r = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?rows=1&api_key='+API_KEY)


# In[4]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
r.json()


# In[5]:


# 1. Get data for the year 2017
R_2017 = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?start_date=2017-01-01&end_date=2017-12-31&api_key='+API_KEY)


# In[6]:


#2. converting JSON to dict
json_2017 = R_2017.json()
type(json_2017)


# In[7]:


#3
# Highest opening price
opening_high = [json_2017['dataset_data']['data'][i][1] for i in range(len(json_2017['dataset_data']['data']))]
opening_high = list(filter(None,opening_high)) # Removing None (null) values
max(opening_high)


# In[8]:


# Lowest opening price
opening_low = [json_2017['dataset_data']['data'][i][1] for i in range(len(json_2017['dataset_data']['data']))]
opening_low = list(filter(None,opening_low)) # Removing None (null) values
min(opening_low)


# In[9]:


#4
# Largest change in a single day
opening_highs = [json_2017['dataset_data']['data'][i][2] for i in range(len(json_2017['dataset_data']['data']))]
opening_lows = [json_2017['dataset_data']['data'][i][3] for i in range(len(json_2017['dataset_data']['data']))]
diff_list = [h-l for (h,l) in zip(opening_highs,opening_lows)]
round(max(diff_list),2)


# In[10]:


#5
# Largest closing price
largest_close = [json_2017['dataset_data']['data'][i][4] for i in range(len(json_2017['dataset_data']['data']))]
max(largest_close)


# In[11]:


#6
# Avg volume traded
avg_trade_volume = [json_2017['dataset_data']['data'][i][6] for i in range(len(json_2017['dataset_data']['data']))]
round(sum(avg_trade_volume)/len(avg_trade_volume),2)


# In[12]:


#7
# Median volume traded
med_trade_volume = [json_2017['dataset_data']['data'][i][6] for i in range(len(json_2017['dataset_data']['data']))]
median(med_trade_volume)


# In[ ]:




