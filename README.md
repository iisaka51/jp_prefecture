# jp_prefecture.
> Japan prefecture and city names and codes

Simple utility to convert the name of japanese prefectures and cities.

- parser for japanese address.
- full_name from/to code (JIS X 0401-1973, JIX X 0402).
- short_name to full_name (prefecture only)
- alphabet_name from/to full_name
- validate for full_name and short_name, alphabet_name.
- allow code as str or int.
- support lists and pandas serires as input.
- support checkdigits for citycode.
- support regular expression for cityName.
- get geodetic(latitude, longitude) from cityCode or cityName

Reference

- https://www.soumu.go.jp/denshijiti/code.html (in japanese)

## Install

`pip install jp_prefecture`

## How to use

```python
from jp_prefecture import jp_prefectures as jp

# or

from jp_prefecture.jp_cities import jp.jp_cities as jp

# If you want to town data.
del jp
jp = JpCity(enable_town=True)

# or Set Shell Environment variable

export JP_PREFECTURE_ENABLE_TOWN=1

# and, japanese address parser.

from jp_prefecture.address import JpAddressParser, JpAddress
parser = JpAddressParser()

```


## class JpAddressParser

- `parse_address()`


```python
from jp_prefecture.address import JpAddressParser, JpAddress
parser = JpAddressParser()

data = '〒617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == '6170826' )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '開田1丁目-2-3 アパート123号室')
assert ( addr.prefCode == 26)
assert ( addr.cityCode == 26209)
assert ( addr.geodetic == (34.928769, 135.696847))


data = '〒617-0824 長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == '6170824' )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

data = '6170824 長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == '6170824' )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

data = '長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '京都府長岡京市天神２丁目１５−１３')

data = '京都長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '京都府長岡京市天神２丁目１５−１３')


data = '京都 長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '京都府長岡京市天神２丁目１５−１３')

data = '京都府 長岡京市天神２丁目１５−１３'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '長岡京市' )
assert ( addr.street == '天神２丁目１５−１３')
assert ( addr.geodetic == (34.923314, 135.685162))
assert ( addr.__str__()
         == '京都府長岡京市天神２丁目１５−１３')

data = '京都市下京区烏丸通七条下ル 東塩小路町 721-1'

addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '京都市下京区' )
assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
assert ( addr.prefCode == 26)
assert ( addr.cityCode == 26106)
assert ( addr.geodetic == (35.002973, 135.764009))

data = '京都市 下京区烏丸通七条下ル 東塩小路町 721-1'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '京都市下京区' )
assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
assert ( addr.prefCode == 26)
assert ( addr.cityCode == 26106)
assert ( addr.geodetic == (35.002973, 135.764009))
assert ( addr.__str__()
         == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

data = '京都 下京区 烏丸通七条下ル 東塩小路町 721-1'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '京都府' )
assert ( addr.city == '京都市下京区' )
assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
assert ( addr.prefCode == 26)
assert ( addr.cityCode == 26106)
assert ( addr.geodetic == (35.002973, 135.764009))
assert ( addr.__str__()
         == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

data = '千代田区丸の内1-9-2グラントウキョウサウスタワー23階'

addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '東京都')
assert ( addr.city == '千代田区' )
assert ( addr.street == '丸の内1-9-2グラントウキョウサウスタワー23階')
assert ( addr.prefCode == 13)
assert ( addr.cityCode == 13101)
assert ( addr.geodetic == (35.68156, 139.767201))
assert ( addr.__str__()
   ==  '東京都千代田区丸の内1-9-2グラントウキョウサウスタワー23階' )

data = '千代田区 丸の内1-9-2グラントウキョウサウスタワー23階'
addr = self.parser.parse_address(data)
assert ( addr.zipCode == None )
assert ( addr.prefecture == '東京都')
assert ( addr.city == '千代田区' )
assert ( addr.street == '丸の内1-9-2グラントウキョウサウスタワー23階')
assert ( addr.prefCode == 13)
assert ( addr.cityCode == 13101)
assert ( addr.geodetic == ( 35.68156, 139.767201))
assert ( addr.__str__()
   ==  '東京都千代田区丸の内1-9-2グラントウキョウサウスタワー23階' )
```

### Dataframe of jp.prefectures

```python
In [2]: jp.prefectures
Out[2]:
      name short_name alphabet_name
code
1      北海道         北海      Hokkaido
2      青森県         青森        Aomori
3      岩手県         岩手         Iwate
4      宮城県         宮城        Miyagi
5      秋田県         秋田         Akita
6      山形県         山形      Yamagata
7      福島県         福島     Fukushima
8      茨城県         茨城       Ibaraki
9      栃木県         栃木       Tochigi
10     群馬県         群馬         Gunma
11     埼玉県         埼玉       Saitama
12     千葉県         千葉         Chiba
13     東京都         東京         Tokyo
14    神奈川県        神奈川      Kanagawa
15     新潟県         新潟       Niigata
16     富山県         富山        Toyama
17     石川県         石川      Ishikawa
18     福井県         福井         Fukui
19     山梨県         山梨     Yamanashi
20     長野県         長野        Nagano
21     岐阜県         岐阜          Gifu
22     静岡県         静岡      Shizuoka
23     愛知県         愛知         Aichi
24     三重県         三重           Mie
25     滋賀県         滋賀         Shiga
26     京都府         京都         Kyoto
27     大阪府         大阪         Osaka
28     兵庫県         兵庫         Hyogo
29     奈良県         奈良          Nara
30    和歌山県        和歌山      Wakayama
31     鳥取県         鳥取       Tottori
32     島根県         島根       Shimane
33     岡山県         岡山       Okayama
34     広島県         広島     Hiroshima
35     山口県         山口     Yamaguchi
36     徳島県         徳島     Tokushima
37     香川県         香川        Kagawa
38     愛媛県         愛媛         Ehime
39     高知県         高知         Kochi
40     福岡県         福岡       Fukuoka
41     佐賀県         佐賀          Saga
42     長崎県         長崎      Nagasaki
43     熊本県         熊本      Kumamoto
44     大分県         大分          Oita
45     宮崎県         宮崎      Miyazaki
46    鹿児島県        鹿児島     Kagoshima
47     沖縄県         沖縄       Okinawa

In [3]: jp.prefectures.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 47 entries, 1 to 47
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   name           47 non-null     object
 1   short_name     47 non-null     object
 2   alphabet_name  47 non-null     object
dtypes: object(3)
memory usage: 1.2+ KB

In [4]:
>>>
```

## Dataframe of Cities

```python
In [1]: from jp_prefecture.jp_cities import jp_cities as jp

In [2]: jp.cities
Out[2]:
      prefCode  cityCode  cityName              cityAlphabet  latitude  longitude  bigCityFlag
0            1      1100       札幌市               Sapporo-shi   43.0351   141.2049            2
1            1      1101    札幌市中央区       Sapporo-shi Chuo-ku   43.0422   141.3197            1
2            1      1102     札幌市北区       Sapporo-shi Kita-ku   43.1571   141.3902            1
3            1      1103     札幌市東区    Sapporo-shi Higashi-ku   43.1208   141.3944            1
4            1      1104    札幌市白石区  Sapporo-shi Shiroishi-ku   43.0716   141.4370            1
...        ...       ...       ...                       ...       ...        ...          ...
1909        47     47361   島尻郡久米島町  Shimajiri-gun Kumejim...   26.3474   126.7697            0
1910        47     47362   島尻郡八重瀬町   Shimajiri-gun Yaese-cho   26.1260   127.7472            0
1911        47     47375   宮古郡多良間村     Miyako-gun Tarama-son   24.6578   124.6854            0
1912        47     47381   八重山郡竹富町  Yaeyama-gun Taketomi-cho   24.2371   124.0119            0
1913        47     47382  八重山郡与那国町  Yaeyama-gun Yonaguni-cho   24.4559   122.9877            0

In [3]: jp.cities.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1914 entries, 0 to 1913
Data columns (total 7 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   prefCode      1914 non-null   int8
 1   cityCode      1914 non-null   int32
 2   cityName      1914 non-null   object
 3   cityAlphabet  1914 non-null   object
 4   latitude      1914 non-null   float64
 5   longitude     1914 non-null   float64
 6   bigCityFlag   1914 non-null   int8
dtypes: float64(2), int32(1), int8(2), object(2)
memory usage: 86.0+ KB

In [4]:

```

## Dataframe of Towns

```python
In [1]: import os

In [2]: os.environ.update({'JP_PREFECTURE_ENABLE_TOWN': '1'})

In [3]: from jp_prefecture.jp_cities import jp_cities as jp

In [4]: jp.towns
Out[4]:
        prefCode  cityCode        town         townAlphabet  latitude  longitude  bigCityFlag
0              1      1101      旭ケ丘一丁目         Asahigaoka 1   43.0422   141.3197            0
1              1      1101  南二十五条西十一丁目  Minami25-Jonishi 11   43.0261   141.3446            0
2              1      1101  南二十五条西十二丁目  Minami25-Jonishi 12   43.0259   141.3430            0
3              1      1101  南二十五条西十三丁目  Minami25-Jonishi 13   43.0258   141.3412            0
4              1      1101  南二十五条西十四丁目  Minami25-Jonishi 14   43.0255   141.3401            0
...          ...       ...         ...                  ...       ...        ...          ...
277186        47     47381         字鳩間                  NaN   24.4723   123.8204            0
277187        47     47381         字竹富                  NaN   24.3261   124.0891            0
277188        47     47381       字南風見仲                  NaN   24.2882   123.8880            0
277189        47     47381         字新城                  NaN   24.2340   123.9449            0
277190        47     47382        字与那国                  NaN   24.4559   122.9877            0

In [5]: jp.towns.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 277191 entries, 0 to 277190
Data columns (total 7 columns):
 #   Column        Non-Null Count   Dtype
---  ------        --------------   -----
 0   prefCode      277191 non-null  int8
 1   cityCode      277191 non-null  int32
 2   town          277191 non-null  object
 3   townAlphabet  237491 non-null  object
 4   latitude      277191 non-null  float64
 5   longitude     277191 non-null  float64
 6   bigCityFlag   277191 non-null  int8
dtypes: float64(2), int32(1), int8(2), object(2)
memory usage: 12.2+ MB

In [6]:
```

## class JpPrefecture

 - `name2code()`
 - `code2name()`
 - `name2normalize()`
 - `validate()`


```python
from jp_prefecture import jp_prefectures as jp
import pandas as pd

assert ( jp.name2code('京都府')
         == jp.name2code('京都')
         == jp.name2code('Kyoto')
         == jp.name2code('KYOTO')
         == jp.name2code('kyoto')
         == 26 )

assert ( jp.name2code(['京都府', '大阪府', '奈良県'])
         == jp.name2code(['京都', '大阪', '奈良'])
         == jp.name2code(['Kyoto', 'Osaka', 'Nara'])
         == jp.name2code(['KYOTO', 'OSAKA', 'NARA'])
         == jp.name2code(['kyoto', 'osaka', 'nara'])
         == [26, 27, 29] )

s1 = jp.name2code(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.name2code(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.name2code(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.name2code(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.name2code(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series([26, 27, 29])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

assert jp.code2name(26) == '京都府'
assert jp.code2name("26") == '京都府'

assert ( jp.code2name([26, 27, 29])
         == ['京都府', '大阪府', '奈良県'] )
assert ( jp.code2name(["26", "27", "29"])
         == ['京都府', '大阪府', '奈良県'] )

s1 = jp.code2name(pd.Series([26, 27, 29]))
s2 = pd.Series(['京都府', '大阪府', '奈良県'])
assert s1.equals(s2) == True
s1 = jp.code2name(pd.Series(["26", "27", "29"]))
s2 = pd.Series(['京都府', '大阪府', '奈良県'])
assert s1.equals(s2) == True

assert jp.code2name(26, ascii=True) == 'Kyoto'
assert jp.code2name("26", ascii=True) == 'Kyoto'

assert ( jp.code2name([26, 27, 29], ascii=True)
         == ['Kyoto', 'Osaka', 'Nara'] )
assert ( jp.code2name(["26", "27", "29"], ascii=True)
         == ['Kyoto', 'Osaka', 'Nara'] )

s1 = jp.code2name(pd.Series([26, 27, 29]), ascii=True)
s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert s1.equals(s2) == True

s1 = jp.code2name(pd.Series(["26", "27", "29"]), ascii=True)
s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert s1.equals(s2) == True

assert ( jp.name2normalize('京都府')
         == jp.name2normalize('京都')
         == jp.name2normalize('Kyoto')
         == jp.name2normalize('KYOTO')
         == jp.name2normalize('kyoto')
         == '京都府' )

assert ( jp.name2normalize(['京都府', '大阪府', '奈良県'])
         == jp.name2normalize(['京都', '大阪', '奈良'])
         == jp.name2normalize(['Kyoto', 'Osaka', 'Nara'])
         == jp.name2normalize(['KYOTO', 'OSAKA', 'NARA'])
         == jp.name2normalize(['kyoto', 'osaka', 'nara'])
         == ['京都府', '大阪府', '奈良県'] )

s1 = jp.name2normalize(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.name2normalize(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.name2normalize(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.name2normalize(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.name2normalize(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series(['京都府', '大阪府', '奈良県'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

assert ( jp.name2normalize('京都府', ascii=True)
         == jp.name2normalize('京都', ascii=True)
         == jp.name2normalize('Kyoto', ascii=True)
         == jp.name2normalize('KYOTO', ascii=True)
         == jp.name2normalize('kyoto', ascii=True)
         == 'Kyoto' )

assert ( jp.name2normalize(['京都府', '大阪府', '奈良県'], ascii=True)
         == jp.name2normalize(['京都', '大阪', '奈良'], ascii=True)
         == jp.name2normalize(['Kyoto', 'Osaka', 'Nara'], ascii=True)
         == jp.name2normalize(['KYOTO', 'OSAKA', 'NARA'], ascii=True)
         == jp.name2normalize(['kyoto', 'osaka', 'nara'], ascii=True)
         == ['Kyoto', 'Osaka', 'Nara'] )

s1 = jp.name2normalize(
        pd.Series(['京都府', '大阪府', '奈良県']), ascii=True)
s2 = jp.name2normalize(
        pd.Series(['京都', '大阪', '奈良']), ascii=True)
s3 = jp.name2normalize(
        pd.Series(['Kyoto', 'Osaka', 'Nara']), ascii=True)
s4 = jp.name2normalize(
        pd.Series(['KYOTO', 'OSAKA', 'NARA']), ascii=True)
s5 = jp.name2normalize(
        pd.Series(['kyoto', 'osaka', 'nara']), ascii=True)
s6 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

assert ( jp.validate('京都府')
         == jp.validate('京都')
         == jp.validate('Kyoto')
         == jp.validate('KYOTO')
         == jp.validate('kyoto')
         == True )

assert ( jp.validate('京都県')
         == jp.validate('都京')
         == jp.validate('KyOto')
         == jp.validate('KYoTO')
         == jp.validate('kyotofu')
         == False )

assert ( jp.validate(['京都府', '大阪府', '奈良県'])
         == jp.validate(['京都', '大阪', '奈良'])
         == jp.validate(['Kyoto', 'Osaka', 'Nara'])
         == jp.validate(['KYOTO', 'OSAKA', 'NARA'])
         == jp.validate(['kyoto', 'osaka', 'nara'])
         == [True, True, True] )

assert ( jp.validate(['京都県', '大阪府', '奈良県'])
         == jp.validate(['都京', '大阪', '奈良'])
         == jp.validate(['KyOto', 'Osaka', 'Nara'])
         == jp.validate(['KYoTO', 'OSAKA', 'NARA'])
         == jp.validate(['kyotofu', 'osaka', 'nara'])
         == [False, True, True] )

s1 = jp.validate(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.validate(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.validate(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.validate(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.validate(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series([True, True, True])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

s1 = jp.validate(pd.Series(['京都県', '大阪府', '奈良県']))
s2 = jp.validate(pd.Series(['都京', '大阪', '奈良']))
s3 = jp.validate(pd.Series(['KyOto', 'Osaka', 'Nara']))
s4 = jp.validate(pd.Series(['KYoTO', 'OSAKA', 'NARA']))
s5 = jp.validate(pd.Series(['kyotofu', 'osaka', 'nara']))
s6 = pd.Series([False, True, True])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

```

## class JpCity

JpCity class is subclass of JpPrefecture.

- `citycode2name()`
- `cityname2code()`
- `cityname2normalize()`
- `citycode2normalize()`
- `cityname2prefcode()`
- `cityname2preffecture()`
- `cityname2geodetic()`
- `citycode2geodetic()`
- `findcity()`
- `validate_city()`

```python
from jp_prefecture.jp_cities import jp_cities as jp
import pandas as pd

assert ( jp.cityname2code('札幌市')
         == jp.cityname2code('Sapporo-shi')
         == 1100 )

assert ( jp.cityname2code('札幌市', as_str=True)
         == jp.cityname2code('Sapporo-shi', as_str=True)
         == "01100" )

assert ( jp.cityname2code('京都市')
         == jp.cityname2code('Kyoto-shi')
         == 26100 )

assert ( jp.cityname2code('KYOTO-SHI')
         == jp.cityname2code('kyoto-shi')
         == None )

assert ( jp.cityname2code('京都市', ignore_case=True)
         == jp.cityname2code('Kyoto-shi', ignore_case=True)
         == jp.cityname2code('KYOTO-SHI', ignore_case=True)
         == jp.cityname2code('kyoto-shi', ignore_case=True)
         == 26100 )

assert ( jp.cityname2code('京都市', checkdigit=True)
         == jp.cityname2code('Kyoto-shi', checkdigit=True)
         == 261009 )

assert ( jp.cityname2code(
            ['京都市北区', '京都市左京区', '京都市右京区'])
         == jp.cityname2code(
                ['Kyoto-shi Kita-ku',
                 'Kyoto-shi Sakyo-ku',
                 'Kyoto-shi Ukyo-ku'] )
         == [26101, 26103, 26108] )

assert ( jp.cityname2code(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU'] )
         == jp.cityname2code(
                ['kyoto-shi kita-ku',
                 'kyoto-shi sakyo-ku',
                 'kyoto-shi ukyo-ku'] )
         == [None, None, None] )

assert ( jp.cityname2code(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU'], ignore_case=True )
         == jp.cityname2code(
                ['kyoto-shi kita-ku',
                 'kyoto-shi sakyo-ku',
                 'kyoto-shi ukyo-ku'], ignore_case=True )
         == [26101, 26103, 26108] )

s1 = jp.cityname2code( pd.Series(
             ['京都市北区', '京都市左京区', '京都市右京区']))
s2 = jp.cityname2code( pd.Series(
                ['Kyoto-shi Kita-ku',
                 'Kyoto-shi Sakyo-ku',
                 'Kyoto-shi Ukyo-ku'] ))
s3 = pd.Series([26101, 26103, 26108])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2code( pd.Series(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU'] ))
s2 = jp.cityname2code( pd.Series(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU'] ))
s3 = pd.Series([None, None, None])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2code( pd.Series(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU']), ignore_case=True )
s2 = jp.cityname2code( pd.Series(
                ['KYOTO-SHI KITA-KU',
                 'KYOTO-SHI SAKYO-KU',
                 'KYOTO-SHI UKYO-KU']), ignore_case=True )
s3 = pd.Series([26101, 26103, 26108])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

assert ( jp.cityname2normalize('京都市')
         == jp.cityname2normalize('Kyoto-shi')
         == '京都市')

assert ( jp.cityname2normalize('KYOTO-SHI')
         == jp.cityname2normalize('kyoto-shi')
         == None )

assert ( jp.cityname2normalize('京都市')
         == jp.cityname2normalize('KYOTO-SHI', ignore_case=True)
         == jp.cityname2normalize('kyoto-shi', ignore_case=True)
         == '京都市')

assert ( jp.cityname2normalize(
            ['京都市北区',
             '京都市左京区',
             '京都市右京区'])
         == jp.cityname2normalize(
            ['Kyoto-shi Kita-ku',
             'Kyoto-shi Sakyo-ku',
             'Kyoto-shi Ukyo-ku'] )
         == ['京都市北区',
             '京都市左京区',
             '京都市右京区'])

assert ( jp.cityname2normalize(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU'] )
         == jp.cityname2normalize(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku'] )
         == [None, None, None] )

assert ( jp.cityname2normalize(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU'], ignore_case=True )
         == jp.cityname2normalize(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku'], ignore_case=True)
         == ['京都市北区',
             '京都市左京区',
             '京都市右京区'])

s1 = jp.cityname2normalize( pd.Series(
                 ['京都市北区',
                  '京都市左京区',
                   '京都市右京区']))
s2 = jp.cityname2normalize( pd.Series(
                 ['Kyoto-shi Kita-ku',
                  'Kyoto-shi Sakyo-ku',
                  'Kyoto-shi Ukyo-ku'] ))
s3 = pd.Series( ['京都市北区',
                 '京都市左京区',
                 '京都市右京区'])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2normalize( pd.Series(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU'] ))
s2 = jp.cityname2normalize( pd.Series(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku'] ))
s3 = pd.Series( [None, None, None] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2normalize( pd.Series(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU']), ignore_case=True )
s2 = jp.cityname2normalize( pd.Series(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku']), ignore_case=True)
s3 = pd.Series( ['京都市北区',
                 '京都市左京区',
                 '京都市右京区'])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

assert ( jp.cityname2normalize('京都市',ascii=True)
         == jp.cityname2normalize('Kyoto-shi',ascii=True)
         == "Kyoto-shi" )

assert ( jp.cityname2normalize('KYOTO-SHI',ascii=True)
         == jp.cityname2normalize('kyoto-shi',ascii=True)
         == None )

assert ( jp.cityname2normalize('KYOTO-SHI',
                ascii=True, ignore_case=True)
         == jp.cityname2normalize('kyoto-shi',
                ascii=True, ignore_case=True)
         == "Kyoto-shi" )

assert ( jp.cityname2normalize(
            ['京都市北区',
             '京都市左京区',
             '京都市右京区'], ascii=True)
         == jp.cityname2normalize(
            ['Kyoto-shi Kita-ku',
             'Kyoto-shi Sakyo-ku',
             'Kyoto-shi Ukyo-ku'], ascii=True)
         == ['Kyoto-shi Kita-ku',
             'Kyoto-shi Sakyo-ku',
             'Kyoto-shi Ukyo-ku']  )

assert ( jp.cityname2normalize(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU'], ascii=True)
         == jp.cityname2normalize(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku'], ascii=True)
         == [None, None, None] )

assert ( jp.cityname2normalize(
            ['KYOTO-SHI KITA-KU',
             'KYOTO-SHI SAKYO-KU',
             'KYOTO-SHI UKYO-KU'], ascii=True, ignore_case=True)
         == jp.cityname2normalize(
            ['kyoto-shi kita-ku',
             'kyoto-shi sakyo-ku',
             'kyoto-shi ukyo-ku'], ascii=True, ignore_case=True)
         == ['Kyoto-shi Kita-ku',
             'Kyoto-shi Sakyo-ku',
             'Kyoto-shi Ukyo-ku']  )

s1 = jp.cityname2normalize( pd.Series(
             ['京都市北区',
              '京都市左京区',
              '京都市右京区']), ascii=True)
s2 = jp.cityname2normalize( pd.Series(
             ['Kyoto-shi Kita-ku',
              'Kyoto-shi Sakyo-ku',
              'Kyoto-shi Ukyo-ku'] ), ascii=True)
s3 = pd.Series( ['Kyoto-shi Kita-ku',
                 'Kyoto-shi Sakyo-ku',
                 'Kyoto-shi Ukyo-ku'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2normalize( pd.Series(
             ['KYOTO-SHI KITA-KU',
              'KYOTO-SHI SAKYO-KU',
              'KYOTO-SHI UKYO-KU'] ), ascii=True)
s2 = jp.cityname2normalize( pd.Series(
             ['kyoto-shi kita-ku',
              'kyoto-shi sakyo-ku',
              'kyoto-shi ukyo-ku'] ), ascii=True)
s3 = pd.Series([None, None, None])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2normalize( pd.Series(
             ['KYOTO-SHI KITA-KU',
              'KYOTO-SHI SAKYO-KU',
              'KYOTO-SHI UKYO-KU'] ), ascii=True, ignore_case=True)
s2 = jp.cityname2normalize( pd.Series(
             ['kyoto-shi kita-ku',
              'kyoto-shi sakyo-ku',
              'kyoto-shi ukyo-ku'] ), ascii=True, ignore_case=True)
s3 = pd.Series( ['Kyoto-shi Kita-ku',
                 'Kyoto-shi Sakyo-ku',
                 'Kyoto-shi Ukyo-ku'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

assert jp.citycode2normalize(26100) == 26100
assert jp.citycode2normalize(261009) == 26100
assert jp.citycode2normalize(26100, as_str=True) == '26100'
assert jp.citycode2normalize(261009, as_str=True) == '26100'
assert jp.citycode2normalize("26100") == 26100
assert jp.citycode2normalize("261009") == 26100
assert jp.citycode2normalize("26100", as_str=True) == '26100'
assert jp.citycode2normalize("261009", as_str=True) == '26100'

assert jp.citycode2name(26100) == '京都市'
assert jp.citycode2name("26100") == '京都市'
assert jp.citycode2name(261009) == '京都市'
assert jp.citycode2name("261009") == '京都市'

assert ( jp.citycode2name([26101, 26103, 26108])
         ==  ['京都市北区', '京都市左京区', '京都市右京区'] )

assert jp.citycode2name(26100, ascii=True) == 'Kyoto-shi'
assert jp.citycode2name("26100", ascii=True) == 'Kyoto-shi'
assert jp.citycode2name(261009, ascii=True) == 'Kyoto-shi'
assert jp.citycode2name("261009", ascii=True) == 'Kyoto-shi'
assert ( jp.citycode2name([26101, 26103, 26108], ascii=True)
        == ['Kyoto-shi Kita-ku',
            'Kyoto-shi Sakyo-ku',
            'Kyoto-shi Ukyo-ku'] )

s1 = jp.citycode2name(pd.Series([26101, 26103, 26108]), ascii=True)
s2 = pd.Series( ['Kyoto-shi Kita-ku',
                 'Kyoto-shi Sakyo-ku',
                 'Kyoto-shi Ukyo-ku'] )
assert s1.equals(s2) == True


assert ( jp.cityname2prefcode('京都市')
         == jp.cityname2prefcode('Kyoto-shi')
         == 26 )

assert ( jp.cityname2prefcode('KYOTO-SHI')
         == jp.cityname2prefcode('kyoto-shi')
         == None )

assert ( jp.cityname2prefcode('京都市', ignore_case=True)
         == jp.cityname2prefcode('KYOTO-SHI', ignore_case=True)
         == jp.cityname2prefcode('kyoto-shi', ignore_case=True)
         == 26 )

assert ( jp.cityname2prefcode(['京都市北区', '大阪市中央区'])
         == jp.cityname2prefcode(['Kyoto-shi Kita-ku',
                                  'Osaka-shi Chuo-ku'])
         == [26, 27] )

assert ( jp.cityname2prefcode(['KYOTO-SHI KITA-KU',
                               'OSAKA-SHI CHUO-KU'])
         == jp.cityname2prefcode(['kyoto-shi kita-ku',
                                  'osaka-shi chuo-ku'])
         == [None, None] )

assert ( jp.cityname2prefcode(
               ['京都市北区', '大阪市中央区'],
               ignore_case=True)
         == jp.cityname2prefcode(
               ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
               ignore_case=True)
         == jp.cityname2prefcode(
               ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
               ignore_case=True)
         == [26, 27] )

s1 = jp.cityname2prefcode(
        pd.Series(['京都市北区', '大阪市中央区']))
s2 = jp.cityname2prefcode(
        pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']))
s3 = pd.Series([26, 27])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefcode(
        pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
s2 = jp.cityname2prefcode(
        pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
s3 = pd.Series([None, None])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefcode(
        pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
        ignore_case=True)
s2 = jp.cityname2prefcode(
        pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
        ignore_case=True)
s3 = pd.Series([26, 27])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

assert ( jp.cityname2prefecture('京都市')
         == jp.cityname2prefecture('Kyoto-shi')
         == '京都府' )

assert ( jp.cityname2prefecture('KYOTO-SHI')
         == jp.cityname2prefecture('kyoto-shi')
         == None )

assert ( jp.cityname2prefecture('京都市', ignore_case=True)
         == jp.cityname2prefecture('Kyoto-shi', ignore_case=True)
         == jp.cityname2prefecture('KYOTO-SHI', ignore_case=True)
         == jp.cityname2prefecture('kyoto-shi', ignore_case=True)
         == '京都府' )

assert ( jp.cityname2prefecture(['京都市北区', '大阪市中央区'])
         == jp.cityname2prefecture(['Kyoto-shi Kita-ku',
                                    'Osaka-shi Chuo-ku'])
         == ['京都府', '大阪府'] )

assert ( jp.cityname2prefecture(
             ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'])
         == jp.cityname2prefecture(
             ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'])
         == [None, None] )

assert ( jp.cityname2prefecture(
              ['京都市北区', '大阪市中央区'],
              ignore_case=True)
         == jp.cityname2prefecture(
              ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
              ignore_case=True)
         == jp.cityname2prefecture(
              ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
              ignore_case=True)
         == jp.cityname2prefecture(
              ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
              ignore_case=True)
         == ['京都府', '大阪府'] )

s1 = jp.cityname2prefecture(
            pd.Series( ['京都市北区', '大阪市中央区']))
s2 = jp.cityname2prefecture(
            pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']))
s3 = pd.Series(['京都府', '大阪府'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefecture(
            pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
s2 = jp.cityname2prefecture(
            pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
s3 = pd.Series([None, None] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefecture(
            pd.Series( ['京都市北区', '大阪市中央区']),
            ignore_case=True)
s2 = jp.cityname2prefecture(
            pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
            ignore_case=True)
s3 = jp.cityname2prefecture(
            pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
            ignore_case=True)
s4 = jp.cityname2prefecture(
            pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
            ignore_case=True)
s5 = pd.Series(['京都府', '大阪府'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == True )

assert ( jp.cityname2prefecture('京都市', ascii=True)
         == jp.cityname2prefecture('Kyoto-shi', ascii=True)
         == 'Kyoto' )

assert ( jp.cityname2prefecture('KYOTO-SHI', ascii=True)
         == jp.cityname2prefecture('kyoto-shi', ascii=True)
         == None )

assert ( jp.cityname2prefecture('京都市',
                 ascii=True, ignore_case=True)
         == jp.cityname2prefecture('Kyoto-shi',
                 ascii=True, ignore_case=True)
         == jp.cityname2prefecture('KYOTO-SHI',
                 ascii=True, ignore_case=True)
         == jp.cityname2prefecture('kyoto-shi',
                 ascii=True, ignore_case=True)
         == 'Kyoto' )

assert ( jp.cityname2prefecture(
             ['京都市北区', '大阪市中央区'],
             ascii=True)
         == jp.cityname2prefecture(
             ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
             ascii=True)
         == ['Kyoto', 'Osaka'] )

assert ( jp.cityname2prefecture(
             ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
             ascii=True)
         == jp.cityname2prefecture(
             ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
             ascii=True)
         == [None, None] )

assert ( jp.cityname2prefecture(
             ['京都市北区', '大阪市中央区'],
             ascii=True, ignore_case=True)
         == jp.cityname2prefecture(
             ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
             ascii=True, ignore_case=True)
         == jp.cityname2prefecture(
             ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
             ascii=True, ignore_case=True)
         == jp.cityname2prefecture(
             ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
             ascii=True, ignore_case=True)
         == ['Kyoto', 'Osaka'] )

s1 = jp.cityname2prefecture(
             pd.Series(['京都市北区', '大阪市中央区']),
             ascii=True)
s2 = jp.cityname2prefecture(
             pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
             ascii=True)
s3 = pd.Series(['Kyoto', 'Osaka'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefecture(
             pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
             ascii=True)
s2 = jp.cityname2prefecture(
             pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
             ascii=True)
s3 = pd.Series([None, None])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.cityname2prefecture(
             pd.Series(['京都市北区', '大阪市中央区']),
             ascii=True, ignore_case=True)
s2 = jp.cityname2prefecture(
             pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
             ascii=True, ignore_case=True)
s3 = jp.cityname2prefecture(
             pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
             ascii=True, ignore_case=True)
s4 = jp.cityname2prefecture(
             pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
             ascii=True, ignore_case=True)
s5 = pd.Series(['Kyoto', 'Osaka'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == True )

assert ( jp.validate_city('京都市')
         == jp.validate_city('Kyoto-shi')
         == True )

assert ( jp.validate_city('KYOTO-SHI')
         == jp.validate_city('kyoto-shi')
         == False )

assert ( jp.validate_city('京都市', ignore_case=True)
         == jp.validate_city('Kyoto-shi', ignore_case=True)
         == jp.validate_city('KYOTO-SHI', ignore_case=True)
         == jp.validate_city('kyoto-shi', ignore_case=True)
         == True )

assert ( jp.validate_city('京都県')
         == jp.validate_city('都京市')
         == jp.validate_city('Kyoto')
         == jp.validate_city('kyotoshi')
         == False )

assert ( jp.validate_city(
            ['京都市北区',
             '京都市左京区',
              '京都市右京区'])
         == jp.validate_city(
             ['Kyoto-shi Kita-ku',
              'Kyoto-shi Sakyo-ku',
              'Kyoto-shi Ukyo-ku'] )
         == [True, True, True] )

assert ( jp.validate_city(
             ['KYOTO-SHI KITA-KU',
              'KYOTO-SHI SAKYO-KU',
              'KYOTO-SHI UKYO-KU'] )
         == jp.validate_city(
             ['kyoto-shi kita-ku',
              'kyoto-shi sakyo-ku',
              'kyoto-shi ukyo-ku'] )
         == [False, False, False] )

assert ( jp.validate_city(
            ['京都市北区',
             '京都市左京区',
              '京都市右京区'], ignore_case=True)
         == jp.validate_city(
             ['Kyoto-shi Kita-ku',
              'Kyoto-shi Sakyo-ku',
              'Kyoto-shi Ukyo-ku'], ignore_case=True )
         == jp.validate_city(
             ['KYOTO-SHI KITA-KU',
              'KYOTO-SHI SAKYO-KU',
              'KYOTO-SHI UKYO-KU'], ignore_case=True )
         == jp.validate_city(
             ['kyoto-shi kita-ku',
              'kyoto-shi sakyo-ku',
              'kyoto-shi ukyo-ku'], ignore_case=True )
         == [True, True, True] )

assert ( jp.validate_city(['京都県', '大阪府', '奈良県'])
         == jp.validate_city(['都京', '大阪', '奈良'])
         == jp.validate_city(['Kyoto', 'OSAKA', 'NARA'])
         == jp.validate_city(['kyotofu', 'osaka', 'nara'])
         == [False, False, False] )

s1 = jp.validate_city(pd.Series(
         ['京都市北区',
          '京都市左京区',
          '京都市右京区']))
s2 = jp.validate_city( pd.Series(
         ['Kyoto-shi Kita-ku',
          'Kyoto-shi Sakyo-ku',
          'Kyoto-shi Ukyo-ku'] ))
s3 = pd.Series([True, True, True])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.validate_city(pd.Series(['京都県', '大阪府', '奈良県']))
s2 = pd.Series([False, False, False])
assert ( s1.equals(s2)
         == True )

s1 = jp.validate_city(
             pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
s2 = jp.validate_city(
             pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
s3 = pd.Series([False, False])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == True )

s1 = jp.validate_city(
             pd.Series(['京都市北区', '大阪市中央区']),
             ignore_case=True)
s2 = jp.validate_city(
             pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
             ignore_case=True)
s3 = jp.validate_city(
             pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
             ignore_case=True)
s4 = jp.validate_city(
             pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
             ignore_case=True)
s5 = pd.Series([True, True] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == True )

assert ( jp.cityname2geodetic('京都市')
         == jp.cityname2geodetic('Kyoto-shi')
         == (35.0117,135.452 ) )

assert ( jp.cityname2geodetic(['京都市', '大阪市'])
         == jp.cityname2geodetic(['Kyoto-shi','Osaka-shi'])
         == [(35.0117,135.452),(34.4138,135.3808)] )

d1 = jp.cityname2geodetic(pd.Series(['京都市', '大阪市']))
d2 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                    ['大阪市', 34.4138,135.3808]],
                  columns=['cityName', 'latitude', 'longitude'])
check = pd.concat([d1,d2]).drop_duplicates(keep=False)
assert ( len(check) == 0 )

d3 = jp.cityname2geodetic(pd.Series(['Kyoto-shi', 'Osaka-shi']))
d4 = pd.DataFrame([['Kyoto-shi', 35.0117,135.452],
                   ['Osaka-shi', 34.4138,135.3808]],
                  columns=['cityName', 'latitude', 'longitude'])
check = pd.concat([d3,d4]).drop_duplicates(keep=False)
assert ( len(check) == 0 )

assert ( jp.citycode2geodetic(26100) == (35.0117,135.452) )
assert ( jp.citycode2geodetic("26100") == (35.0117,135.452) )
assert ( jp.citycode2geodetic(261009) == (35.0117,135.452) )
assert ( jp.citycode2geodetic("261009") == (35.0117,135.452) )

assert ( jp.citycode2geodetic([26100, 27100])
         == [(35.0117,135.452), (34.4138,135.3808)] )

assert ( jp.citycode2geodetic(["26100", "27100"])
         == [(35.0117,135.452), (34.4138,135.3808)] )

assert ( jp.citycode2geodetic([261009, 271004])
         == [(35.0117,135.452), (34.4138,135.3808)] )

assert ( jp.citycode2geodetic(["26100", "271004"])
         == [(35.0117,135.452), (34.4138,135.3808)] )

d1 = jp.citycode2geodetic(pd.Series([26100,27100]))
d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                    [27100, 34.4138,135.3808] ],
                  columns=['cityCode', 'latitude', 'longitude'])
check = pd.concat([d1,d2]).drop_duplicates(keep=False)
assert ( len(check) == 0 )

d1 = jp.citycode2geodetic(pd.Series([261009,271004]))
d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                    [27100, 34.4138,135.3808] ],
                  columns=['cityCode', 'latitude', 'longitude'])
check = pd.concat([d1,d2]).drop_duplicates(keep=False)
assert ( len(check) == 0 )

d1 = jp.citycode2geodetic(pd.Series(["26100","27100"]))
d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                    [27100, 34.4138,135.3808] ],
                  columns=['cityCode', 'latitude', 'longitude'])
check = pd.concat([d1,d2]).drop_duplicates(keep=False)
assert ( len(check) == 0 )

d1 = jp.citycode2geodetic(pd.Series(["261009","271004"]))
d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                    [27100, 34.4138,135.3808] ],
                  columns=['cityCode', 'latitude', 'longitude'])
check = pd.concat([d1,d2]).drop_duplicates(keep=False)
assert ( len(check) == 0 )


```

>Trivia
Kyoto, Osaka and Nara are the place where the emperor established their capitals.


## Regular Expression

`findcity()` and  `cityname2code()` allow to regexpression.

```python

from jp_prefecture.jp_cities import jp_cities as jp
import re

name=re.compile('.*長岡.*')
expect = ['長岡市', '長岡京市', '長岡郡本山町', '長岡郡大豊町']

result = jp.findcity(name)
assert ( result == expect )

name=re.compile('Kyoto.*')
expect = ['Kyoto-Shi',
          'Kyoto-Shi Kita-Ku',
          'Kyoto-Shi Kamigyo-Ku',
          'Kyoto-Shi Sakyo-Ku',
          'Kyoto-Shi Nakagyo-Ku',
          'Kyoto-Shi Higashiyama-Ku',
          'Kyoto-Shi Shimogyo-Ku',
          'Kyoto-Shi Minami-Ku',
          'Kyoto-Shi Ukyo-Ku',
          'Kyoto-Shi Fushimi-Ku',
          'Kyoto-Shi Yamashina-Ku',
          'Kyoto-Shi Nishikyo-Ku']

result = jp.findcity(name)
assert ( result == expect )

pattern = re.compile('.*町町')
expect = ['杵島郡大町町']
result = jp.findcity(pattern)
assert ( result == expect )

pattern = re.compile('.*町町')
expect = ['Kishima-gun Omachi-cho']
result = jp.findcity(pattern, ascii=True)
assert ( result == expect )

pattern=re.compile('.*長岡.*')
expect = [15202, 26209, 39341, 39344]
result = jp.cityname2code(pattern)
assert ( result == expect )

pattern=re.compile('Kyoto.*')
expect = [26100, 26101, 26102, 26103, 26104, 26105,
         26106, 26107, 26108, 26109, 26110, 26111]
result = jp.cityname2code(pattern)
assert ( result == expect )
```

## class JpNumberParser

- `kanji2number(val)`
- `number2kanji(val, style)`
- `parser_jpnumber(val)``

```python
n [1]: from jp_prefecture.jp_numbers import JpNumberParser

In [2]: jn = JpNumberParser()

In [3]: jn.number2kanji(87654)
Out[3]: JpNumber(number=87654, as_str='87654', as_kanji='八万七千六百五十四')

In [4]: jn.number2kanji(87654, style='arabic')
Out[4]: JpNumber(number=87654, as_str='87654', as_kanji='８７６５４')

In [5]: jn.number2kanji(87654, style='mix')
09:44:27.69 LOG:
09:44:27.78 .... count = 0
Out[5]: JpNumber(number=87654, as_str='87654', as_kanji='８万６５４')

In [6]: jn.number2kanji(87654, style='finance')
Out[6]: JpNumber(number=87654, as_str='87654', as_kanji='８７，６５４')

In [7]: jn.number2kanji(87654, style='daiji')
Out[7]: JpNumber(number=87654, as_str='87654', as_kanji='捌萬漆仟陸佰伍拾肆')

In [8]: jn.kanji2number('八万七千六百五十四')
Out[8]: JpNumber(number=87654, as_str='87654', as_kanji='八万七千六百五十四')

In [9]: jn.kanji2number('８７６５４')
Out[9]: JpNumber(number=87654, as_str='87654', as_kanji='８７６５４')

In [10]: jn.kanji2number('８７，６５４')
Out[10]: JpNumber(number=87654, as_str='87654', as_kanji='８７，６５４')

In [11]: jn.kanji2number('捌萬漆仟陸佰伍拾肆')
Out[11]: JpNumber(number=87654, as_str='87654', as_kanji='捌萬漆仟陸佰伍拾肆')

In [12]: jn.normalize_kanjinumber('京都府長岡京市天神２丁目１５-１３')
Out[12]: '京都府長岡京市天神二丁目十五-十三'
```


## Memory Usage

```
      jp_prefecture: 60.05 KB.
          jp_cities: 2919.74 KB.
jp_cities_with_town: 130071.29 KB.
     address parser: 15.07 KB.
```


## BONUS: simpledispatchmethod
As of python 3.8 [funtools.singledispatchmethod](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod) allows singledispatch on methods, class methods, and staticmethods.

For older python version, you can use as follows.

```python
from jp_prefecture.singledispatchmethod import singledispatchmethod

class Patchwork(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @singledispatchmethod
    def get(self, arg):
        return getattr(self, arg, None)

    @get.register(list)
    def _(self, arg):
        return [self.get(x) for x in arg]

if __name__ == '__main__':
    pw = Patchwork(a=1, b=2, c=3)
    print(pw.get('b'))
    print(pw.get(['a', 'c']))
```

See Also [StackOverflow](https://stackoverflow.com/questions/24601722/how-can-i-use-functools-singledispatch-with-instance-methods/)


##  BONUS: ImmutableDict
If you want to use immutable dictionary. try as follows.

```python
In [1]: from jp_prefecture.immutable_dict import ImmutableDict

In [2]: d = ImmutableDict({1: 'A', 2: 'B', 3: 'C'})

In [3]: d
Out[3]: {1: 'A', 2: 'B', 3: 'C'}

In [4]: d.pop(1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [5], in <cell line: 1>()
----> 1 d.pop(1)

File ~/Projects/GitHub/jp_prefecture/jp_prefecture/immutable_dict.py:10, in ImmutableDict.__getattribute__(self, attribute)
      8 def __getattribute__(self, attribute):
      9     if attribute in ('clear', 'update', 'pop', 'popitem', 'setdefault'):
---> 10         raise AttributeError("%r object has no attribute %r" % (type(self).__name__, attribute))
     11     return dict.__getattribute__(self, attribute)

AttributeError: 'ImmutableDict' object has no attribute 'pop'

In [5]:
```

## BONUS: checkdigit.validate_checkdigit, checkdigit.calc_cehckdigit

small utility to compute modulus 11 check digit.

```python
from jp_prefecture.checkdigit import validate_checkdigit, calc_checkdigit

# 26100 is CityCode of Kyoto City

assert validate_checkdigit(261009) == 26100

assert validate_checkdigit("261009") == "26100"

assert validate_checkdigit(261008) == None

assert validate_checkdigit("261008") == None

assert validate_checkdigit("2610", 5) == None

assert validate_checkdigit("2610", 5) == None

assert validate_checkdigit(261009, 5) == 26100

assert validate_checkdigit("261009", 5) == "26100"

assert ( validate_checkdigit(26100, 5) == 26100 )

assert ( validate_checkdigit(1100, 5) == 1100 )

assert ( validate_checkdigit("1100", 5) == "01100" )

assert calc_checkdigit(26100) == 261009

assert calc_checkdigit("26100") == "261009"

assert calc_checkdigit(26100, only_checkdigit=True) == 9

assert calc_checkdigit("26100", only_checkdigit=True) == "9"

assert validate_checkdigit(261009, weights=[6,5,4,3,2]) == 26100

assert calc_checkdigit("26100",  weights=[6,5,4,3,2]) == "261009"

# for ISDB10
assert( validate_checkdigit(4-900900672) == 490090067)
assert( validate_checkdigit("4-900900672") == "490090067")

# for ISDB13
assert( validate_checkdigit("978-4-906649-006") == "978490664900")
```

# Japanese address

```
Prefecture : ( '-To':'都', '-Dou': '道', '-Fu': '府',  '-Ken': '県' )
City: { '-Shi': '市' }
District: { '-Ku': '区' }
County: {'-Gun': '郡' }
Town: { '-Machi': '町',
        '-Cho': '町' }
Village: { '-Son': '村',
           '-Mura': '村' }
```


## The CityCode (JIS X 0402)
The CityCode consists of a five-digit number assigned to each local public entity (prefecture, municipality, etc.) in Japan, as well as to counties that are not solely local public entities but are used as statistical divisions, in accordance with certain rules.
Among the five-digit numbers The first two digits represent prefectures, numbered from north to south, from "01" (Hokkaido) to "47" (Okinawa).
The third digit indicates whether the area belongs to a city or a county. The third digit indicates whether the area belongs to a city or a county.
The last two digits are the number of the respective group represented by the third digit ("1": special wards, wards of ordinance-designated cities, "2": a group of cities, "3-": a group of counties, "4-": a group of towns and villages belonging to counties, "5-": a group of cities). 3-": counties and towns/villages within each county), and the last two digits are assigned to each city, county, town, or village according to the arrangement of the third digit. The arrangement of cities, counties, towns, and villages is fixed for each prefecture and ordinance-designated city. In most prefectures, cities are arranged in the order in which they were established, but in some cases, such as Wakayama Prefecture, cities are arranged from north to south regardless of the order in which they were established.
Thus, each city, county, town, village is represented by the third digit and the last two digits combined.
For example, Nagaokakyo City in Kyoto Prefecture is represented by the citycode "26209", of which the upper two digits "26" represent Kyoto Prefecture and the lower three digits The last 3-digit "209" represents Nagaokakyo City, which is the 9th city (10th if Kyoto City is included) in Kyoto Prefecture.
