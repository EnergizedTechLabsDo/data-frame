#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

url="https://github.com/EnergizedTechLabsDo/data-frame/raw/import-data/Datensammlung.csv"
df = pd.read_csv(url, index_col = [0,1])



'''Beispiel für Slicing mit Doppelindizes: Für den Doppelindex wird ein Tupel mit ('Land', Jahr) angegeben.'''
print(df.loc[('Germany', 2005),'PEC [TWh]'])
print(df.columns)

print(df.isnull().sum())
print(df.head(-100))

df_filled = df.fillna(df.mean())
print(df.isnull().sum())

print(df_filled['PEC [TWh]'].head())

# sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
# plt.show()
#
# sns.boxplot(x="Year", y="GDP per capita [$]", data=df_small, palette="summer")
# plt.show()
#
# sns.distplot(df["GDP per capita [$]"].dropna(), color="purple", bins=30)
# plt.show()


#df_small[["Population", "GDP per capita [$]", "Year"]] = df_small[["Population", "GDP per capita [$]"]].replace(0, nan)
# imputation of NaN
# df_values = df_small.values
# sim_imp = SimpleImputer(missing_values=nan, strategy="constant")
# sim_imp = sim_imp.fit(df_values[1:, 1:])
# df_values[1:, 1:] = sim_imp.transform(df_values[1:, 1:])
# print(df_values)
