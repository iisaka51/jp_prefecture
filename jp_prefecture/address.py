import re
from dataclasses import dataclass
from typing import Optional
from .jp_cities import jp_cities as jp

class JpAddressError(BaseException):
    pass

@dataclass
class JpAddress(object):
    zipcode: Optional[str]=None
    prefecture: Optional[str]=None
    city: Optional[str]=None
    street: Optional[str]=None

class JpAddressParser(object):
    __zip_pattern = (
       r'(〒)? *(\d{3}-\d{4}|\d{7})? *'
    )
    __pattern = (
        r'(〒? *\d{3}-\d{4}|〒? *\d{7})? *'
        r'(...?[都道府県])?'
        r'('
          r'(?:'
          r'旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|'
          r'東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|'
          r'蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|'
          r'大村|宮古|富良野|別府|佐伯|黒部|小諸|塩尻|玉野|周南'
          r')市|'
        r'(?:余市|高市|[^市]{2,3}?)'
        r'郡(?:玉村|大町|.{1,5}?)[町村]|'
        r'(?:.{1,4}市)?[^町]{1,4}?区|'
        r'.{1,7}?[市町村])(.+)'
    )

    def __init__(self):
        self.address_re = re.compile(self.__pattern, re.UNICODE)
        self.zip_re = re.compile(self.__zip_pattern, re.UNICODE)

    def parse_address(self, address):
        r = self.address_re.search(address)
        result = None
        if r:
            result = JpAddress(*r.groups())
            result.zipcode = self.zipcode2normalize(result.zipcode)
            if not result.prefecture:
                result.prefecture = jp.cityname2prefecture(result.city)
        return result

    def zipcode2normalize(self,
            zipcode: Optional[str]=None
        ) -> Optional[str]:
        if not zipcode:
            return None

        r = self.zip_re.search(zipcode)
        result = None
        if r:
            symbol = r.group(1)
            code = r.group(2)
            if not code:
                return None
            code = code.replace('-','')
            code = '{}-{}'.format(code[:3], code[3:])
            result = '〒' + code
        return result