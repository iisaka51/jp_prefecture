import os
os.environ.update({'JP_PREFECTURE_ENABLE_TOWN': '1'})
from jp_prefecture.address import JpAddressParser

addr=JpAddressParser()
data  = addr.parse_address('〒617-0824 長岡京市天神２丁目１５−１３')
print(data)
print(f'CityCode: {data.cityCode}')
print(f'Location: {data.geodetic}')
