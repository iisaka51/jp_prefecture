import sys
sys.path.insert(0,"../jp_numbers")

from jp_numbers import JpNumberParser

class TestClass:
    parser = JpNumberParser()

class TestKanji2Number(TestClass):

    def test_kanji_number_single_char(self):
        data = [ '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九' ]
        for i, d in enumerate(data):
            v = self.parser.kanji2number(d)
            assert ( v.as_int == i )
            assert ( v.as_str == str(i) )
            assert ( v.as_kanji == d )

    def test_arabic_kanji_number_single_char(self):
        data = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
        for i, d in enumerate(data):
            v = self.parser.kanji2number(d)
            assert ( v.as_int == i )
            assert ( v.as_str == str(i) )
            assert ( v.as_kanji == d )

    def test_kanji_number_case1(self):
        data = { '十':10, '十一': 11,
                 '百五':105, '百十': 110, '一百十': 110,
                 '二百六十': 260, '二百六十四': 264,
                 '千三百':1_300, '一千三百': 1_300 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_kanji_number_case2(self):
        data = { '百三十五万': 1_350_000,
                 '一億二千三百': 100_002_300,
                 '一億二千三百万': 123_000_000,
                 '二百億': 20_000_000_000 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_arabic_kanji_number_case1(self):
        data = { '１０':10, '１１': 11, '１３５':135, '１３００':1_300 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_arabic_kanji_number_case2(self):
        data = { '１３５００００': 1_350_000,
                 '１２３００００００': 123_000_000,
                 '２００００００００００':20_000_000_000 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_arabic_kanji_number_case3(self):
        data = { '１，３５０，０００': 1_350_000,
                 '１２３，０００，０００': 123_000_000,
                 '２００，０００，０００，０００':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_arabic_kanji_number_case4(self):
        data = { '１千３５０万': 13_500_000,
                 '１億２３０万': 102_300_000,
                 '２００億':  20_000_000_000 }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_daiji_number(self):
        data = { '壱仟参佰肆': 1304,
                 '捌萬漆仟陸佰伍拾肆': 87654,
        }
        for d, n in data.items():
            v = self.parser.kanji2number(d)
            assert (v.as_int == n)
            assert (v.as_str == str(n))
            assert ( v.as_kanji == d )


class TestNumber2Kanji(TestClass):

    def test_number2kanji_single_char(self):
        data = [ '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九' ]
        for n, d in enumerate(data):
            v = self.parser.number2kanji(n)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2arabic_kanji_single_char(self):
        data = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
        for n, d in enumerate(data):
            v = self.parser.number2kanji(n, style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_str_number2kanji_single_char(self):
        data = [ '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九' ]
        for n, d in enumerate(data):
            v = self.parser.number2kanji(str(n))
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_str_number2arabic_kanji_single_char(self):
        data = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
        for n, d in enumerate(data):
            v = self.parser.number2kanji(str(n), style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )


    def test_number2arabic_kanji_case1(self):
        data = { '１０':10, '１１': 11, '１３５':135, '１３００':1_300 }
        for d, n in data.items():
            v = self.parser.number2kanji(n, style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_str_number2arabic_kanji_case1(self):
        data = { '１０':10, '１１': 11, '１３５':135, '１３００':1_300 }
        for d, n in data.items():
            v = self.parser.number2kanji(str(n), style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case1(self):
        data = { '千三百五': 1305,
                 '千三百五十': 1350,
                 '千三百五十万': 13_500_000,
                 '一億二千三百万': 123_000_000,
                 '百三十五億': 1_3500_000_000,
                 '二百億': 20_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(n)
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case2(self):
        data = { '千三百五十万': 13_500_000,
                 '一億二千三百万': 123_000_000,
                 '百三十五億': 1_3500_000_000,
                 '二千億':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(str(n))
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case3(self):
        data = { '１３５００００': 1_350_000,
                 '１２３００００００': 123_000_000,
                 '２０００００００００００':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(n, style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case4(self):
        data = { '１３５００００': 1_350_000,
                 '１２３００００００': 123_000_000,
                 '２０００００００００００':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(str(n), style='arabic')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case5(self):
        data = { '１億２３': 100_000_023,
                 '８万７６５４': 87654,
                 '１３５０万': 13_500_000,
                 '１億２３０万': 102_300_000,
                 '２０００億':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(str(n), style='mix')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_case6(self):
        data = { '１，３５０，０００': 1_350_000,
                 '１２３，０００，０００': 123_000_000,
                 '２００，０００，０００，０００':200_000_000_000 }
        for d, n in data.items():
            v = self.parser.number2kanji(n, style='finance')
            assert ( v.as_int == n )
            assert ( v.as_str == str(n) )
            assert ( v.as_kanji == d )

    def test_number2kanji_daiji(self):
        data = { '壱仟参佰肆': 1304,
                 '捌萬漆仟陸佰伍拾肆': 87654,
        }
        for d, n in data.items():
            v = self.parser.number2kanji(n, style='daiji')
            assert (v.as_int == n)
            assert (v.as_str == str(n))
            assert ( v.as_kanji == d )

class TestNormalize(TestClass):

    def test_normalized_kanji_case1(self):
        data = '京都府長岡京市天神2丁目15-13'
        expect = '京都府長岡京市天神二丁目十五-十三'
        v = self.parser.normalize_kanjinumber(data)
        assert ( v == expect )

    def test_normalized_kanji_case2(self):
        data = '京都府長岡京市天神２丁目１５ー１３'
        expect = '京都府長岡京市天神二丁目十五ー十三'
        v = self.parser.normalize_kanjinumber(data)
        assert ( v == expect )

    def test_normalized_kanji_case3(self):
        data = '京都府長岡京市天神２丁目15ー13'
        expect = '京都府長岡京市天神二丁目十五ー十三'
        v = self.parser.normalize_kanjinumber(data)
        assert ( v == expect )

    def test_normalized_kanji_case3(self):
        data = '京都府長岡京市天神二丁目十五ー十三'
        expect = '京都府長岡京市天神二丁目十五ー十三'
        v = self.parser.normalize_kanjinumber(data)
        assert ( v == expect )

    def test_normalized_kanji_case3(self):
        data = '札幌市中央区南２５条西１１丁目'
        expect = '札幌市中央区南二十五条西十一丁目'
        v = self.parser.normalize_kanjinumber(data)
        assert ( v == expect )
