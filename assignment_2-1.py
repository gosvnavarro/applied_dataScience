import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')

#---

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
print(df.head())

# pegar o ano de 2015
df_2015 = df.where(df['Date'].str.contains('2015')).dropna()
df_2015['Date'] = df_2015.Date.str[5:]
print(df_2015.head())

df['Date'] = df.Date.str[5:]
print(df.head())

# remover bissexto 
df = df.where(df['Date'] != '02-29')

# pegar temperaturas maximas e minimas
high = df.groupby('Date')['Data_Value'].max()
print(high.head())

low = df.groupby('Date')['Data_Value'].min()
print(low.head())

high_2015  = df_2015.groupby('Date')['Data_Value'].max()
print(high_2015.head())

low_2015 = df_2015.groupby('Date')['Data_Value'].min()
print(low_2015.head())

# pegar recordes quebrados em 2015
observation_dates = list(range(1,366))

x = np.linspace(1,365,365)
y = np.linspace(1,365,365)

record_high_2015 = high_2015[high_2015 >= high.reindex_like(high_2015)]
print(record_high_2015.head())

x = [n for n in range(0,365) if (high_2015.iloc[n] >= high.iloc[n]) ]
print(x)

record_low_2015 = low_2015[low_2015 <= low.reindex_like(low_2015)]
print(record_low_2015.head())

y = [n for n in range(0,365) if (low_2015.iloc[n] <= low.iloc[n]) ]
print(y)

# grafico
plt.figure(figsize = (12, 10))
graph = plt.gca()

graph.set_xlabel('Day of the year')
graph.set_ylabel('Temperature (tenths of degrees C)')
graph.set_title('Record highest and lowest temperature by day of the year')

plt.plot(observation_dates, high, '-o', observation_dates, low, '-o', zorder = 1)
graph.legend(['Record high temperatures', 'Record low temperatures'])

plt.scatter(x, record_high_2015, s = 100, c = 'red', zorder = 2, alpha = 0.7)
plt.scatter(y, record_low_2015, s = 100, c = 'red', zorder = 2, alpha = 0.7)

graph.legend(['Record high temperatures', 'Record low temperatures','Record broken in 2015'])

graph.fill_between(observation_dates, high, low, facecolor = 'blue', alpha = 0.25)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()
