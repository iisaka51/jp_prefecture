import sys
sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.address import JpAddressParser, JpAddress

class TestClass:
    parser = JpAddressParser()

    def test_jpaddressparser_kyoto_with_apartment(self):
        data = '〒617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26209)
        assert ( addr.geodetic == (34.928769, 135.696847))


    def test_jpaddressparser_with_zip(self):
        data = '〒617-0824 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170824' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_with_7digit_zip(self):
        data = '6170824 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170824' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_no_zip(self):
        data = '長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_short_prefecture(self):
        data = '京都長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '京都府長岡京市天神２丁目１５−１３')


    def test_jpaddressparser_short_prefecture_with_space(self):
        data = '京都 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_with_space(self):
        data = '京都府 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( addr.__str__()
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_no_prefecture(self):
        data = '京都市下京区烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))

    def test_jpaddressparser_no_prefecture_with_space(self):
        data = '京都市 下京区烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))
        assert ( addr.__str__()
                 == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

    def test_jpaddressparser_fuzzy(self):
        data = '京都 下京区 烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))
        assert ( addr.__str__()
                 == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

    def test_jpaddressparser_tokyo_no_prefecture(self):
        data = '千代田区丸の内1-9-2グラントウキョウサウスタワー23階'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '千代田区' )
        assert ( addr.street == '丸の内1-9-2グラントウキョウサウスタワー23階')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13101)
        assert ( addr.geodetic == (35.68156, 139.767201))
        assert ( addr.__str__()
           ==  '東京都千代田区丸の内1-9-2グラントウキョウサウスタワー23階' )

    def test_jpaddressparser_tokyo_no_prefecture_with_space(self):
        data = '千代田区 丸の内1-9-2グラントウキョウサウスタワー23階'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '千代田区' )
        assert ( addr.street == '丸の内1-9-2グラントウキョウサウスタワー23階')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13101)
        assert ( addr.geodetic == ( 35.68156, 139.767201))
        assert ( addr.__str__()
           ==  '東京都千代田区丸の内1-9-2グラントウキョウサウスタワー23階' )
