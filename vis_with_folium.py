#!/usr/bin/env python
# coding: utf-8

# In[5]:


#youtube zu folium: https://www.youtube.com/watch?v=t9Ed5QyO7qY
#dazugehöriger code: https://github.com/groundhogday321/python-folium
#andere Seite mit instructions https://www.kdnuggets.com/2018/09/visualising-geospatial-data-python-folium.html

import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd
from vega_datasets import data as vds

#url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/master/Datensammlung.csv"
#df = pd.read_csv(url, index_col = [0,1])

# In[18]:

#get_ipython().run_line_magic('pinfo', 'folium.Map')

# In[2]:

#die ausgangsmap die anzeigen lassen
m = folium.Map()
m
# In[ ]:

# In[25]:

#save map
#map2 = folium.Map(location=[39.739192, -104.990337], zoom_start=8)

# put in path.html
#map2.save('/Users/Marina/Desktop/map2.html')


# In[46]:


#folium help
#folium.Choropleth?


# In[188]:


#Choropleth
#json aus Internet
#json_url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/folium_vis/map.geojson"

#json aus github
#json_url="https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
#json_url="https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"

#json mit angepassten ländern aus url nehmen
json_url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/folium_vis/map_bearbeitet.geojson"
data_url="https://github.com/EnergizedTechLabsDo/data-frame/raw/master/Datensammlung.xlsx"
#pop_df = pd.read_excel(data_url, index_col = [0,1])
df = pd.read_excel(data_url)


# In[293]:


#test doppelindex
#df.loc[('Germany', 2005),'PEC [TWh]']


# In[78]:


df.head()


# In[111]:


#nur contintent und pop auswählen z.b.
data_to_plot=df[["Continent","Population"]]


# In[80]:


data_to_plot.head()


# In[112]:


#ausgewähltes jahr festhalten
hist_year=2013


# In[113]:


#maske mit dem ausgewählen jahr erstellen
mask = pop_df["Year"].isin([hist_year])


# In[114]:


#nur noch daten aus ausgewählten Jahr
df=df[mask]


# In[87]:


df.head()


# In[115]:


#Creating a data frame with just the country codes and the values we want plotted.
data_to_plot =df[['Code','Population']]


# In[116]:


data_to_plot.head()


# In[39]:


#hist_indicator="Population"


# In[40]:


#map = folium.Map(location=[100, 0], zoom_start=1.5)


# In[ ]:





# In[189]:


m = folium.Map()

geo_data=json_url


# In[190]:


import json
import requests
geo_json_data = json.loads(requests.get(geo_data).text)
#herntergeladene json auf map anwenden, für Ländergrenzen
folium.GeoJson(geo_json_data).add_to(m)


# In[191]:


m


# In[182]:


#map mit folium.map aufrufen
m = folium.Map()

folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'fillColor': '#ffff00',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'
    }
).add_to(m)

m


# In[215]:


m = folium.Map()

#alle länder mit einem "E" im Namen grün markieren
folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'fillColor': 'green' if 'e' in feature['properties']['name'].lower() else '#ffff00',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'
    }
).add_to(m)


# In[216]:


m


# In[202]:


#funktion für color scale bezohen auf pop(hat aber nicht funktionert weil untere Zeilen nicht liefen)

from branca.colormap import linear

colormap = linear.YlGn_09.scale(
    data_to_plot.Population.min(),
    data_to_plot.Population.max())

print(colormap(5.0))

colormap


# In[ ]:





# In[243]:


#data in ein dict überführen
data_to_plot_dict = data_to_plot.set_index('Code')['Population']
#data_to_plot_dict['AFG']

data_sort_dict = data_sort.set_index('Code')['Population']
data_sort_dict['AFG']


# In[292]:


#das hat nicht geklappt
#m = folium.Map([43, -100], zoom_start=4)

#folium.GeoJson(
    #geo_json_data,
    #name='data_sort',
    #style_function=lambda feature: {
        #'fillColor': colormap(data_sort_dict[feature['id']]),
        #'color': 'black',
        #'weight': 1,
        #'dashArray': '5, 5',
        #'fillOpacity': 0.9,
    #}
#).add_to(m)

#folium.LayerControl().add_to(m)

#m


# In[247]:


#color_sort_dict = {key: colormap(data_sort_dict[key]) for key in data_sort_dict.keys()}


# In[249]:


data_sort.head(5)
data_sort.keys()


# In[234]:


data_sort=data_to_plot.sort_values("Code")


# In[ ]:





# In[253]:


#versuch mit choropleth zeigt alle länder die in geojson vorhanden
m = folium.Map([43, -100], zoom_start=4)

folium.Choropleth(
    geo_data=geo_json_data,
    fill_opacity=0.3,
    line_weight=2,
).add_to(m)

m


# In[ ]:





# In[262]:


m = folium.Map()

folium.Choropleth(
    geo_data=geo_json_data,
    data=data_to_plot,
    columns=['Code', 'Population'],
    key_on='feature.id',
).add_to(m)

#m


# In[291]:


m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_to_plot,
    columns=['Code', 'Population'],
    key_on='feature.id',
    #fill_color='YlGn',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_to_plot['Population'].quantile([0,0.2,0.3,0.4, 0.5,0.75,0.8,0.9,0.95, 1])),
    reset=True
).add_to(m)

m


# In[ ]:





# In[ ]:
