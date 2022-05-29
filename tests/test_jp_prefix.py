import sys

sys.path.append("../jp_prefecture")

from jp_prefecture import jp_prefectures as jp
import pandas as pd

class TestClass:
    def test_name2code(self):
        assert ( jp.name2code('京都府')
                 == jp.name2code('京都')
                 == jp.name2code('Kyoto')
                 == jp.name2code('KYOTO')
                 == jp.name2code('kyoto')
                 == 26 )

    def test_name2code_list(self):
        assert ( jp.name2code(['京都府', '大阪府', '奈良県'])
                 == jp.name2code(['京都', '大阪', '奈良'])
                 == jp.name2code(['Kyoto', 'Osaka', 'Nara'])
                 == jp.name2code(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.name2code(['kyoto', 'osaka', 'nara'])
                 == [26, 27, 29] )

    def test_name2code_series(self):
        s1 = jp.name2code(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.name2code(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.name2code(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = jp.name2code(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s5 = jp.name2code(pd.Series(['kyoto', 'osaka', 'nara']))
        s6 = pd.Series([26, 27, 29])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == s4.equals(s5)
                 == s5.equals(s6)
                 == True )

    def test_code2name(self):
        assert jp.code2name(26) == '京都府'

    def test_code2name_list(self):
        assert jp.code2name([26, 27, 29]) == ['京都府', '大阪府', '奈良県']

    def test_code2name_series(self):
        s1 = jp.code2name(pd.Series([26, 27, 29]))
        s2 = pd.Series(['京都府', '大阪府', '奈良県'])
        assert s1.equals(s2) == True

    def test_code2alphabet(self):
        assert jp.code2alphabet(26) == 'Kyoto'

    def test_code2alphabet_list(self):
        assert jp.code2alphabet([26, 27, 29]) == ['Kyoto', 'Osaka', 'Nara']

    def test_code2alphabet_series(self):
        s1 = jp.code2alphabet(pd.Series([26, 27, 29]))
        s2 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert s1.equals(s2) == True

    def test_name2alphabet(self):
        assert ( jp.name2alphabet('京都府')
                 == jp.name2alphabet('京都')
                 == jp.name2alphabet('Kyoto')
                 == jp.name2alphabet('KYOTO')
                 == jp.name2alphabet('kyoto')
                 == 'Kyoto' )

    def test_name2alphabet_list(self):
        assert ( jp.name2alphabet(['京都府', '大阪府', '奈良県'])
                 == jp.name2alphabet(['京都', '大阪', '奈良'])
                 == jp.name2alphabet(['Kyoto', 'Osaka', 'Nara'])
                 == jp.name2alphabet(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.name2alphabet(['kyoto', 'osaka', 'nara'])
                 == ['Kyoto', 'Osaka', 'Nara'] )

    def test_name2alphabet_series(self):
        s1 = jp.name2alphabet(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.name2alphabet(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.name2alphabet(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = jp.name2alphabet(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s5 = jp.name2alphabet(pd.Series(['kyoto', 'osaka', 'nara']))
        s6 = pd.Series(['Kyoto', 'Osaka', 'Nara'])
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == s4.equals(s5)
                 == s5.equals(s6)
                 == True )

    def test_alphabet2name(self):
        assert ( jp.alphabet2name('Kyoto')
                 == jp.alphabet2name('KYOTO')
                 == jp.alphabet2name('kyoto')
                 == jp.alphabet2name('京都府')
                 == jp.alphabet2name('京都')
                 == '京都府' )

    def test_alphabet2name_list(self):
        assert ( jp.alphabet2name(['京都府', '大阪府', '奈良県'])
                 == jp.alphabet2name(['京都', '大阪', '奈良'])
                 == jp.alphabet2name(['Kyoto', 'Osaka', 'Nara'])
                 == jp.alphabet2name(['KYOTO', 'OSAKA', 'NARA'])
                 == jp.alphabet2name(['kyoto', 'osaka', 'nara'])
                 == ['京都府', '大阪府', '奈良県'] )

    def test_alphabet2name_series(self):
        s1 = jp.alphabet2name(pd.Series(['京都府', '大阪府', '奈良県']))
        s2 = jp.alphabet2name(pd.Series(['京都', '大阪', '奈良']))
        s3 = jp.alphabet2name(pd.Series(['Kyoto', 'Osaka', 'Nara']))
        s4 = jp.alphabet2name(pd.Series(['KYOTO', 'OSAKA', 'NARA']))
        s5 = jp.alphabet2name(pd.Series(['kyoto', 'osaka', 'nara']))
        s6 = pd.Series(['京都府', '大阪府', '奈良県'] )
        assert ( s1.equals(s2)
                 == s2.equals(s3)
                 == s3.equals(s4)
                 == s4.equals(s5)
                 == s5.equals(s6)
                 == True )
