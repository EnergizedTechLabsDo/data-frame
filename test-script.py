#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
filename='Datensammlung.xlsx'
path_dir=r"C:\Users\Marina\Desktop\energized"
path_file=path_dir +'\\'+ filename
df = pd.read_excel(path_file)
df.info()
df.head()
df.describe()

#hier gibts ne veränderung

#hier die zweite änderung 


df = df[['Entity','Year', 'Population', 'GDP in $','Primary Energy Consumption (terrawatt-hours)']]


# In[16]:


df = df.rename(index= str, columns={'Entity':'Country', 'Year':'Year', 'Population':'Population','GDP in $':'GDP','Primary Energy Consumption (terrawatt-hours)':'PEV' })
df = df.set_index(['Year','Country']).sort_index()#Beispiele für slicing: 1. Gesamter DataFrame bis Zeile 100, 2. bestimmtes Jahr 3. bestimmtes Land
print(df[:100])
print(df.loc[2010])
print(df.xs((slice(None), 'Germany')))
df.plot(x='Population', y='PEV', kind='scatter')
df.plot(x='GDP', y='PEV', kind='scatter')
plt.show()


# In[ ]: