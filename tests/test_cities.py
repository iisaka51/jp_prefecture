import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.jp_cities import jp_cities as jp
import pandas as pd

class TestClass:
    def test_cityname2code(self):
        assert ( jp.cityname2code('京都市')
                 == jp.cityname2code('Kyoto-shi')
                 == 26100 )

    def test_cityname2code_fail(self):
        assert ( jp.cityname2code('KYOTO-SHI')
                 == jp.cityname2code('kyoto-shi')
                 == None )

    def test_cityname2code_ignore_case(self):
        assert ( jp.cityname2code('京都市', ignore_case=True)
                 == jp.cityname2code('Kyoto-shi', ignore_case=True)
                 == jp.cityname2code('KYOTO-SHI', ignore_case=True)
                 == jp.cityname2code('kyoto-shi', ignore_case=True)
                 == 26100 )

    def test_cityname2code_checkdigit(self):
        assert ( jp.cityname2code('京都市', checkdigit=True)
                 == jp.cityname2code('Kyoto-shi', checkdigit=True)
                 == 261009 )

    def test_cityname2code_list(self):
        assert ( jp.cityname2code(
                    ['京都市北区', '京都市左京区', '京都市右京区'])
                 == jp.cityname2code(
                        ['Kyoto-shi Kita-ku',
                         'Kyoto-shi Sakyo-ku',
                         'Kyoto-shi Ukyo-ku'] )
                 == [26101, 26103, 26108] )

    def test_cityname2code_list_fail(self):
        assert ( jp.cityname2code(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU'] )
                 == jp.cityname2code(
                        ['kyoto-shi kita-ku',
                         'kyoto-shi sakyo-ku',
                         'kyoto-shi ukyo-ku'] )
                 == [None, None, None] )

    def test_cityname2code_list_ignore_case(self):
        assert ( jp.cityname2code(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU'], ignore_case=True )
                 == jp.cityname2code(
                        ['kyoto-shi kita-ku',
                         'kyoto-shi sakyo-ku',
                         'kyoto-shi ukyo-ku'], ignore_case=True )
                 == [26101, 26103, 26108] )

    def test_cityname2code_series(self):
        s1 = jp.cityname2code( pd.Series(
                     ['京都市北区', '京都市左京区', '京都市右京区']))
        s2 = jp.cityname2code( pd.Series(
                        ['Kyoto-shi Kita-ku',
                         'Kyoto-shi Sakyo-ku',
                         'Kyoto-shi Ukyo-ku'] ))
        s3 = pd.Series([26101, 26103, 26108])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2code_series_fail(self):
        s1 = jp.cityname2code( pd.Series(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU'] ))
        s2 = jp.cityname2code( pd.Series(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU'] ))
        s3 = pd.Series([None, None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2code_series_ignore_case(self):
        s1 = jp.cityname2code( pd.Series(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU']), ignore_case=True )
        s2 = jp.cityname2code( pd.Series(
                        ['KYOTO-SHI KITA-KU',
                         'KYOTO-SHI SAKYO-KU',
                         'KYOTO-SHI UKYO-KU']), ignore_case=True )
        s3 = pd.Series([26101, 26103, 26108])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize(self):
        assert ( jp.cityname2normalize('京都市')
                 == jp.cityname2normalize('Kyoto-shi')
                 == '京都市')

    def test_cityname2normalize_fail(self):
        assert ( jp.cityname2normalize('KYOTO-SHI')
                 == jp.cityname2normalize('kyoto-shi')
                 == None )

    def test_cityname2normalize_ignore_case(self):
        assert ( jp.cityname2normalize('京都市')
                 == jp.cityname2normalize('KYOTO-SHI', ignore_case=True)
                 == jp.cityname2normalize('kyoto-shi', ignore_case=True)
                 == '京都市')

    def test_cityname2normalize_list(self):
        assert ( jp.cityname2normalize(
                    ['京都市北区',
                     '京都市左京区',
                     '京都市右京区'])
                 == jp.cityname2normalize(
                    ['Kyoto-shi Kita-ku',
                     'Kyoto-shi Sakyo-ku',
                     'Kyoto-shi Ukyo-ku'] )
                 == ['京都市北区',
                     '京都市左京区',
                     '京都市右京区'])

    def test_cityname2normalize_list_fail(self):
        assert ( jp.cityname2normalize(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU'] )
                 == jp.cityname2normalize(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku'] )
                 == [None, None, None] )

    def test_cityname2normalize_list_ignore_case(self):
        assert ( jp.cityname2normalize(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU'], ignore_case=True )
                 == jp.cityname2normalize(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku'], ignore_case=True)
                 == ['京都市北区',
                     '京都市左京区',
                     '京都市右京区'])

    def test_cityname2normalize_series(self):
        s1 = jp.cityname2normalize( pd.Series(
                         ['京都市北区',
                          '京都市左京区',
                           '京都市右京区']))
        s2 = jp.cityname2normalize( pd.Series(
                         ['Kyoto-shi Kita-ku',
                          'Kyoto-shi Sakyo-ku',
                          'Kyoto-shi Ukyo-ku'] ))
        s3 = pd.Series( ['京都市北区',
                         '京都市左京区',
                         '京都市右京区'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize_series_fail(self):
        s1 = jp.cityname2normalize( pd.Series(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU'] ))
        s2 = jp.cityname2normalize( pd.Series(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku'] ))
        s3 = pd.Series( [None, None, None] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize_series_fail(self):
        s1 = jp.cityname2normalize( pd.Series(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU']), ignore_case=True )
        s2 = jp.cityname2normalize( pd.Series(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku']), ignore_case=True)
        s3 = pd.Series( ['京都市北区',
                         '京都市左京区',
                         '京都市右京区'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize_ascii(self):
        assert ( jp.cityname2normalize('京都市',ascii=True)
                 == jp.cityname2normalize('Kyoto-shi',ascii=True)
                 == "Kyoto-shi" )

    def test_cityname2normalize_ascii_fail(self):
        assert ( jp.cityname2normalize('KYOTO-SHI',ascii=True)
                 == jp.cityname2normalize('kyoto-shi',ascii=True)
                 == None )

    def test_cityname2normalize_ascii_ignore_case(self):
        assert ( jp.cityname2normalize('KYOTO-SHI',
                        ascii=True, ignore_case=True)
                 == jp.cityname2normalize('kyoto-shi',
                        ascii=True, ignore_case=True)
                 == "Kyoto-shi" )

    def test_cityname2normalize_ascii_list_list(self):
        assert ( jp.cityname2normalize(
                    ['京都市北区',
                     '京都市左京区',
                     '京都市右京区'], ascii=True)
                 == jp.cityname2normalize(
                    ['Kyoto-shi Kita-ku',
                     'Kyoto-shi Sakyo-ku',
                     'Kyoto-shi Ukyo-ku'], ascii=True)
                 == ['Kyoto-shi Kita-ku',
                     'Kyoto-shi Sakyo-ku',
                     'Kyoto-shi Ukyo-ku']  )

    def test_cityname2normalize_ascii_list_fail(self):
        assert ( jp.cityname2normalize(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU'], ascii=True)
                 == jp.cityname2normalize(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku'], ascii=True)
                 == [None, None, None] )

    def test_cityname2normalize_ascii_list_ignore_case(self):
        assert ( jp.cityname2normalize(
                    ['KYOTO-SHI KITA-KU',
                     'KYOTO-SHI SAKYO-KU',
                     'KYOTO-SHI UKYO-KU'], ascii=True, ignore_case=True)
                 == jp.cityname2normalize(
                    ['kyoto-shi kita-ku',
                     'kyoto-shi sakyo-ku',
                     'kyoto-shi ukyo-ku'], ascii=True, ignore_case=True)
                 == ['Kyoto-shi Kita-ku',
                     'Kyoto-shi Sakyo-ku',
                     'Kyoto-shi Ukyo-ku']  )

    def test_cityname2normalize_ascii_series(self):
        s1 = jp.cityname2normalize( pd.Series(
                     ['京都市北区',
                      '京都市左京区',
                      '京都市右京区']), ascii=True)
        s2 = jp.cityname2normalize( pd.Series(
                     ['Kyoto-shi Kita-ku',
                      'Kyoto-shi Sakyo-ku',
                      'Kyoto-shi Ukyo-ku'] ), ascii=True)
        s3 = pd.Series( ['Kyoto-shi Kita-ku',
                         'Kyoto-shi Sakyo-ku',
                         'Kyoto-shi Ukyo-ku'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize_ascii_series_fail(self):
        s1 = jp.cityname2normalize( pd.Series(
                     ['KYOTO-SHI KITA-KU',
                      'KYOTO-SHI SAKYO-KU',
                      'KYOTO-SHI UKYO-KU'] ), ascii=True)
        s2 = jp.cityname2normalize( pd.Series(
                     ['kyoto-shi kita-ku',
                      'kyoto-shi sakyo-ku',
                      'kyoto-shi ukyo-ku'] ), ascii=True)
        s3 = pd.Series([None, None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2normalize_ascii_series_ignore_case(self):
        s1 = jp.cityname2normalize( pd.Series(
                     ['KYOTO-SHI KITA-KU',
                      'KYOTO-SHI SAKYO-KU',
                      'KYOTO-SHI UKYO-KU'] ), ascii=True, ignore_case=True)
        s2 = jp.cityname2normalize( pd.Series(
                     ['kyoto-shi kita-ku',
                      'kyoto-shi sakyo-ku',
                      'kyoto-shi ukyo-ku'] ), ascii=True, ignore_case=True)
        s3 = pd.Series( ['Kyoto-shi Kita-ku',
                         'Kyoto-shi Sakyo-ku',
                         'Kyoto-shi Ukyo-ku'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_citycode2name(self):
        assert jp.citycode2name(26100) == '京都市'

    def test_citycode2name_as_str(self):
        assert jp.citycode2name("26100") == '京都市'

    def test_citycode2name_checkdigit(self):
        assert jp.citycode2name(261009) == '京都市'

    def test_citycode2name_as_str_checkdigit(self):
        assert jp.citycode2name("261009") == '京都市'

    def test_citycode2name_list(self):
        assert ( jp.citycode2name([26101, 26103, 26108])
                 ==  ['京都市北区', '京都市左京区', '京都市右京区'] )


    def test_citycode2name_ascii(self):
        assert jp.citycode2name(26100, ascii=True) == 'Kyoto-shi'

    def test_citycode2name_ascii_str(self):
        assert jp.citycode2name("26100", ascii=True) == 'Kyoto-shi'

    def test_citycode2name_ascii_checkdigit(self):
        assert jp.citycode2name(261009, ascii=True) == 'Kyoto-shi'

    def test_citycode2name_ascii_str_checkdigit(self):
        assert jp.citycode2name("261009", ascii=True) == 'Kyoto-shi'

    def test_citycode2name_ascii_list(self):
        assert ( jp.citycode2name([26101, 26103, 26108], ascii=True)
                == ['Kyoto-shi Kita-ku',
                    'Kyoto-shi Sakyo-ku',
                    'Kyoto-shi Ukyo-ku'] )

    def test_citycode2name_ascii_series(self):
        s1 = jp.citycode2name(pd.Series([26101, 26103, 26108]), ascii=True)
        s2 = pd.Series( ['Kyoto-shi Kita-ku',
                         'Kyoto-shi Sakyo-ku',
                         'Kyoto-shi Ukyo-ku'] )
        assert s1.equals(s2) == True


    def test_cityname2prefcode(self):
        assert ( jp.cityname2prefcode('京都市')
                 == jp.cityname2prefcode('Kyoto-shi')
                 == 26 )

    def test_cityname2prefcode_fail(self):
        assert ( jp.cityname2prefcode('KYOTO-SHI')
                 == jp.cityname2prefcode('kyoto-shi')
                 == None )

    def test_cityname2prefcode_ignore_case(self):
        assert ( jp.cityname2prefcode('京都市', ignore_case=True)
                 == jp.cityname2prefcode('KYOTO-SHI', ignore_case=True)
                 == jp.cityname2prefcode('kyoto-shi', ignore_case=True)
                 == 26 )

    def test_cityname2prefcode_list(self):
        assert ( jp.cityname2prefcode(['京都市北区', '大阪市中央区'])
                 == jp.cityname2prefcode(['Kyoto-shi Kita-ku',
                                          'Osaka-shi Chuo-ku'])
                 == [26, 27] )

    def test_cityname2prefcode_list_fail(self):
        assert ( jp.cityname2prefcode(['KYOTO-SHI KITA-KU',
                                       'OSAKA-SHI CHUO-KU'])
                 == jp.cityname2prefcode(['kyoto-shi kita-ku',
                                          'osaka-shi chuo-ku'])
                 == [None, None] )

    def test_cityname2prefcode_list_ignore_case(self):
        assert ( jp.cityname2prefcode(
                       ['京都市北区', '大阪市中央区'],
                       ignore_case=True)
                 == jp.cityname2prefcode(
                       ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
                       ignore_case=True)
                 == jp.cityname2prefcode(
                       ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
                       ignore_case=True)
                 == [26, 27] )

    def test_cityname2prefcode_series(self):
        s1 = jp.cityname2prefcode(
                pd.Series(['京都市北区', '大阪市中央区']))
        s2 = jp.cityname2prefcode(
                pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']))
        s3 = pd.Series([26, 27])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefcode_series_fail(self):
        s1 = jp.cityname2prefcode(
                pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
        s2 = jp.cityname2prefcode(
                pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
        s3 = pd.Series([None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefcode_series_ignore_case(self):
        s1 = jp.cityname2prefcode(
                pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
                ignore_case=True)
        s2 = jp.cityname2prefcode(
                pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
                ignore_case=True)
        s3 = pd.Series([26, 27])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefecture(self):
        assert ( jp.cityname2prefecture('京都市')
                 == jp.cityname2prefecture('Kyoto-shi')
                 == '京都府' )

    def test_cityname2prefecture_fail(self):
        assert ( jp.cityname2prefecture('KYOTO-SHI')
                 == jp.cityname2prefecture('kyoto-shi')
                 == None )

    def test_cityname2prefecture_ignore_case(self):
        assert ( jp.cityname2prefecture('京都市', ignore_case=True)
                 == jp.cityname2prefecture('Kyoto-shi', ignore_case=True)
                 == jp.cityname2prefecture('KYOTO-SHI', ignore_case=True)
                 == jp.cityname2prefecture('kyoto-shi', ignore_case=True)
                 == '京都府' )

    def test_cityname2prefecture_list(self):
        assert ( jp.cityname2prefecture(['京都市北区', '大阪市中央区'])
                 == jp.cityname2prefecture(['Kyoto-shi Kita-ku',
                                            'Osaka-shi Chuo-ku'])
                 == ['京都府', '大阪府'] )

    def test_cityname2prefecture_list_fail(self):
        assert ( jp.cityname2prefecture(
                     ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'])
                 == jp.cityname2prefecture(
                     ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'])
                 == [None, None] )

    def test_cityname2prefecture_list_ignore_case(self):
        assert ( jp.cityname2prefecture(
                      ['京都市北区', '大阪市中央区'],
                      ignore_case=True)
                 == jp.cityname2prefecture(
                      ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
                      ignore_case=True)
                 == jp.cityname2prefecture(
                      ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
                      ignore_case=True)
                 == jp.cityname2prefecture(
                      ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
                      ignore_case=True)
                 == ['京都府', '大阪府'] )

    def test_cityname2prefecture_series(self):
        s1 = jp.cityname2prefecture(
                    pd.Series( ['京都市北区', '大阪市中央区']))
        s2 = jp.cityname2prefecture(
                    pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']))
        s3 = pd.Series(['京都府', '大阪府'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefecture_series_fail(self):
        s1 = jp.cityname2prefecture(
                    pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']))
        s2 = jp.cityname2prefecture(
                    pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']))
        s3 = pd.Series([None, None] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefecture_series_ignore_case(self):
        s1 = jp.cityname2prefecture(
                    pd.Series( ['京都市北区', '大阪市中央区']),
                    ignore_case=True)
        s2 = jp.cityname2prefecture(
                    pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
                    ignore_case=True)
        s3 = jp.cityname2prefecture(
                    pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
                    ignore_case=True)
        s4 = jp.cityname2prefecture(
                    pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
                    ignore_case=True)
        s5 = pd.Series(['京都府', '大阪府'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == s4.equals(s5)
                 == True )

    def test_cityname2prefecture_ascii(self):
        assert ( jp.cityname2prefecture('京都市', ascii=True)
                 == jp.cityname2prefecture('Kyoto-shi', ascii=True)
                 == 'Kyoto' )

    def test_cityname2prefecture_ascii_fail(self):
        assert ( jp.cityname2prefecture('KYOTO-SHI', ascii=True)
                 == jp.cityname2prefecture('kyoto-shi', ascii=True)
                 == None )

    def test_cityname2prefecture_ascii_ignore_case(self):
        assert ( jp.cityname2prefecture('京都市',
                         ascii=True, ignore_case=True)
                 == jp.cityname2prefecture('Kyoto-shi',
                         ascii=True, ignore_case=True)
                 == jp.cityname2prefecture('KYOTO-SHI',
                         ascii=True, ignore_case=True)
                 == jp.cityname2prefecture('kyoto-shi',
                         ascii=True, ignore_case=True)
                 == 'Kyoto' )

    def test_cityname2prefecture_ascii_list(self):
        assert ( jp.cityname2prefecture(
                     ['京都市北区', '大阪市中央区'],
                     ascii=True)
                 == jp.cityname2prefecture(
                     ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
                     ascii=True)
                 == ['Kyoto', 'Osaka'] )

    def test_cityname2prefecture_ascii_list_fail(self):
        assert ( jp.cityname2prefecture(
                     ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
                     ascii=True)
                 == jp.cityname2prefecture(
                     ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
                     ascii=True)
                 == [None, None] )

    def test_cityname2prefecture_ascii_list_ignore_case(self):
        assert ( jp.cityname2prefecture(
                     ['京都市北区', '大阪市中央区'],
                     ascii=True, ignore_case=True)
                 == jp.cityname2prefecture(
                     ['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku'],
                     ascii=True, ignore_case=True)
                 == jp.cityname2prefecture(
                     ['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU'],
                     ascii=True, ignore_case=True)
                 == jp.cityname2prefecture(
                     ['kyoto-shi kita-ku', 'osaka-shi chuo-ku'],
                     ascii=True, ignore_case=True)
                 == ['Kyoto', 'Osaka'] )

    def test_cityname2prefecture_ascii_series(self):
        s1 = jp.cityname2prefecture(
                     pd.Series(['京都市北区', '大阪市中央区']),
                     ascii=True)
        s2 = jp.cityname2prefecture(
                     pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
                     ascii=True)
        s3 = pd.Series(['Kyoto', 'Osaka'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefecture_ascii_series_fail(self):
        s1 = jp.cityname2prefecture(
                     pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
                     ascii=True)
        s2 = jp.cityname2prefecture(
                     pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
                     ascii=True)
        s3 = pd.Series([None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_cityname2prefecture_ascii_series_ignore_case(self):
        s1 = jp.cityname2prefecture(
                     pd.Series(['京都市北区', '大阪市中央区']),
                     ascii=True, ignore_case=True)
        s2 = jp.cityname2prefecture(
                     pd.Series(['Kyoto-shi Kita-ku', 'Osaka-shi Chuo-ku']),
                     ascii=True, ignore_case=True)
        s3 = jp.cityname2prefecture(
                     pd.Series(['KYOTO-SHI KITA-KU', 'OSAKA-SHI CHUO-KU']),
                     ascii=True, ignore_case=True)
        s4 = jp.cityname2prefecture(
                     pd.Series(['kyoto-shi kita-ku', 'osaka-shi chuo-ku']),
                     ascii=True, ignore_case=True)
        s5 = pd.Series(['Kyoto', 'Osaka'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == s4.equals(s5)
                 == True )

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
