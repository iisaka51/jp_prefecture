import sys

sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.utils import is_alpha, is_alnum, df_compare
import pandas as pd

class TestClass:
    def test_is_alpha_alphabet(self):
        assert ( is_alpha('iisaka')
                 == True )

    def test_is_alpha_alphabet_with_number(self):
        assert ( is_alpha('iisaka51')
                 == False )

    def test_is_alpha_alphabet_with_symbol(self):
        assert ( is_alpha('@iisaka51')
                 == is_alpha('Goichi (iisaka) Yukawa')
                 == False )

    def test_is_alpha_kanji(self):
        assert ( is_alpha('京都市')
                 == False )

    def test_is_alpha_kanji_num(self):
        assert ( is_alpha('１２３')
                 == False )

    def test_is_alnum_alphabet(self):
        assert ( is_alnum('iisaka')
                 == True )

    def test_is_alnum_alphabet_with_number(self):
        assert ( is_alnum('iisaka51')
                 == True )

    def test_is_alnum_alphabet_with_symbol(self):
        assert ( is_alnum('@iisaka51')
                 == is_alnum('Goichi (iisaka) Yukawa')
                 == False )

    def test_is_alnum_kanji(self):
        assert ( is_alnum('京都市')
                 == False )

    def test_is_alnum_kanji_num(self):
        assert ( is_alpha('１２３')
                 == False )

    def test_df_compare(self):
        d1 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        d2 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        assert ( df_compare(d1, d2) == True )

    def test_df_compare_diff_count_zero(self):
        d1 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        d2 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        assert ( df_compare(d1, d2, diff_count=True) == 0 )

    def test_df_compare_diff_count_non_zero(self):
        d1 = pd.DataFrame([ ['26100', 35.0117,135.452],
                            ['27100', 34.4138,135.3808]],
                          columns=['cityCode', 'latitude', 'longitude'])
        d2 = pd.DataFrame([ ['京都市', 35.0117,135.452],
                            ['大阪市', 34.4138,135.3808]],
                          columns=['cityName', 'latitude', 'longitude'])
        assert ( df_compare(d1, d2, diff_count=True) != 0 )
