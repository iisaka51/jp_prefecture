import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as jp
import pandas as pd

class TestClass:
    def test_name2citycode(self):
        assert ( jp.name2citycode('京都市')
                 == 26100 )

    def test_name2citycode_with_checkdigit(self):
        assert ( jp.name2citycode('京都市', with_checkdigit=True)
                 == 261009 )

    def test_name2citycode_list(self):
        assert ( jp.name2citycode(
                    ['京都市北区', '京都市左京区', '京都市右京区'])
                 == [26101, 26103, 26108] )

    def test_name2citycode_series(self):
        s1 = jp.name2citycode( pd.Series(
                     ['京都市北区', '京都市左京区', '京都市右京区']))
        s2 = pd.Series([26101, 26103, 26108])
        assert ( s1.equals(s2) == True )

    def test_name2prefcode(self):
        assert ( jp.name2prefcode('京都市')
                 == 26 )

    def test_name2prefcode_list(self):
        assert ( jp.name2prefcode(['京都市北区', '大阪市中央区'])
                 == [26, 27] )

    def test_name2prefcode_series(self):
        s1 = jp.name2prefcode(pd.Series(['京都市北区', '大阪市中央区']))
        s2 = pd.Series([26, 27])
        assert ( s1.equals(s2) == True )

    def test_name2prefecture(self):
        assert ( jp.name2prefecture('京都市')
                 == '京都府' )

    def test_name2prefecture_list(self):
        assert ( jp.name2prefecture(['京都市北区', '大阪市中央区'])
                 == ['京都府', '大阪府'] )

    def test_name2prefecture_series(self):
        s1 = jp.name2prefecture(pd.Series(['京都市北区', '大阪市中央区']))
        s2 = pd.Series(['京都府', '大阪府'] )
        assert ( s1.equals(s2) == True )

    def test_citycode2name(self):
        assert jp.citycode2name(26100) == '京都市'

    def test_citycode2name_as_str(self):
        assert jp.citycode2name("26100") == '京都市'

    def test_citycode2name_with_checkdigit(self):
        assert jp.citycode2name(261009) == '京都市'

    def test_citycode2name_as_str_with_checkdigit(self):
        assert jp.citycode2name("261009") == '京都市'

    def test_citycode2name_list(self):
        assert ( jp.citycode2name([26101, 26103, 26108])
                 ==  ['京都市北区', '京都市左京区', '京都市右京区'] )

    def test_citycode2name_series(self):
        s1 = jp.citycode2name(pd.Series([26101, 26103, 26108]))
        s2 = pd.Series( ['京都市北区', '京都市左京区', '京都市右京区'] )
        assert s1.equals(s2) == True

    def test_validate_city_true(self):
        assert ( jp.validate_city('京都市')
                 == True )

    def test_validate_city_false(self):
        assert ( jp.validate_city('京都県')
                 == jp.validate_city('都京市')
                 == jp.validate_city('KyOto')
                 == jp.validate_city('KYoTO')
                 == jp.validate_city('kyotoshi')
                 == False )

    def test_validate_city_list(self):
        assert ( jp.validate_city(
                    ['京都市北区', '京都市左京区', '京都市右京区'])
                 == [True, True, True] )

    def test_validate_city_list_false(self):
        assert ( jp.validate_city(['京都県', '大阪府', '奈良県'])
                 == jp.validate_city(['都京', '大阪', '奈良'])
                 == jp.validate_city(['KyOto', 'Osaka', 'Nara'])
                 == jp.validate_city(['KYoTO', 'OSAKA', 'NARA'])
                 == jp.validate_city(['kyotofu', 'osaka', 'nara'])
                 == [False, False, False] )

    def test_validate_city_series(self):
        s1 = jp.validate_city(pd.Series(
                 ['京都市北区', '京都市左京区', '京都市右京区']))
        s2 = pd.Series([True, True, True])
        assert ( s1.equals(s2)
                 == True )

    def test_validate_city_series_false(self):
        s1 = jp.validate_city(pd.Series(['京都県', '大阪府', '奈良県']))
        s2 = pd.Series([False, False, False])
        assert ( s1.equals(s2)
                 == True )

