import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture import jp_prefectures as jp
import pandas as pd

class TestClass:
    def test_name2code(self):
        assert ( jp.name2code('京都府')
                 == jp.name2code('京都')
                 == jp.name2code('Kyoto')
                 == 26 )

    def test_name2code_none(self):
        assert ( jp.name2code('KYOTO')
                 == jp.name2code('kyoto')
                 == None )

    def test_name2code_ignore_case(self):
        assert ( jp.name2code('KYOTO', ignore_case=True)
                 == jp.name2code('kyoto', ignore_case=True)
                 == 26 )

    def test_name2code_list(self):
        assert ( jp.name2code(['京都府', '大阪府', '奈良県'])
                 == jp.name2code(['京都', '大阪', '奈良'])
                 == jp.name2code(['Kyoto', 'Osaka', 'Nara'])
                 == [26, 27, 29] )

    def test_name2code_none_list(self):
        assert ( jp.name2code(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.name2code(['kyoto', 'osaka', 'nara'])
                 == [None, None, None] )

    def test_name2code_ignore_case_list(self):
        assert ( jp.name2code(['KYOTO', 'OSAKA', 'NARA'], ignore_case=True)
                 == jp.name2code(['kyoto', 'osaka', 'nara'], ignore_case=True)
                 == [26, 27, 29] )

    def test_name2code_series(self):
        s1 = jp.name2code(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.name2code(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.name2code(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = pd.Series([26, 27, 29])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == True )

    def test_name2code_none_series(self):
        s1 = jp.name2code(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s2 = jp.name2code(pd.Series(['kyoto', 'osaka', 'nara']))
        s3 = pd.Series([None, None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_name2code_ignore_case_series(self):
        s1 = jp.name2code(
                pd.Series(['KYOTO', 'OSAKA', 'NARA']), ignore_case=True)
        s2 = jp.name2code(
                pd.Series(['kyoto', 'osaka', 'nara']), ignore_case=True)
        s3 = pd.Series([26, 27, 29])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_code2name(self):
        assert jp.code2name(26) == '京都府'

    def test_code2name_as_str(self):
        assert jp.code2name("26") == '京都府'

    def test_code2name_list(self):
        assert ( jp.code2name([26, 27, 29])
                 == ['京都府', '大阪府', '奈良県'] )

    def test_code2name_as_str_list(self):
        assert ( jp.code2name(["26", "27", "29"])
                 == ['京都府', '大阪府', '奈良県'] )

    def test_code2name_series(self):
        s1 = jp.code2name(pd.Series([26, 27, 29]))
        s2 = pd.Series(['京都府', '大阪府', '奈良県'])
        assert s1.equals(s2) == True

    def test_code2name_as_str_series(self):
        s1 = jp.code2name(pd.Series(["26", "27", "29"]))
        s2 = pd.Series(['京都府', '大阪府', '奈良県'])
        assert s1.equals(s2) == True

    def test_code2name_ascii(self):
        assert jp.code2name(26, ascii=True) == 'Kyoto'

    def test_code2name_ascii_str(self):
        assert jp.code2name("26", ascii=True) == 'Kyoto'

    def test_code2name_ascii_list(self):
        assert ( jp.code2name([26, 27, 29], ascii=True)
                 == ['Kyoto', 'Osaka', 'Nara'] )

    def test_code2name_ascii_str_list(self):
        assert ( jp.code2name(["26", "27", "29"], ascii=True)
                 == ['Kyoto', 'Osaka', 'Nara'] )

    def test_code2name_ascii_series(self):
        s1 = jp.code2name(pd.Series([26, 27, 29]), ascii=True)
        s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert s1.equals(s2) == True

    def test_code2name_ascii_str_series(self):
        s1 = jp.code2name(pd.Series(["26", "27", "29"]), ascii=True)
        s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert s1.equals(s2) == True

    def test_name2normalize(self):
        assert ( jp.name2normalize('京都府')
                 == jp.name2normalize('京都')
                 == jp.name2normalize('Kyoto')
                 == '京都府' )

    def test_name2normalize_none(self):
        assert ( jp.name2normalize('KYOTO')
                 == jp.name2normalize('kyoto')
                 == None )

    def test_name2normalize_ignore_case(self):
        assert ( jp.name2normalize('KYOTO', ignore_case=True)
                 == jp.name2normalize('kyoto', ignore_case=True)
                 == '京都府' )

    def test_name2normalize_list(self):
        assert ( jp.name2normalize(['京都府', '大阪府', '奈良県'])
                 == jp.name2normalize(['京都', '大阪', '奈良'])
                 == jp.name2normalize(['Kyoto', 'Osaka', 'Nara'])
                 == ['京都府', '大阪府', '奈良県'] )

    def test_name2normalize_list_none(self):
        assert ( jp.name2normalize(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.name2normalize(['kyoto', 'osaka', 'nara'])
                 == [None, None, None] )

    def test_name2normalize_list_ignore_case(self):
        assert ( jp.name2normalize(
                     ['KYOTO', 'OSAKA', 'NARA'], ignore_case=True)
                 == jp.name2normalize(
                     ['kyoto', 'osaka', 'nara'], ignore_case=True)
                 == ['京都府', '大阪府', '奈良県'] )

    def test_name2normalize_series(self):
        s1 = jp.name2normalize(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.name2normalize(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.name2normalize(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = pd.Series(['京都府', '大阪府', '奈良県'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == True )

    def test_name2normalize_series_none(self):
        s1 = jp.name2normalize(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s2 = jp.name2normalize(pd.Series(['kyoto', 'osaka', 'nara']))
        s3 = pd.Series([None, None, None])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_name2normalize_ascii(self):
        assert ( jp.name2normalize('京都府', ascii=True)
                 == jp.name2normalize('京都', ascii=True)
                 == jp.name2normalize('Kyoto', ascii=True)
                 == 'Kyoto' )

    def test_name2normalize_ascii_none(self):
        assert ( jp.name2normalize('KYOTO', ascii=True)
                 == jp.name2normalize('kyoto', ascii=True)
                 == None )

    def test_name2normalize_ascii_ignore_case(self):
        assert ( jp.name2normalize('KYOTO', ascii=True, ignore_case=True)
                 == jp.name2normalize('kyoto', ascii=True, ignore_case=True)
                 == 'Kyoto' )

    def test_name2normalize_list_ascii(self):
        assert ( jp.name2normalize(['京都府', '大阪府', '奈良県'], ascii=True)
                 == jp.name2normalize(['京都', '大阪', '奈良'], ascii=True)
                 == jp.name2normalize(['Kyoto', 'Osaka', 'Nara'], ascii=True)
                 == ['Kyoto', 'Osaka', 'Nara'] )

    def test_name2normalize_list_ascii_fail(self):
        assert ( jp.name2normalize(
                     ['KYOTO', 'OSAKA', 'NARA'], ascii=True, ignore_case=True)
                 == jp.name2normalize(
                     ['kyoto', 'osaka', 'nara'], ascii=True, ignore_case=True)
                 == ['Kyoto', 'Osaka', 'Nara'] )

    def test_name2normalize_series_ascii(self):
        s1 = jp.name2normalize( pd.Series(['京都府', '大阪府', '奈良県']),
                               ascii=True)
        s2 = jp.name2normalize(pd.Series(['京都', '大阪', '奈良']),
                               ascii=True)
        s3 = jp.name2normalize(pd.Series(['Kyoto', 'Osaka', 'Nara']),
                               ascii=True)
        s4 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == True )

    def test_name2normalize_series_ascii_fail(self):
        s1 = jp.name2normalize( pd.Series(['KYOTO', 'OSAKA', 'NARA']),
                  ascii=True)
        s2 = jp.name2normalize( pd.Series(['kyoto', 'osaka', 'nara']),
                  ascii=True)
        s3 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == False )

    def test_name2normalize_series_ascii_fail(self):
        s1 = jp.name2normalize(pd.Series(['KYOTO', 'OSAKA', 'NARA']),
                  ascii=True, ignore_case=True)
        s2 = jp.name2normalize(pd.Series(['kyoto', 'osaka', 'nara']),
                  ascii=True, ignore_case=True)
        s3 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_validate_ok(self):
        assert ( jp.validate('京都府')
                 == jp.validate('京都')
                 == jp.validate('Kyoto')
                 == True )

    def test_validate_fail(self):
        assert ( jp.validate('京都県')
                 == jp.validate('都京')
                 == jp.validate('kyotofu')
                 == False )

    def test_validate_ignore_case(self):
        assert ( jp.validate('KYOTO', ignore_case=True)
                 == jp.validate('kyoto', ignore_case=True)
                 == True )

    def test_validate_list(self):
        assert ( jp.validate(['京都府', '大阪府', '奈良県'])
                 == jp.validate(['京都', '大阪', '奈良'])
                 == jp.validate(['Kyoto', 'Osaka', 'Nara'])
                 == [True, True, True] )

    def test_validate_list_fail(self):
        assert ( jp.validate(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.validate(['kyoto', 'osaka', 'nara'])
                 == [False, False, False] )

    def test_validate_list_ignore_case(self):
        assert ( jp.validate(['KYOTO', 'OSAKA', 'NARA'], ignore_case=True)
                 == jp.validate(['kyoto', 'osaka', 'nara'], ignore_case=True)
                 == [True, True, True] )

    def test_validate_list_false(self):
        assert ( jp.validate(['京都県', '大阪府', '奈良県'])
                 == jp.validate(['都京', '大阪', '奈良'])
                 == jp.validate(['KyOto', 'Osaka', 'Nara'])
                 == [False, True, True] )

    def test_validate_series(self):
        s1 = jp.validate(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.validate(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.validate(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = pd.Series([True, True, True])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == True )

    def test_validate_series_fail(self):
        s1 = jp.validate(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s2 = jp.validate(pd.Series(['kyoto', 'osaka', 'nara']))
        s3 = pd.Series([False, False, False])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_validate_series_ignore_case(self):
        s1 = jp.validate(pd.Series(['KYOTO', 'OSAKA', 'NARA']),
                         ignore_case=True)
        s2 = jp.validate(pd.Series(['kyoto', 'osaka', 'nara']),
                         ignore_case=True)
        s3 = pd.Series([True, True, True])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == True )

    def test_validate_series_false(self):
        s1 = jp.validate(pd.Series(['京都県', '大阪府', '奈良県']))
        s2 = jp.validate(pd.Series(['都京', '大阪', '奈良']))
        s3 = jp.validate(pd.Series(['kyotofu', 'Osaka', 'Nara']))
        s4 = pd.Series([False, True, True])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == True )
