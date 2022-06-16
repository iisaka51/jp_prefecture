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

cols=[0,4,5,7,12,13]
names=[ 'prefCode',
        'cityCode', 'cityName', 'cityAlphabet',
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
    ' Shi ': '-shi ',
    ' Shi ': '-shi ',
    ' Gun ': '-gun ',
    ' Shi$': '-shi',
    '-Shi$': '-shi',
    ' Ku$': '-ku',
    ' Cho$': '-cho',
    ' Machi$': '-machi',
    ' Son$': '-son',
    ' Mura$': '-mura',
}

# See Also:
# BaseUrl='https://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/'
# heso_data = [
#   'hokkaido_heso.pdf',
#   'miyagi_heso.pdf',
#   'saitama_heso.pdf',
#   'chiba_heso.pdf',
#   'kanagawa_heso.pdf',
#   'niigata_heso.pdf',
#   'shizuoka_heso.pdf',
#   'aichi_heso.pdf',
#   'kyoto_heso.pdf',
#   'osaka_heso.pdf',
#   'hyogo_heso.pdf',
#   'okayama_heso.pdf',
#   'hiroshima_heso.pdf',
#   'fukuoka_heso.pdf',
#   'kumamoto_heso.pdf',
# ]


major_city = [
    [1,'01100','札幌市','Sapporo-shi',43.0351,141.2049,2],
    [4,'04100','仙台市','Sendai-shi',38.1608,140.5219,2],
    [11,'11100','さいたま市','Saitama-shi',35.5142,139.3843,2],
    [12,'12100','千葉市','Chiba-shi',35.3626,140.0625,2],
    [14,'14100','横浜市','Yokohama-shi',35.2639,139.3817,2],
    [14,'14130','川崎市','Kawasaki-shi',35.3148,139.4209,2],
    [14,'14150','相模原市','Sagamihara-shi',35.3417,139.2224,2],
    [15,'15100','新潟市','Niigata-shi',37.5458,139.0211,2],
    [22,'22100','静岡市','Shizuoka-shi',34.5837,138.2258,2],
    [22,'22130','浜松市','Hamamatsu-shi',34.4239,137.4336,2],
    [23,'23100','名古屋市','Nagoya-shi',35.1049,136.5424,2],
    [26,'26100','京都市','Kyoto-shi',35.0117,135.4520,2],
    [27,'27100','大阪市','Osaka-shi',34.4138,135.3808,2],
    [27,'27140','堺市','Sakai-shi',34.3424,135.2859,2],
    [28,'28100','神戸市','Kobe-shi',34.4129,135.1049,2],
    [33,'33100','岡山市','Okayama-shi',34.3942,133.5606,2],
    [34,'34100','広島市','Hiroshima-shi',34.2347,132.2734,2],
    [40,'40100','北九州市','Kitakyushu-shi',33.3623,130.2505,2],
    [40,'40130','福岡市','Fukuoka-shi',33.3623,130.2505,2],
    [43,'43100','熊本市','Kumamoto-shi',32.4723,130.4430,2],
]


data = df[~df.duplicated(keep='first',subset='cityCode')].copy()
data['prefCode'] = pd.to_numeric(data['prefCode'], downcast='integer')
# data['latitude'] = pd.to_numeric(data['latitude'], downcast='float')
# data['longitude'] = pd.to_numeric(data['longitude'], downcast='float')
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['latitude'].astype(float)

data['bigCityFlag']=0

# Set 3 to bigCityFlag for Tokyo
data.loc[data['prefCode']==13, ['bigCityFlag']]=3

data['bigCityFlag']=pd.to_numeric(data['bigCityFlag'], downcast='integer')

major_data = pd.DataFrame(major_city, columns=names+['bigCityFlag'])
data = pd.concat([data, major_data]).copy()

data['cityAlphabet'] = data['cityAlphabet'].str.title()
data = data.replace({'cityAlphabet': replace_vallues }, regex=True)
data.sort_values('cityCode', inplace=True)
data.reset_index(drop=True,inplace=True)

if __name__ == '__main__':
    data.to_csv('allcities.csv')
