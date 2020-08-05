import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Data import
df = pd.read_excel('Data_test.xlsx')

#Data overview
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.shape)


# Plot
df_chn = df[(df['Entity']=='China')]
df_ger = df[(df['Entity']=='Germany')]

print(df_chn.head())

plt.scatter(df_chn['Year'], df_chn['Co2e'])
sns.pairplot(df_chn.iloc [:,2:])
plt.scatter(df_chn['Coal consumption per capita'],df_chn['Co2e'])

# Plots Anstieg GDP, Co2, PEV, Coal cons im Vergleich
plt.subplot(4,1,1)
plt.plot(df_chn['Year'],df_chn['Coal consumption per capita'])
plt.ylabel('Coal consumption per capita')
plt.xlabel('Year')
plt.title('Coal consumption per capita')

plt.subplot(4,1,2)
plt.plot(df_chn['Year'],df_chn['Energy use per capita'])
plt.ylabel('Energy use per capita')
plt.xlabel('Year')
plt.title('Energy use per capita')

plt.subplot(4,1,3)
plt.plot(df_chn['Year'],df_chn['GDP'])
plt.ylabel('GDP')
plt.xlabel('Year')
plt.title('GDP')

plt.subplot(4,1,4)
plt.plot(df_chn['Year'],df_chn['Co2e'])
plt.ylabel('Co2e')
plt.xlabel('Year')
plt.title('Co2e')



plt.show()
