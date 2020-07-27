# add column named PEC per capita by dividing PEC [TWh] by population

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 101)


filename = '../Datensammlung.csv'
df = pd.read_csv(filename, index_col=[0,1])


# getting started
# Unit for PEC per capita is going to be kWh
# tera ~ 10^12, giga ~ 10^9, mega ~ 10^6, kilo ~ 10^3
df['PEC per capita [kWh]'] = df['PEC [TWh]'] / df ['Population'] * 10**9


# change order of columns for more convinience
col_names = ['Code', 'Continent', 'Population', 'GDP per capita [$]', 'PEC [TWh]',
        'PEC per capita [kWh]',
       'Oil', 'Coal', 'Gas', 'Hydropower', 'Nuclear', 'Solar', 'Wind',
       'Other renewables', 'Biofuels and Waste', 'Transport S', 'Industry S',
       'Residential S', 'Commercial and public services S',
       'Agriculture/Forestry S', 'Non-energy use S', 'Non-specified S']
df.columns = col_names


print(df.loc[('Afghanistan', range(1990,2010,1)),['Population','PEC [TWh]', 'PEC per capita [kWh]']].head())
print(df.columns)


# export as csv and excel
df.to_csv('Datensammlung-07-27-20.csv')
df.to_excel('Datensammlung-07-27-20.xlsx')
