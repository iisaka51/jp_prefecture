import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as jp
import pandas as pd

class TestClass:
    def test_cityname2geodetic(self):
        assert ( jp.cityname2geodetic('京都市')
                 == jp.cityname2geodetic('Kyoto-shi')
                 == (35.0117,135.452 ) )

    def test_cityname2geodetic_list(self):
        assert ( jp.cityname2geodetic(['京都市', '大阪市'])
                 == jp.cityname2geodetic(['Kyoto-shi','Osaka-shi'])
                 == [(35.0117,135.452),(34.4138,135.3808)] )

    def test_cityname2geodetic_series(self):
        d1 = jp.cityname2geodetic(pd.Series(['京都市', '大阪市']))
        d2 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        check = pd.concat([d1,d2]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )

        d3 = jp.cityname2geodetic(pd.Series(['Kyoto-shi', 'Osaka-shi']))
        d4 = pd.DataFrame([['Kyoto-shi', 35.0117,135.452],
                           ['Osaka-shi', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        check = pd.concat([d3,d4]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )

    def test_citycode2geodetic_int(self):
        assert ( jp.citycode2geodetic(26100) == (35.0117,135.452) )

    def test_citycode2geodetic_str(self):
        assert ( jp.citycode2geodetic("26100") == (35.0117,135.452) )

    def test_citycode2geodetic_int_with_checkdegits(self):
        assert ( jp.citycode2geodetic(261009) == (35.0117,135.452) )

    def test_citycode2geodetic_str(self):
        assert ( jp.citycode2geodetic("261009") == (35.0117,135.452) )

    def test_citycode2geodetic_int_list(self):
        assert ( jp.citycode2geodetic([26100, 27100])
                 == [(35.0117,135.452), (34.4138,135.3808)] )

    def test_citycode2geodetic_str_list(self):
        assert ( jp.citycode2geodetic(["26100", "27100"])
                 == [(35.0117,135.452), (34.4138,135.3808)] )

    def test_citycode2geodetic_int_with_checkdigit_list(self):
        assert ( jp.citycode2geodetic([261009, 271004])
                 == [(35.0117,135.452), (34.4138,135.3808)] )

    def test_citycode2geodetic_str_with_checkdigit_list(self):
        assert ( jp.citycode2geodetic(["26100", "271004"])
                 == [(35.0117,135.452), (34.4138,135.3808)] )

    def test_citycode2geodetic_int_series(self):
        d1 = jp.citycode2geodetic(pd.Series([26100,27100]))
        d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                            [27100, 34.4138,135.3808] ],
                          columns=['cityCode', 'latitude', 'longitude'])
        check = pd.concat([d1,d2]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )

    def test_citycode2geodetic_int_with_checkdigit_series(self):
        d1 = jp.citycode2geodetic(pd.Series([261009,271004]))
        d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                            [27100, 34.4138,135.3808] ],
                          columns=['cityCode', 'latitude', 'longitude'])
        check = pd.concat([d1,d2]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )

    def test_citycode2geodetic_str_series(self):
        d1 = jp.citycode2geodetic(pd.Series(["26100","27100"]))
        d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                            [27100, 34.4138,135.3808] ],
                          columns=['cityCode', 'latitude', 'longitude'])
        check = pd.concat([d1,d2]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )

    def test_citycode2geodetic_str_with_checkdigit_series(self):
        d1 = jp.citycode2geodetic(pd.Series(["261009","271004"]))
        d2 = pd.DataFrame([ [26100, 35.0117,135.452],
                            [27100, 34.4138,135.3808] ],
                          columns=['cityCode', 'latitude', 'longitude'])
        check = pd.concat([d1,d2]).drop_duplicates(keep=False)
        assert ( len(check) == 0 )


