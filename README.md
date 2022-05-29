# jp_prefecture.
> Japan prefecture names and codes

Simple utility to convert the name of japanese prefectures.

- full_name from/to code (JIS X 0401-1973).
- short_name to full_name
- alphabet_name from/to full_name
- support lists and pandas serires as input.

Reference

- [JIS X 0401 JSON API](https://madefor.github.io/jisx0401/)

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

assert jp.code2name([26, 27, 29]) == ['京都府', '大阪府', '奈良県']

s1 = jp.code2name(pd.Series([26, 27, 29]))
s2 = pd.Series(['京都府', '大阪府', '奈良県'])
assert s1.equals(s2) == True

assert jp.code2alphabet(26) == 'Kyoto'

assert jp.code2alphabet([26, 27, 29]) == ['Kyoto', 'Osaka', 'Nara']

s1 = jp.code2alphabet(pd.Series([26, 27, 29]))
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
```



### BONUS

Here's simple example for type dispatch in class method.

```python
from jp_prefecture.methoddispatch  import methoddispatch

class Patchwork(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @methoddispatch
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

```python
>>> pw = Patchwork(a=1, b=2, c=3)
>>> pw.get("b")
2
>>> pw.get(["a", "c"])
[1, 3]
```

See Also: [StackOverflow](https://stackoverflow.com/questions/24601722/how-can-i-use-functools-singledispatch-with-instance-methods).

