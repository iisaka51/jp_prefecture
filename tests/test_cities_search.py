import sys
sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as jp
import re
import pandas as pd

class TestClass:
    def test_find_city_kanji(self):
        name=re.compile('.*長岡.*')
        expect = ['長岡市', '長岡京市', '長岡郡本山町', '長岡郡大豊町']

        result = jp.findcity(name)
        assert ( result == expect )

    def test_find_city_alhabet(self):
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

    def test_cityname2code_kanji(self):
        name=re.compile('.*長岡.*')
        expect = [15202, 26209, 39341, 39344]

        result = jp.cityname2code(name)
        assert ( result == expect )

    def test_cityname2code_alphabet(self):
        name=re.compile('Kyoto.*')
        expect = [26100, 26101, 26102, 26103, 26104, 26105,
                 26106, 26107, 26108, 26109, 26110, 26111]

        result = jp.cityname2code(name)
        assert ( result == expect )

