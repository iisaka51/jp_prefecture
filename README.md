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
assert ( jp.name2code("京都府")
         == jp.name2code("京都")
         == jp.name2code("Kyoto")
         == jp.name2code("KYOTO")
         == jp.name2code("kyoto")
         == 26 )

assert jp.code2name(26) == "京都府"

assert jp.name2alphabet("京都府") == "Kyoto"

assert ( jp.alphabet2name("Kyoto")
         == jp.name2code("KYOTO")
         == jp.name2code("kyoto")
         == "京都府" )

```
