import os
import sys
sys.path.insert(0,"../jp_prefecture")
os.environ.update({'JP_PREFECTURE_ENABLE_TOWN': '1'})
from jp_prefecture.address import JpAddressParser, JpAddress

class TestClass:
    parser = JpAddressParser()

    def test_jpaddressparser_case01(self):
        data = '〒617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26209)
        assert ( addr.geodetic == (34.928769, 135.696847))
        assert ( str(addr)
                 == '〒617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室' )

    def test_jpaddressparser_case02(self):
        data = '〒617-0824 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170824' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_case03(self):
        data = '6170824 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170824' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '〒617-0824 京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_case04(self):
        data = '長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_case05(self):
        data = '京都長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '京都府長岡京市天神２丁目１５−１３')


    def test_jpaddressparser_case06(self):
        data = '京都 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_case07(self):
        data = '京都府 長岡京市天神２丁目１５−１３'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '天神２丁目１５−１３')
        assert ( addr.geodetic == (34.923314, 135.685162))
        assert ( str(addr)
                 == '京都府長岡京市天神２丁目１５−１３')

    def test_jpaddressparser_case08(self):
        data = '京都市下京区烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))

    def test_jpaddressparser_case09(self):
        data = '京都市 下京区烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))
        assert ( str(addr)
                 == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

    def test_jpaddressparser_case10(self):
        data = '京都 下京区 烏丸通七条下ル 東塩小路町 721-1'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '京都市下京区' )
        assert ( addr.street == '烏丸通七条下ル 東塩小路町 721-1')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26106)
        assert ( addr.geodetic == (35.002973, 135.764009))
        assert ( str(addr)
                 == '京都府京都市下京区烏丸通七条下ル 東塩小路町 721-1' )

    def test_jpaddressparser_case11(self):
        data = '東京都渋谷区桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case12(self):
        data = '東京都 渋谷区桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case13(self):
        data = '東京渋谷区桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case14(self):
        data = '東京 渋谷区桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case15(self):
        data = '東京 渋谷区 桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case16(self):
        data = '東京　渋谷区　桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )

    def test_jpaddressparser_case17(self):
        data = '渋谷区桜丘町１２−３４'
        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '渋谷区' )
        assert ( addr.street == '桜丘町１２−３４')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13113)
        assert ( addr.geodetic == ( 35.655642, 139.700634) )
        assert ( str(addr)
                 == '東京都渋谷区桜丘町１２−３４' )
