"""
 0  都道府県コード
 1  都道府県名
 2  都道府県名カナ
 3  都道府県名ローマ字
 4  市区町村コード
 5  市区町村名
 6  市区町村名カナ
 7  市区町村名ローマ字
 8  大字町丁目名
 9  大字町丁目名カナ
 10 大字町丁目名ローマ字
 11 小字・通称名
 12 緯度
 13 経度
"""

import pandas as pd

cols=[0,4,8,10,12,13]
names=[ 'prefCode', 'cityCode',
        'town', 'townAlphabet',
        'latitude', 'longitude'
    ]

url=( 'https://github.com/iisaka51/'
       'japanese-addresses/raw/develop/data/latest.csv' )
df = pd.read_csv(url,
                 usecols=cols,
                 header=None,
                 skiprows=1,
                 dtype=str,
                 names=names,
            )

replace_vallues = {
    ' Shi ': '-Shi ',
    ' Shi ': '-Shi ',
    ' Gun ': '-Gun ',
    ' Shi$': '-Shi',
    '-Shi$': '-Shi',
    ' Ku$': '-Ku',
    ' Cho$': '-Cho',
    ' Machi$': '-Machi',
    ' Son$': '-Son',
    ' Mura$': '-Mura',
}

data = df[~df.duplicated(keep='first',subset=['cityCode','town'])].copy()
data['prefCode'] = pd.to_numeric(data['prefCode'], downcast='integer')
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

data['bigCityFlag']=0
data['bigCityFlag']=pd.to_numeric(data['bigCityFlag'], downcast='integer')

data['townAlphabet'] = data['townAlphabet'].str.title()
data = data.replace({'townAlphabet': replace_vallues }, regex=True)
data.sort_values('cityCode', inplace=True)
data.reset_index(drop=True,inplace=True)

if __name__ == '__main__':
    data.to_csv('towns.csv')
