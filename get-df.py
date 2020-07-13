#!/usr/bin/env python
# coding: utf-8

#demo
#demo brunch

import pandas as pd
import matplotlib.pyplot as plt


url="https://raw.githubusercontent.com/EnergizedTechLabsDo/data-frame/master/Datensammlung.csv"
df = pd.read_csv(url)

print(df.shape)

#print(df.info())
#print(df.head())
#print(df.describe())

df = df[['Entity','Year', 'Population', 'GDP per capita [$]','PEC [TWh]','Oil','Coal','Gas','Hydropower','Nuclear','Solar','Wind','Other renewables','Biofuels and Waste','Transport S','Industry S','Residential S','Commercial and public services S','Agriculture/Forestry S','Non-energy use S','Non-specified S']]

df = df.rename(index= str, columns={'Entity':'Country', 'Year':'Year', 'Population':'Population','GDP per capita [$]':'GDP','PEC [TWh]':'PEV'})#,'Oil':'Oil','Coal':'Coal','Gas':'Gas','Hydropower':'Hydropower','Nuclear':'Nuclear'})

df = df.set_index(['Year','Country']).sort_index()#Beispiele für slicing: 1. Gesamter DataFrame bis Zeile 100, 2. bestimmtes Jahr 3. bestimmtes Land
print(df[:100])
#print(df.loc[2010])
#print(df.loc[1970])
#print(df.loc[[1970], ['Transport S', 'Gas', 'PEV']])
#print(df.xs((slice(None), 'Germany')))


#df.plot(x='Population', y='PEV', kind='scatter')
#df.plot(x='GDP', y='PEV', kind='scatter')
#plt.show()
