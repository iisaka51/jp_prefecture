import sys
sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.address import JpAddressParser, JpAddress

class TestClass:
    parser = JpAddressParser()

    def test_jpaddressparser_hokaido_no_zip(self):
        data = '北海道札幌市西区二十四軒１条７丁目'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '北海道' )
        assert ( addr.city == '札幌市西区' )
        assert ( addr.street == '二十四軒１条７丁目' )
        assert ( addr.prefCode == 1)
        assert ( addr.cityCode == 1107)
        assert ( addr.geodetic == (43.079715, 141.308758))


    def test_jpaddressparser_kyoto_with_zip_not_symnol(self):
        data = '617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26209)
        assert ( addr.geodetic == (34.937151, 135.676083))


    def test_jpaddressparser_kyoto_apartment_with_zip(self):
        data =  '〒617-0826 長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.geodetic == (34.937151, 135.676083))


    def test_jpaddressparser_7digit_zip_with_symbol(self):
        data = '〒6170826 京都府長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26209)
        assert ( addr.geodetic == (34.937151, 135.676083))

    def test_jpaddressparser_7digit_zip(self):
        data = '6170826 京都府長岡京市開田1丁目-2-3 アパート123号室'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == '6170826' )
        assert ( addr.prefecture == '京都府' )
        assert ( addr.city == '長岡京市' )
        assert ( addr.street == '開田1丁目-2-3 アパート123号室')
        assert ( addr.prefCode == 26)
        assert ( addr.cityCode == 26209)
        assert ( addr.geodetic == (34.937151, 135.676083))


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

    def test_jpaddressparser_tokyo_no_prefecture(self):
        data = '千代田区丸の内1-9-2グラントウキョウサウスタワー23階'

        addr = self.parser.parse_address(data)
        assert ( addr.zipCode == None )
        assert ( addr.prefecture == '東京都')
        assert ( addr.city == '千代田区' )
        assert ( addr.street == '丸の内1-9-2グラントウキョウサウスタワー23階')
        assert ( addr.prefCode == 13)
        assert ( addr.cityCode == 13101)
        assert ( addr.geodetic == (35.670812, 139.754182))
