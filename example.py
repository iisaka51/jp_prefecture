from jp_prefecture.address import JpAddressParser

addr=JpAddressParser()
data  = addr.parse_address('〒617-0824 長岡京市天神２丁目１５−１３')
data
data.cityCode
data.geodetic
