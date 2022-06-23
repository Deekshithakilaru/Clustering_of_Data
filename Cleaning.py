#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv('q1.csv')
df.head()


# In[ ]:


pip install geocoder


# In[ ]:


import geocoder


# In[ ]:


def get_latlng(postal_code):
    # initialize your variable to None
    lat_lng_coords = None
    # loop until you get the coordinates
    while(lat_lng_coords is None):
        g = geocoder.arcgis('{}, Toronto, Ontario'.format(postal_code))
        lat_lng_coords = g.latlng
    return lat_lng_coords


# In[ ]:


postal_codes = df['Postcode']    
coords = [ get_latlng(postal_code) for postal_code in postal_codes.tolist() ]


# In[ ]:


df_coords = pd.DataFrame(coords, columns=['Latitude', 'Longitude'])
df['Latitude'] = df_coords['Latitude']
df['Longitude'] = df_coords['Longitude']
df.head()


# In[ ]:


df.drop('Unnamed: 0',axis=1,inplace=True)
df.head()


# In[ ]:


df.to_csv('task2.csv', index=False)

