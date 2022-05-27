import sys

sys.path.append("../jp_prefecture")

from jp_prefecture import jp_prefectures as jp

class TestClass:
    def test_name2code(self):
        assert ( jp.name2code('京都府')
                 == jp.name2code('京都')
                 == jp.name2code('Kyoto')
                 == jp.name2code('KYOTO')
                 == jp.name2code('kyoto')
                 == 26 )

    def test_code2name(self):
        assert jp.code2name(26) == '京都府'

    def test_code2alphabet(self):
        assert jp.code2alphabet(26) == 'Kyoto'

    def test_name2alphabet(self):
        assert ( jp.name2alphabet('京都府')
                 == jp.name2alphabet('京都')
                 == jp.name2alphabet('Kyoto')
                 == jp.name2alphabet('KYOTO')
                 == jp.name2alphabet('kyoto')
                 == 'Kyoto' )

    def test_alphabet2name(self):
        assert ( jp.alphabet2name('Kyoto')
                 == jp.alphabet2name('KYOTO')
                 == jp.alphabet2name('kyoto')
                 == jp.alphabet2name('京都府')
                 == jp.alphabet2name('京都')
                 == '京都府' )
