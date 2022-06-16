import pandas as pd

bigcity = pd.read_csv('semimajor.csv', dtype=str,
                 names=['prefCode', 'cityCode', 'cityName'] )
city = pd.read_csv('allcities.csv', index_col=0, dtype=str)

for code in bigcity['cityCode'].values:
    city.loc[city['cityCode'] == code, ['bigCityFlag']]=1

city.to_csv('allcities.csv')
