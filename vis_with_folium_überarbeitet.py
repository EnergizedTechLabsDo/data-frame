#!/usr/bin/env python
# coding: utf-8

# In[1]:


#youtube video zu folium: https://www.youtube.com/watch?v=t9Ed5QyO7qY
#dazugehöriger code: https://github.com/groundhogday321/python-folium
#geojson.io: Bearbeitung einer geojson Datei hier möglich sowie Erstellung eigener Datei
#weitere nützliche Infos zu choropleth: https://towardsdatascience.com/choropleth-maps-with-folium-1a5b8bcdd392

import folium
import numpy as np
import pandas as pd

import json
import requests


# In[2]:


#Infos zu folium.Map
#folium.Map?
#folium help
#folium.Choropleth?


# In[3]:


#eine ausgangsmap die anzeigen lassen
#m = folium.Map()
#m


# In[25]:


#map speichern
#map2 = folium.Map(location=[39.739192, -104.990337], zoom_start=8)

# put in path.html
#map2.save('/Users/Marina/Desktop/map2.html')


# In[36]:


#Choropleth

#json mit angepassten ländern aus url nehmen
#json_url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/folium_vis/map_bearbeitet.geojson"
#neue json
json_url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/folium_vis/map.geojson"
data_url="https://github.com/EnergizedTechLabsDo/data-frame/raw/master/Datensammlung.xlsx"
df = pd.read_excel(data_url)


# In[293]:





# In[15]:


df.head()


# In[16]:





# In[ ]:





# In[5]:


#gewünschtes jahr festhalten
hist_year=2013


# In[6]:


#maske mit dem gewünschten jahr erstellen
mask = df["Year"].isin([hist_year])


# In[7]:


#nur noch daten aus ausgewählten Jahr
df=df[mask]


# In[23]:


df.head()


# In[8]:


#Creating a data frame with just the country codes and the values we want plotted.
data_to_plot =df[['Code','Population']]


# In[9]:


data_to_plot.head()


# In[10]:


m = folium.Map()


# In[37]:


geo_json_data = json.loads(requests.get(json_url).text)

#herntergeladene json auf map anwenden, für Ländergrenzen
folium.GeoJson(geo_json_data).add_to(m)


# In[38]:


m


# In[15]:


#map mit folium.map aufrufen
m = folium.Map()

#hier ist die Struktur einer Funktion, die auf die map angewendet wird
#in der geojson sind die ländergrenzen als koordinaten hinterlegt und
#diese wird jetzt auf die folium.map draufgelegt
#weiter unten sind zwei beispiele
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


# In[17]:


m = folium.Map()

# Beipsielbearbeitung der map
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


# In[18]:


m


# In[46]:


#funktion für color scale bezogen auf population
#hat aber nicht funktionert weil untere Zeilen nicht liefen

#from branca.colormap import linear

#colormap = linear.YlGn_09.scale(
#    data_to_plot.Population.min(),
#    data_to_plot.Population.max())

#print(colormap(5.0))

#colormap


# In[ ]:





# In[58]:


#data in ein dict überführen
#data_to_plot_dict = data_to_plot.set_index('Code')['Population']
#data_to_plot_dict['AFG']

#data_sort_dict = data_sort.set_index('Code')['Population']
#data_sort_dict['AFG']


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


# In[ ]:





# In[234]:





# In[ ]:





# In[35]:


#versuch mit choropleth zeigt alle länder die in geojson vorhanden
#choropleth ist eine alternativ möglichkeit zur dem Versuch hierdrüber
m = folium.Map()

folium.Choropleth(
    geo_data=geo_json_data,
    fill_opacity=0.3,
    line_weight=2,
).add_to(m)

m


# In[ ]:





# In[29]:


#über den Ländercode werden unsere Daten mit den Daten der
#geojson zusammengeschlossen - in der geojson ist ein feature der
#ländercode
m = folium.Map()

folium.Choropleth(
    geo_data=geo_json_data,
    data=data_to_plot,
    columns=['Code', 'Population'],
    key_on='feature.id',
).add_to(m)

#m


# In[39]:


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


# In[31]:


#Creating a data frame with just the country codes and the values we want plotted.
data_gdp =df[['Code','GDP per capita [$]']]


# In[40]:


#Vis des gdp
#data_gdp.head(5)


# In[41]:


#über den Ländercode werden unsere Daten mit den Daten der
#geojson zusammengeschlossen - in der geojson ist ein feature der
#ländercode
#m = folium.Map()

#folium.Choropleth(
 #   geo_data=geo_json_data,
 #   data=data_gdp,
 #   columns=['Code', 'GDP per capita [$]'],
 #   key_on='feature.id',
#).add_to(m)

#m


# In[42]:


m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_gdp,
    columns=['Code','GDP per capita [$]'],
    key_on='feature.id',
    #fill_color='YlGn',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_gdp['GDP per capita [$]'].quantile([0,0.2,0.4,0.6,0.8,1])),
    reset=True
).add_to(m)

m


# In[45]:


#vis von oil
#Creating a data frame with just the country codes and the values we want plotted.
data_oil =df[['Code','Oil']]
m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_oil,
    columns=['Code','Oil'],
    key_on='feature.id',
    #fill_color='YlGn',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_oil['Oil'].quantile([0,0.2,0.4,0.6,0.8,1])),
    reset=True
).add_to(m)

m


# In[46]:


#vis von PEC [TWh]
#Creating a data frame with just the country codes and the values we want plotted.
data_pec =df[['Code','PEC [TWh]']]
m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_pec,
    columns=['Code','PEC [TWh]'],
    key_on='feature.id',
    #fill_color='YlGn',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_pec['PEC [TWh]'].quantile([0,0.2,0.4,0.6,0.8,1])),
    reset=True
).add_to(m)

m


# In[48]:


#vis von PEC [TWh]
#Creating a data frame with just the country codes and the values we want plotted.
data_coal =df[['Code','Coal']]
m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_coal,
    columns=['Code','Coal'],
    key_on='feature.id',
    fill_color='YlGn',
    #fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_coal['Coal'].quantile([0,0.2,0.4,0.6,0.8,1])),
    reset=True
).add_to(m)

m


# In[ ]:





# In[56]:


#vis von PEC [TWh]
#Creating a data frame with just the country codes and the values we want plotted.
data_hy =df[['Code','Hydropower']]
m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_hy,
    columns=['Code','Hydropower'],
    key_on='feature.id',
    fill_color='YlGn',
    #fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[3, 4, 9, 11],
    bins = list(data_hy['Hydropower'].quantile([0,0.2,0.4,0.6,0.8,1])),
    reset=True
).add_to(m)

m


# In[ ]:
