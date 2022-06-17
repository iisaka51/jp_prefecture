import sys
sys.path.insert(0,"../jp_prefecture")

from jp_prefecture.address import JpAddressParser, JpAddress

class TestClass:
    addr = JpAddressParser()

    def test_jpaddressparser_hokaido_no_zip(self):
        data = '北海道札幌市西区二十四軒１条７丁目'
        expect = JpAddress(None, '北海道', '札幌市西区', '二十四軒１条７丁目')

        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_kyoto_with_zip_not_symnol(self):
        data = '617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'
        expect = JpAddress('〒617-0826', '京都府', '長岡京市',
                        '開田1丁目-2-3 アパート123号室')

        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_kyoto_apartment(self):
        data = '京都府長岡京市開田1丁目-2-3 アパート123号室'
        expect = JpAddress(None, '京都府', '長岡京市',
                        '開田1丁目-2-3 アパート123号室')

        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_kyoto_apartment_with_zip(self):
        data =  '〒617-0826 京都府長岡京市開田1丁目-2-3 アパート123号室'
        expect =  JpAddress('〒617-0826', '京都府', '長岡京市',
                        '開田1丁目-2-3 アパート123号室')

        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_7digit_zip_with_symbol(self):
        data = '〒6170826 京都府長岡京市開田1丁目-2-3 アパート123号室'
        expect = JpAddress('〒617-0826', '京都府', '長岡京市',
                        '開田1丁目-2-3 アパート123号室')
        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_7digit_zip(self):
        data = '6170826 京都府長岡京市開田1丁目-2-3 アパート123号室'
        expect = JpAddress('〒617-0826', '京都府', '長岡京市',
                        '開田1丁目-2-3 アパート123号室')
        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_no_prefecture(self):
        data = '京都市下京区烏丸通七条下ル 東塩小路町 721-1'
        expect = JpAddress(None, '京都府', '京都市下京区',
                        '烏丸通七条下ル 東塩小路町 721-1')
        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_tokyo_no(self):
        data = '東京都千代田区丸の内1-9-2グラントウキョウサウスタワー23階'
        expect = JpAddress(None, '東京都', '千代田区',
                        '丸の内1-9-2グラントウキョウサウスタワー23階')

        result = self.addr.parse_address(data)
        assert (result == expect)

    def test_jpaddressparser_tokyo_no_prefecture(self):
        data = '千代田区丸の内1-9-2グラントウキョウサウスタワー23階'
        expect = JpAddress(None, '東京都', '千代田区',
                        '丸の内1-9-2グラントウキョウサウスタワー23階')

        result = self.addr.parse_address(data)
        assert (result == expect)
