# jp_prefecture.
> Japan prefecture and city names and codes

Simple utility to convert the name of japanese prefectures.

- full_name from/to code (JIS X 0401-1973, JIX X 0402).
- short_name to full_name
- alphabet_name from/to full_name
- validator for full_name and short_name, alphabet_name.
- allow code as str or int.
- support lists and pandas serires as input.
- support checkdigits for citycode.

currently alphabet_name and short_name only works for prefectures.

Reference

- https://www.soumu.go.jp/denshijiti/code.html (in japanese)

## Install

`pip install jp_prefecture`

## How to use

```python
from jp_prefecture import jp_prefectures as jp
```

### Dataframe of jp.prefectures

```python
>>> from jp_prefecture import jp_prefectures as jp
>>> jp.prefectures
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
>>> jp.prefectures.info()
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
>>>
```

## Dataframe of Cities

```python

In [6]: city.cities
Out[6]:
      prefCode  cityCode cityName  bigCityFlag
0            1      1100      札幌市            2
1            1      1101   札幌市中央区            1
2            1      1102    札幌市北区            1
3            1      1103    札幌市東区            1
4            1      1104   札幌市白石区            1
...        ...       ...      ...          ...
1917        47     47361     久米島町            0
1918        47     47362     八重瀬町            0
1919        47     47375     多良間村            0
1920        47     47381      竹富町            0
1921        47     47382     与那国町            0

In [7]: city.cities.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1922 entries, 0 to 1921
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   prefCode     1922 non-null   int64
 1   cityCode     1922 non-null   int64
 2   cityName     1922 non-null   object
 3   bigCityFlag  1922 non-null   int64
dtypes: int64(3), object(1)
memory usage: 75.1+ KB

In [8]:
```

### Conversion

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

assert jp.code2name([26, 27, 29]) == ['京都府', '大阪府', '奈良県']
assert jp.code2name(["26", "27", "29"]) == ['京都府', '大阪府', '奈良県']

s1 = jp.code2name(pd.Series([26, 27, 29]))
s2 = pd.Series(['京都府', '大阪府', '奈良県'])
assert s1.equals(s2) == True

assert jp.code2alphabet(26) == 'Kyoto'

assert jp.code2alphabet([26, 27, 29]) == ['Kyoto', 'Osaka', 'Nara']

s1 = jp.code2alphabet(pd.Series([26, 27, 29]))
s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert s1.equals(s2) == True

s1 = jp.code2alphabet(pd.Series(["26", "27", "29"]))
s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert s1.equals(s2) == True

assert ( jp.name2alphabet('京都府')
         == jp.name2alphabet('京都')
         == jp.name2alphabet('Kyoto')
         == jp.name2alphabet('KYOTO')
         == jp.name2alphabet('kyoto')
         == 'Kyoto' )

assert ( jp.name2alphabet(['京都府', '大阪府', '奈良県'])
         == jp.name2alphabet(['京都', '大阪', '奈良'])
         == jp.name2alphabet(['Kyoto', 'Osaka', 'Nara'])
         == jp.name2alphabet(['KYOTO', 'OSAKA', 'NARA'])
         == jp.name2alphabet(['kyoto', 'osaka', 'nara'])
         == ['Kyoto', 'Osaka', 'Nara'] )

s1 = jp.name2alphabet(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.name2alphabet(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.name2alphabet(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.name2alphabet(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.name2alphabet(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

assert ( jp.alphabet2name('Kyoto')
         == jp.alphabet2name('KYOTO')
         == jp.alphabet2name('kyoto')
         == jp.alphabet2name('京都府')
         == jp.alphabet2name('京都')
         == '京都府' )

assert ( jp.alphabet2name(['京都府', '大阪府', '奈良県'])
         == jp.alphabet2name(['京都', '大阪', '奈良'])
         == jp.alphabet2name(['Kyoto', 'Osaka', 'Nara'])
         == jp.alphabet2name(['KYOTO', 'OSAKA', 'NARA'])
         == jp.alphabet2name(['kyoto', 'osaka', 'nara'])
         == ['京都府', '大阪府', '奈良県'] )

s1 = jp.alphabet2name(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.alphabet2name(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.alphabet2name(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.alphabet2name(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.alphabet2name(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series(['京都府', '大阪府', '奈良県'] )
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )

assert ( jp.validator('京都府')
         == jp.validator('京都')
         == jp.validator('Kyoto')
         == jp.validator('KYOTO')
         == jp.validator('kyoto')
         == True )

assert ( jp.validator('京都県')
         == jp.validator('都京')
         == jp.validator('KyOto')
         == jp.validator('KYoTO')
         == jp.validator('kyotofu')
         == False )

assert ( jp.validator(['京都府', '大阪府', '奈良県'])
         == jp.validator(['京都', '大阪', '奈良'])
         == jp.validator(['Kyoto', 'Osaka', 'Nara'])
         == jp.validator(['KYOTO', 'OSAKA', 'NARA'])
         == jp.validator(['kyoto', 'osaka', 'nara'])
         == [True, True, True] )

s1 = jp.validator(pd.Series(['京都府', '大阪府', '奈良県']))
s2 = jp.validator(pd.Series(['京都', '大阪', '奈良']))
s3 = jp.validator(pd.Series(['Kyoto', 'Osaka', 'Nara']))
s4 = jp.validator(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
s5 = jp.validator(pd.Series(['kyoto', 'osaka', 'nara']))
s6 = pd.Series([True, True, True])
assert ( s1.equals(s2)
         == s2.equals(s3)
         == s3.equals(s4)
         == s4.equals(s5)
         == s5.equals(s6)
         == True )
```


```python
from jp_prefecture.jp_cities import jp_cities as city
import pandas as pd

assert city.name2code('京都市') == 26100
assert city.name2code('京都市', with_checkdigit=True) == 261009

assert ( city.name2code(['京都市北区', '京都市左京区', '京都市右京区'])
         == [26101, 26103, 26108] )

s1 = city.name2code( pd.Series(
             ['京都市北区', '京都市左京区', '京都市右京区']))
s2 = pd.Series([26101, 26103, 26108])
assert ( s1.equals(s2) == True )

assert city.code2name(26100) == '京都市'
assert city.code2name("26100") == '京都市'
assert city.code2name(261009) == '京都市'
assert city.code2name("261009") == '京都市'

assert ( city.code2name([26101, 26103, 26108])
         ==  ['京都市北区', '京都市左京区', '京都市右京区'] )

s1 = city.code2name(pd.Series([26101, 26103, 26108]))
s2 = pd.Series( ['京都市北区', '京都市左京区', '京都市右京区'] )
assert s1.equals(s2) == True

assert city.validator('京都市') == True

assert ( city.validator('京都県')
         == city.validator('都京市')
         == city.validator('KyOto')
         == city.validator('KYoTO')
         == city.validator('kyotoshi')
         == False )

assert ( city.validator(['京都市北区', '京都市左京区', '京都市右京区'])
         == [True, True, True] )

assert ( city.validator(['京都県', '大阪府', '奈良県'])
         == city.validator(['都京', '大阪', '奈良'])
         == city.validator(['KyOto', 'Osaka', 'Nara'])
         == city.validator(['KYoTO', 'OSAKA', 'NARA'])
         == city.validator(['kyotofu', 'osaka', 'nara'])
         == [False, False, False] )

s1 = city.validator(pd.Series(
         ['京都市北区', '京都市左京区', '京都市右京区']))
s2 = pd.Series([True, True, True])
assert s1.equals(s2) == True

s1 = city.validator(pd.Series(['京都県', '大阪府', '奈良県']))
s2 = pd.Series([False, False, False])
assert s1.equals(s2) == True
```

>Trivia
Kyoto, Osaka and Nara are the place where the emperor established their capitals.

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

assert calc_checkdigit(26100) == 261009

assert calc_checkdigit("26100") == "261009"

assert calc_checkdigit(26100, only_checkdigit=True) == 9

assert calc_checkdigit("26100", only_checkdigit=True) == "9"

assert validate_checkdigit(261009, weights=[6,5,4,3,2]) == 26100

assert calc_checkdigit("26100",  weights=[6,5,4,3,2]) == "261009"
```


## The CityCode Number (JIS X 0402)
The CityCode number consists of a five-digit number assigned to each local public entity (prefecture, municipality, etc.) in Japan, as well as to counties that are not solely local public entities but are used as statistical divisions, in accordance with certain rules.
Among the five-digit numbers The first two digits represent prefectures, numbered from north to south, from "01" (Hokkaido) to "47" (Okinawa).
The third digit indicates whether the area belongs to a city or a county. The third digit indicates whether the area belongs to a city or a county. The last two digits are 3-digit numbers.
The last two digits are the number of the respective group represented by the third digit ("1": special wards, wards of ordinance-designated cities, "2": a group of cities, "3-": a group of counties, "4-": a group of towns and villages belonging to counties, "5-": a group of cities). 3-": counties and towns/villages within each county), and the last two digits are assigned to each city, county, town, or village according to the arrangement of the third digit. The arrangement of cities, counties, towns, and villages is fixed for each prefecture and ordinance-designated city. In most prefectures, cities are arranged in the order in which they were established, but in some cases, such as Wakayama Prefecture, cities are arranged from north to south regardless of the order in which they were established.
Thus, each city, county, town, village is represented by the third digit and the last two digits combined.
For example, Nagaokakyo City in Kyoto Prefecture is represented by the citycode number "26209", of which the upper two digits "26" represent Kyoto Prefecture and the lower three digits The last 3-digit "209" represents Nagaokakyo City, which is the 9th city (10th if Kyoto City is included) in Kyoto Prefecture.

