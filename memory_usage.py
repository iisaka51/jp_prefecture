from jp_prefecture import jp_prefectures as jp
from jp_prefecture.jp_cities import jp_cities as city

from pympler import asizeof

print('Using Memory:')
print(f"""
jp_prefecture: {asizeof.asizeof(jp)/1024} KB.
    jp_cities: {asizeof.asizeof(city)/1024} KB.
""")
