import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import slug

from geonamescache import GeonamesCache
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap

#
#filename = 'data-frame/api_ag.lnd.frst.zs_ds2_en_csv_v2_1217516.csv'
#shapefile = 'shp/countries/ne_10m_admin_0_countries_lakes'
#num_colors = 9
#year = '2016'
#cols = ['Country Name', 'Country Code', year]
#title = 'Primary Energy Consumption per Capita {}'.format(year)
#
##wofür benötigt??
##imgfile = 'img/{}.png'.format(slug(title))
#
#description = '''
#Primärenergieverbrauch setzt sich zusammen aus ... '''.strip()
#
#
#
## CHOROPLETH MAP !!! #
#fig = plt.figure(figsize=(7,4))
map = Basemap()
map.drawmapboundary(fill_color='aqua')
#
#
map.fillcontinents(color='g',lake_color='aqua')
map.drawcountries(color='k')
#map.drawlsmask(land_color='0.3')
map.drawcoastlines()



plt.show()
##plt.savefig('test.png')
#
#
#
print('done')
#
