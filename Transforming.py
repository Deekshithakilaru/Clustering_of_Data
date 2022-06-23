#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
import pandas as pd
# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

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


TorontoData  = pd.read_csv('task2.csv')
TorontoData .head()


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


print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(TorontoData ['Borough'].unique()),
        TorontoData .shape[0]
    )
)


# In[ ]:


toronto_map = folium.Map(location=[43.65, -79.4], zoom_start=10)

X = TorontoData['Latitude']
Y = TorontoData['Longitude']
Z = np.stack((X, Y), axis=1)

kmeans = KMeans(n_clusters=4, random_state=0).fit(Z)

clusters = kmeans.labels_
colors = ['red', 'green', 'blue', 'yellow']
TorontoData['Cluster'] = clusters

for latitude, longitude, borough, cluster in zip(TorontoData['Latitude'], TorontoData['Longitude'], TorontoData['Borough'], TorontoData['Cluster']):
    label = folium.Popup(borough, parse_html=True)
    folium.CircleMarker(
        [latitude, longitude],
        radius=4,
        popup=label,
        color='black',
        fill=True,
        fill_color=colors[cluster],
        fill_opacity=0.7).add_to(toronto_map)  

toronto_map

