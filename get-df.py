#!/usr/bin/env python
# coding: utf-8

#demobrunch
#demobrunch2

import pandas as pd
import matplotlib.pyplot as plt


url="https://github.com/EnergizedTechLabsDo/data-frame/raw/master/Datensammlung.xlsx"
df = pd.read_excel(url)

print(df.shape)

print(df.info())
print(df.head())
print(df.describe())

df = df[['Entity','Year', 'Population', 'GDP in $','Primary Energy Consumption (terrawatt-hours)']]


df = df.rename(index= str, columns={'Entity':'Country', 'Year':'Year', 'Population':'Population','GDP in $':'GDP','Primary Energy Consumption (terrawatt-hours)':'PEV' })
df = df.set_index(['Year','Country']).sort_index()#Beispiele für slicing: 1. Gesamter DataFrame bis Zeile 100, 2. bestimmtes Jahr 3. bestimmtes Land
print(df[:100])
print(df.loc[2010])
print(df.xs((slice(None), 'Germany')))


df.plot(x='Population', y='PEV', kind='scatter')
df.plot(x='GDP', y='PEV', kind='scatter')
plt.show()
