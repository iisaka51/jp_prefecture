import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as city
import pandas as pd

class TestClass:
    def test_name2citycode(self):
        assert ( city.name2citycode('京都市')
                 == 26100 )

    def test_name2citycode_with_checkdigit(self):
        assert ( city.name2citycode('京都市', with_checkdigit=True)
                 == 261009 )

    def test_name2citycode_list(self):
        assert ( city.name2citycode(['京都市北区', '京都市左京区', '京都市右京区'])
                 == [26101, 26103, 26108] )

    def test_name2citycode_series(self):
        s1 = city.name2citycode( pd.Series(
                     ['京都市北区', '京都市左京区', '京都市右京区']))
        s2 = pd.Series([26101, 26103, 26108])
        assert ( s1.equals(s2) == True )

    def test_name2prefcode(self):
        assert ( city.name2prefcode('京都市')
                 == 26 )

    def test_name2prefcode_list(self):
        assert ( city.name2prefcode(['京都市北区', '大阪市中央区'])
                 == [26, 27] )

    def test_name2prefecture(self):
        assert ( city.name2prefecture('京都市')
                 == '京都府' )

    def test_name2prefecture_list(self):
        assert ( city.name2prefecture(['京都市北区', '大阪市中央区'])
                 == ['京都府', '大阪府'] )

    def test_name2prefcode_series(self):
        s1 = city.name2prefcode(pd.Series(['京都市北区', '大阪市中央区']))
        s2 = pd.Series([26, 27])
        assert ( s1.equals(s2) == True )

    def test_citycode2name(self):
        assert city.citycode2name(26100) == '京都市'

    def test_citycode2name_as_str(self):
        assert city.citycode2name("26100") == '京都市'

    def test_citycode2name_with_checkdigit(self):
        assert city.citycode2name(261009) == '京都市'

    def test_citycode2name_as_str_with_checkdigit(self):
        assert city.citycode2name("261009") == '京都市'

    def test_citycode2name_list(self):
        assert ( city.citycode2name([26101, 26103, 26108])
                 ==  ['京都市北区', '京都市左京区', '京都市右京区'] )

    def test_citycode2name_series(self):
        s1 = city.citycode2name(pd.Series([26101, 26103, 26108]))
        s2 = pd.Series( ['京都市北区', '京都市左京区', '京都市右京区'] )
        assert s1.equals(s2) == True

    def test_validator_true(self):
        assert ( city.validator('京都市')
                 == True )

    def test_validator_false(self):
        assert ( city.validator('京都県')
                 == city.validator('都京市')
                 == city.validator('KyOto')
                 == city.validator('KYoTO')
                 == city.validator('kyotoshi')
                 == False )

    def test_validator_list(self):
        assert ( city.validator(['京都市北区', '京都市左京区', '京都市右京区'])
                 == [True, True, True] )

    def test_validator_list_false(self):
        assert ( city.validator(['京都県', '大阪府', '奈良県'])
                 == city.validator(['都京', '大阪', '奈良'])
                 == city.validator(['KyOto', 'Osaka', 'Nara'])
                 == city.validator(['KYoTO', 'OSAKA', 'NARA'])
                 == city.validator(['kyotofu', 'osaka', 'nara'])
                 == [False, False, False] )

    def test_validator_series(self):
        s1 = city.validator(pd.Series(
                 ['京都市北区', '京都市左京区', '京都市右京区']))
        s2 = pd.Series([True, True, True])
        assert ( s1.equals(s2)
                 == True )

    def test_validator_series_false(self):
        s1 = city.validator(pd.Series(['京都県', '大阪府', '奈良県']))
        s2 = pd.Series([False, False, False])
        assert ( s1.equals(s2)
                 == True )

