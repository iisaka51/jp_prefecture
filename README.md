# jp_prefecture.
> Japan prefecture names and codes

Simple utility to convert the name of japanese prefectures.

- full_name from/to code (JIS X 0401-1973).
- short_name to full_name
- alphabet_name from/to full_name

Reference

- [JIS X 0401 JSON API](https://madefor.github.io/jisx0401/)

## Install

`pip install jp_prefecture`

## How to use

```python
from jp_prefecture import jp_prefectures as jp
```

### Conversion

```python
from jp_prefecture import jp_prefectures as jp

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

assert jp.code2name(26) == '京都府'

assert jp.code2name([26, 27, 29]) == ['京都府', '大阪府', '奈良県']

assert jp.code2alphabet(26) == 'Kyoto'

assert jp.code2alphabet([26, 27, 29]) == ['Kyoto', 'Osaka', 'Nara']

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
```
