import re
from dataclasses import dataclass, InitVar, field
from typing import Optional
from .jp_cities import jp_cities as jp
from .jp_cities import JpCity, Geodetic
from .jp_numbers import JpNumberParser
import snoop

class JpAddressError(BaseException):
    pass

@dataclass
class JpAddress(object):
    zipCode: str
    prefecture: str
    city: str
    street: str
    prefCode: Optional[int]=field(init=False, repr=False, default=None)
    cityCode: Optional[int]=field(init=False, repr=False, default=None)
    geodetic: Optional[Geodetic]=field(init=True, repr=False, default=None)
    validate: Optional[bool]=field(init=False, repr=False, default=None)

    def __post_init__(self):
        zip_parser = JpZipCode()
        self.zipCode = zip_parser.zip2normalize(self.zipCode)
        if self.city:
            self.cityCode = jp.cityname2code(self.city)
            self.city = jp.cityname2normalize(self.city)
        else:
            self.city = None

        if not self.prefecture:
            self.prefecture = jp.cityname2prefecture(self.city)
        else:
            self.prefecture = jp.name2normalize(self.prefecture)
        self.prefCode = jp.name2code(self.prefecture)

        if not self.geodetic:
            self.geodetic = jp.cityname2geodetic(self.city)
            self.validate = True
        elif not self.city or self.geodetic == Geodetic(0,0):
            self.geodetic = None
            self.validate = False
        else:
            self.validate = True

    def __str__(self):
        if self.zipCode:
            zip= f'〒{self.zipCode[:3]}-{self.zipCode[3:]} '
        else:
            zip = ''
        address = (
            f'{zip}'
            f'{self.prefecture}'
            f'{self.city}'
            f'{self.street}'
        )
        return address

class JpZipCode(object):
    __zip_pattern = (
       r'(〒)? *(\d{3}-\d{4}|\d{7})? *'
    )
    def __init__(self):
        self.zip_re = re.compile(self.__zip_pattern, re.UNICODE)

    def zip2normalize(self,
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
            result = code.replace('-','')
        return result

class JpAddressParser(JpZipCode):
    __address_pattern = (
        r'(〒? *\d{3}-\d{4}|〒? *\d{7})? *'
        r'(?P<Prefecture>...?[都道府県]|..?)? *'
        r'('
          r'(?:'
          r'旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|'
          r'東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|'
          r'蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|'
          r'大村|宮古|富良野|別府|佐伯|黒部|小諸|塩尻|玉野|周南'
          r')市 *|'
        r'(?:余市|高市|[^市]{2,3}?)'
        r'郡(?:玉村|大町|.{1,5}?)[町村]|'
        r'(?:.{1,4}市)?[^町]{1,4}?区|'
        r'.{1,7}?[市町村])(.+)'
    )

    def __init__(self, enable_town: bool=False):
        self.address_re = re.compile(self.__address_pattern, re.UNICODE)
        self.jp_number = JpNumberParser()
        self.enable_town = enable_town
        self.jp = JpCity(enable_town=True)
        super().__init__()

    @snoop
    def parse_address(self, address):
        address = address.replace('\u3000', ' ')
        r = self.address_re.search(address)
        result = None
        if r:
            prefecture = jp.name2normalize(r.group('Prefecture'))
            if not prefecture:
                city = r.group('Prefecture') + r.group(3)
                city_normal = self.jp.cityname2normalize(city)
                if not city_normal:
                    city = re.split('[区市]', city)[0]
                    try:
                        city = self.jp.findcity(city + '[区市].*')[0]
                    except:
                        city = ''
                    city_normal = self.jp.cityname2normalize(city)
            else:
                city = r.group(3).replace(' ', '')
                city = city.replace('\u3000', '') # Kanji Space
                city_normal = self.jp.cityname2normalize(city)
            if not city_normal:
                city = jp.findcity(r.group('Prefecture') + '.*' + city)
                if city:
                    city = city[0]
            else:
                city = city_normal
            v  = address.split(city)
            if len(v) == 2:
                street = re.sub('^[ 　]*', '', v[1])
            else:
                if prefecture:
                    street = re.sub('^[ 　]*', '', r.group(4))
                else:
                    re_groups = list(r.groups())
                    street = str().join(re_groups[2:])
                    street = re.sub('^[ 　]*', '', street)

            normalized_street = self.jp_number.normalize_kanjinumber(street)
            town = normalized_street.split('丁目')
            if len(town) >1:
                town = town[0] + '丁目'
            else:
                town = re.split('[-ー]', normalized_street)
                if len(town) >1:
                    town = town[0] + '丁目'
                else:
                    town = re.split('[町村]', normalized_street)[0]
            try:
                if self.enable_town:
                    town = self.jp.findtown(town, city)[0]
                    geodetic = town.geodetic
                else:
                    geodetic = self.jp.cityname2geodetic(city)
            except:
                geodetic = Geodetic(0,0)

            result = JpAddress(zipCode=r.group(1),
                               prefecture=prefecture, city=city,
                               street=street,
                               geodetic=geodetic,
                               )
        return result

