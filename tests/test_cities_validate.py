import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as jp
import pandas as pd

class TestClass:
    def test_validate_city_true(self):
        assert ( jp.validate_city('京都市')
                 == jp.validate_city('Kyoto-shi')
                 == True )

    def test_validate_city_fail(self):
        assert ( jp.validate_city('KYOTO-SHI')
                 == jp.validate_city('kyoto-shi')
                 == False )

    def test_validate_city_ignore_case(self):
        assert ( jp.validate_city('京都市', ignore_case=True)
                 == jp.validate_city('Kyoto-shi', ignore_case=True)
                 == jp.validate_city('KYOTO-SHI', ignore_case=True)
                 == jp.validate_city('kyoto-shi', ignore_case=True)
                 == True )

    def test_validate_city_false(self):
        assert ( jp.validate_city('京都県')
                 == jp.validate_city('都京市')
                 == jp.validate_city('Kyoto')
                 == jp.validate_city('kyotoshi')
                 == False )

    def test_validate_city_list(self):
        assert ( jp.validate_city(
                    ['京都市北区',
                     '京都市左京区',
                      '京都市右京区'])
                 == jp.validate_city(
                     ['Kyoto-shi Kita-ku',
                      'Kyoto-shi Sakyo-ku',
                      'Kyoto-shi Ukyo-ku'] )
                 == [True, True, True] )

    def test_validate_city_list_fail(self):
        assert ( jp.validate_city(
                     ['KYOTO-SHI KITA-KU',
                      'KYOTO-SHI SAKYO-KU',
                      'KYOTO-SHI UKYO-KU'] )
                 == jp.validate_city(
                     ['kyoto-shi kita-ku',
                      'kyoto-shi sakyo-ku',
                      'kyoto-shi ukyo-ku'] )
                 == [False, False, False] )

    def test_validate_city_list_ignore_case(self):
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

    def test_validate_city_list_false(self):
        assert ( jp.validate_city(['京都県', '大阪府', '奈良県'])
                 == jp.validate_city(['都京', '大阪', '奈良'])
                 == jp.validate_city(['Kyoto', 'OSAKA', 'NARA'])
                 == jp.validate_city(['kyotofu', 'osaka', 'nara'])
                 == [False, False, False] )

    def test_validate_city_series(self):
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

    def test_validate_city_series_false(self):
        s1 = jp.validate_city(pd.Series(['京都県', '大阪府', '奈良県']))
        s2 = pd.Series([False, False, False])
        assert ( s1.equals(s2)
                 == True )

    def test_validate_city_series_fail(self):
        s1 = jp.validate_city(
                     pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
        s2 = jp.validate_city(
                     pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
        s3 = pd.Series([False, False])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_validate_city_series_ignore_case(self):
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
