import os
import numpy as np
import pandas as pd
import re
from typing import Optional, Union, Any, NamedTuple
from dataclasses import dataclass, field
from pathlib import Path
from .singledispatchmethod import singledispatchmethod
from .immutable_dict import ImmutableDict
from .checkdigit import calc_checkdigit, validate_checkdigit
from .jp_prefecture import JpPrefecture
from .utils import is_alpha

class Geodetic(NamedTuple):
    latitude: float
    longitude: float

@dataclass
class JpTown(object):
    prefecture: str
    city: str
    town: str
    prefCode: Optional[int]=field(repr=False, default=None)
    cityCode: Optional[int]=field(repr=False, default=None)
    geodetic: Optional[Geodetic]=field(repr=False, default=None)

class JpCity(JpPrefecture):
    def __init__(self, enable_town:bool=False):
        # City Code: JIS X 0402

        super().__init__()
        self.cities = pd.read_csv(Path(__file__).parent / 'data/cities.csv',
                                  index_col = 0)
        self.cities['prefCode'] = pd.to_numeric(self.cities['prefCode'],
                                                downcast='integer')
        self.cities['cityCode'] = pd.to_numeric(self.cities['cityCode'],
                                                downcast='integer')
        self.cities['latitude'].astype(float)
        self.cities['longitude'].astype(float)
        self.cities['bigCityFlag'] = pd.to_numeric(self.cities['bigCityFlag'],
                                                downcast='integer')

        self.enable_town = os.environ.get('JP_PREFECTURE_ENABLE_TOWN',
                                           default=enable_town)
        if self.enable_town:
            self.towns = pd.read_csv(Path(__file__).parent / 'data/towns.csv',
                                  index_col = 0)
            self.towns['prefCode'] = pd.to_numeric(self.towns['prefCode'],
                                                downcast='integer')
            self.towns['cityCode'] = pd.to_numeric(self.towns['cityCode'],
                                                downcast='integer')
            self.towns['latitude'].astype(float)
            self.towns['longitude'].astype(float)
            self.towns['bigCityFlag'] = pd.to_numeric(self.towns['bigCityFlag'],
                                                downcast='integer')

        self.__citycode2name = ImmutableDict({
            code: name
            for code, name in zip(self.cities.cityCode,
                                  self.cities.cityName)
        })

        self.__citycode2alphabet = ImmutableDict({
            code: alphabet
            for code, alphabet in zip(self.cities.cityCode,
                                  self.cities.cityAlphabet)
        })

        self.__cityname2code = ImmutableDict({
            **{name: code
               for name, code in zip(self.cities.cityName,
                                     self.cities.cityCode)},
            **{name: code
               for name, code in zip(self.cities.cityAlphabet,
                                     self.cities.cityCode)},
            **{name.title(): code
               for name, code in zip(self.cities.cityAlphabet,
                                     self.cities.cityCode)},
        })

        self.__cityname2alphabet = ImmutableDict({
            **{name: alphabet
               for name, alphabet in zip(self.cities.cityName,
                                     self.cities.cityAlphabet)},
            **{name: alphabet
               for name, alphabet in zip(self.cities.cityAlphabet,
                                     self.cities.cityAlphabet)},
            **{name.title(): alphabet
               for name, alphabet in zip(self.cities.cityAlphabet,
                                     self.cities.cityAlphabet)},
        })

        self.__cityalphabet2name = ImmutableDict({
            **{alphabet: name
               for alphabet, name in zip(self.cities.cityName,
                                     self.cities.cityName)},
            **{alphabet: name
               for alphabet, name in zip(self.cities.cityAlphabet,
                                     self.cities.cityName)},
            **{alphabet.title(): name
               for alphabet, name in zip(self.cities.cityAlphabet,
                                     self.cities.cityName)},
        })

    @singledispatchmethod
    def cityname2code(self,
            arg: Any
        ) -> Union[Optional[Union[int,str]],list,pd.Series]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @cityname2code.register(type(None))
    def _cityname2code_none(self,
            name: str,
            ignore_case: bool=False,
            checkdigit: bool=False,
            as_str: bool=False,
        ) -> Optional[Union[int,str]]:
        """ Catch None and return None """
        return None

    @cityname2code.register(str)
    def _cityname2code_str(self,
            name: str,
            ignore_case: bool=False,
            checkdigit: bool=False,
            as_str: bool=False,
        ) -> Optional[str]:
        """ Convert cityName to cityCode """
        try:
            name = name.title() if ignore_case else name
            code = self.__cityname2code[name]
            if code:
                code = str(code).zfill(5) if as_str else code
                code = calc_checkdigit(code) if checkdigit else code
        except KeyError:
            code = None
        return code

    @cityname2code.register(re.Pattern)
    def _cityname2code_re(self,
            name: re.Pattern,
            ignore_case: bool=False,
            checkdigit: bool=False,
            as_str: bool=False,
        ) -> list:
        """ Convert cityName to cityCode """
        cities = [ re.search(name, x) for x in self.__cityname2code.keys() ]
        codes = list()
        for x in cities:
            if x:
                code = self.__cityname2code[x.group(0)]
                if code not in codes:
                    codes.append(code)
        return codes

    @cityname2code.register(list)
    def _cityname2code_list(self,
            name_list: list,
            ignore_case: bool=False,
            checkdigit: bool=False,
            as_str: bool=False,
        ) -> list:
        """ Convert list of cityName to cityCode """
        code = [self.cityname2code(x, ignore_case, checkdigit)
                                   for x in name_list]
        return code

    @cityname2code.register(pd.Series)
    def _cityname2code_series(self,
            name_series: pd.Series,
            ignore_case: bool=False,
            checkdigit: bool=False,
            as_str: bool=False,
        ) -> pd.Series:
        """ Convert pandas series of cityName to cityCode """
        try:
            name_series = ( name_series.str.title()
                            if ignore_case else name_series )
            code = name_series.map(self.__cityname2code)
            code = code.map(calc_checkdigit) if checkdigit else code
        except KeyError:
            code = pd.Series([])
        return code


    @singledispatchmethod
    def citycode2name(self, arg: Any) -> Union[Optional[str],list,pd.Series]:
        """ Convert cityCode to cityName """
        raise TypeError('Unsupport Type')

    @citycode2name.register(type(None))
    def _citycode2name_none(self,
            code: None,
            ascii: bool=False,
        ):
        return None

    @citycode2name.register(int)
    def _citycode2name_int(self,
            code: int,
            ascii: bool=False,
        ) -> Optional[str]:
        """ Convert cityCode to cityName
            if set ``True`` to ascii, return cityname as alphabet_name
        """
        if len(str(code)) == 6:
            code = validate_checkdigit(code)  # type: ignore
        try:
            name = ( self.__citycode2alphabet[code]
                     if ascii else self.__citycode2name[code] )
        except KeyError:
            name = None
        return name

    @citycode2name.register(str)
    def _citycode2name_str(self,
            code: str,
            ascii: bool=False,
        ) -> Optional[str]:
        """ Convert cityCode to cityName
            if set ``True`` to ascii, return cityname as alphabet_name
        """
        if len(code) == 6:
            code = validate_checkdigit(int(code), 5)  # type: ignore
        else:
            code = int(code)   # type: ignore
        try:
            name = ( self.__citycode2alphabet[code]
                     if ascii else self.__citycode2name[code] )
        except:
            name = None
        return name

    @citycode2name.register(list)
    def _citycode2name_list(self,
            code_list: list,
            ascii: bool=False,
        ) -> list:
        """ Convert list of cityCode to CityName
            if set ``True`` to ascii, return cityname as alphabet_name
        """
        name = [self.citycode2name(x, ascii) for x in code_list]
        return name

    @citycode2name.register(pd.Series)
    def _citycode2name_series(self,
            code_series: pd.Series,
            ascii: bool=False,
        ) -> pd.Series:
        """ Convert pandas series of cityCode to cityName
            if set ``True`` to ascii, return cityname as alphabet_name
        """
        try:
            code_series.astype(int)
            name = ( code_series.map(self.__citycode2alphabet)
                     if ascii else code_series.map(self.__citycode2name) )
        except:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def cityname2normalize(self, arg: Any
        ) -> Union[Optional[int],list,pd.Series]:
        """ Normalize cityName
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        raise TypeError('Unsupport Type')

    @cityname2normalize.register(type(None))
    def _cityname2normalize_none(self,
            name: None,
            ascii: bool=False,
            ignore_case: bool=False
        ):
        return None

    @cityname2normalize.register(str)
    def _cityname2normalize_str(self,
            name: str,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> Optional[str]:
        """ Normalize cityName
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        try:
            name = name.title() if ignore_case else name
            name = ( self.__cityname2alphabet[name]
                     if ascii else self.__cityalphabet2name[name] )
        except KeyError:
            name = None    # type: ignore
        return name

    @cityname2normalize.register(list)
    def _cityname2normalize_list(self,
            name_list: list,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> list:
        """ Convert list of cityName to cityCode
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        name = [self.cityname2normalize(x,ascii,ignore_case)
                                        for x in name_list]
        return name

    @cityname2normalize.register(pd.Series)
    def _cityname2normalize_series(self,
            name_series: pd.Series,
            checkdigit=False,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to cityCode
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        try:
            name_series = ( name_series.str.title()
                            if ignore_case else name_series )
            name = ( name_series.map(self.__cityname2alphabet)
                     if ascii else name_series.map(self.__cityalphabet2name) )
        except KeyError:
            name = pd.Series([])
        return name

    def get_prefcode(self, citycode: Union[int, str])-> Optional[int]:
        if isinstance(citycode, int):
            citycode = str(citycode)
        try:
            return int(citycode[:2])
        except:
            return None

    def citycode2normalize(self,
            citycode: Union[int, str],
            as_str: bool=False,
        )-> Optional[Union[int, str]]:
        if isinstance(citycode, int):
            citycode = str(citycode).zfill(5)

        try:
            if len(citycode) == 6:
                citycode = validate_checkdigit(citycode)  # type: ignore
            citycode = citycode if as_str else int(citycode) # type: ignore
        except:
            citycode = None       # type: ignore

        return citycode

    def findcity(self,
            name: re.Pattern,
            ignore_case: bool=False,
            ascii: bool=False,
        ) -> list:
        flag = re.IGNORECASE if ignore_case else 0
        result = [ re.search(name, x, flag)
                   for x in self.__cityname2code.keys() ]
        cities = list()
        for x in result:
            if x:
                city = x.group(0).title()
                if city in self.__cityname2code.keys():
                    name = self.__cityname2alphabet[city] if ascii else city
                    if name not in cities:
                        cities.append(name)

        return cities

    def findtown(self,
            name: re.Pattern,
            city: Optional[Union[str,int]]=None
        )->list:
        if not self.enable_town:
            raise NotImplementedError('Town data does not enabled.')

        if city:
            city = self.cityname2code(city)   # type: ignore
            df = self.towns[self.towns['cityCode'] == city]
        else:
            df = self.towns.copy()
        df = df[df['town'].str.match(name)]
        df['cityName'] = df['cityCode'].map(self.__citycode2name)
        df['prefecture'] = df['cityName'].map(self.cityname2prefecture)
        df['prefCode'] = df['cityName'].map(self.cityname2prefcode)
        df = df.loc[:, [
                    'prefecture', 'prefCode',
                    'cityName', 'cityCode',
                    'town', 'latitude', 'longitude']]
        towns_list = list()
        for town in df.values:
            towns_list.append( JpTown(
                     prefecture=town[0], prefCode=town[1],
                     city=town[2], cityCode=town[3],
                     town=town[4],
                     geodetic=Geodetic(town[5], town[6])
                 )
              )
        return towns_list

    @singledispatchmethod
    def cityname2prefcode(self, arg: Any,
        ) -> Union[Optional[int],list,pd.Series]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @cityname2prefcode.register(type(None))
    def _cityname2prefcode_none(self,
            name: None,
            ignore_case: bool=False
        ):
        """ Catch None and return None """
        return None

    @cityname2prefcode.register(str)
    def _cityname2prefcode_str(self,
            name: str,
            ignore_case: bool=False
        ) -> Optional[int]:
        """ Convert CityName to Prefecture Code"""
        name = name.title() if ignore_case else name
        code = self.__cityname2code[name]
        prefcode = self.get_prefcode(code)
        return prefcode

    @cityname2prefcode.register(list)
    def _cityname2prefcode_list(self,
            name_list: list,
            ignore_case: bool=False
        ) -> list:
        """ Convert list of cityName to Prefecture Code """
        code = [self.cityname2prefcode(x, ignore_case) for x in name_list]
        return code

    @cityname2prefcode.register(pd.Series)
    def _cityname2prefcode_series(self,
            name_series: pd.Series,
            ignore_case: bool=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to Prefecture Code """
        try:
            name_series = ( name_series.str.title()
                            if ignore_case else name_series )
            code = name_series.map(self.__cityname2code)
            code = code.map(self.get_prefcode)
        except KeyError:
            code = pd.Series([None])
        return code

    @singledispatchmethod
    def cityname2prefecture(self, arg: Any) -> Union[Optional[str],list,pd.Series]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @cityname2prefecture.register(type(None))
    def _cityname2prefecture_none(self,
            name: None,
            ascii: bool=False,
            ignore_case: bool=False
        ):
        """ Catch None and return None """
        return None

    @cityname2prefecture.register(str)
    def _cityname2prefecture_str(self,
            name: str,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> Optional[str]:
        """ Convert CityName to Prefecture Name"""
        name = name.title() if ignore_case else name
        code = self.cityname2prefcode(name)
        name = code and self.code2name(code, ascii)  # type: ignore
        return name

    @cityname2prefecture.register(list)
    def _cityname2prefecture_list(self,
            name_list: list,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> list:
        """ Convert list of CityName to Prefecture Name"""
        name = [self.cityname2prefecture(x, ascii,ignore_case)
                                         for x in name_list]
        return name

    @cityname2prefecture.register(pd.Series)
    def _cityname2prefecture_series(self,
            name_series: pd.Series,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to Prefecture Name """
        try:
            name_series = ( name_series.str.title()
                            if ignore_case else name_series )
            code = name_series.map(self.cityname2prefcode)
            name = code.apply(self.code2name, ascii=ascii)
        except KeyError:
            # v = [None]
            name = pd.Series([None])
        # return pd.Series(v)
        return name


    @singledispatchmethod
    def cityname2geodetic(self,
            arg: Any,
        ) -> Union[Optional[tuple],list,pd.DataFrame]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @cityname2geodetic.register(str)
    def _cityname2geodetic_str(self,
            name: str,
            ignore_case: bool=False
        ) -> Optional[tuple]:
        """ Return Latitude and Longitude of CityName """
        code = self.cityname2code(name, ignore_case)
        if code:
            city = self.cities.loc[self.cities['cityCode'] == code]
            geodetic = Geodetic( city['latitude'].values[0],
                         city['longitude'].values[0] )
        else:
            geodetic = None    # type: ignore
        return geodetic

    @cityname2geodetic.register(list)
    def _cityname2geodetic_list(self,
            name_list: list,
            ignore_case: bool=False
        ) -> list:
        """ Return Latitude and Longitude of CityName """
        code = self.cityname2code(name_list, ignore_case)
        geodetic = list()
        for c in code:        # type: ignore
            city = self.cities.loc[self.cities['cityCode'] == c]
            pos = Geodetic( city['latitude'].values[0],
                    city['longitude'].values[0] )
            geodetic.append(pos)
        if len(geodetic) == 0:
            geodetic = None    # type: ignore
        return geodetic

    @cityname2geodetic.register(pd.Series)
    def _cityname2geodetic_series(self,
            name_series: pd.Series,
            ignore_case: bool=False
        ) -> pd.DataFrame:
        """ Return Latitude and Longitude of CityName """
        code = name_series.apply(self.cityname2code, ignore_case)
        geodetic = self.cities.loc[self.cities['cityCode'].isin(code.values),
                                   ['latitude','longitude']]
        geodetic.insert(0, 'cityName', name_series.values )
        return geodetic

    @singledispatchmethod
    def citycode2geodetic(self,
            arg: Any,
        ) -> Union[Optional[tuple],list,pd.DataFrame]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @citycode2geodetic.register(str)
    @citycode2geodetic.register(int)
    def _citycode2geodetic(self,
            code: Union[int,str],
            ignore_case: bool=False
        ) -> Optional[tuple]:
        """ Return Latitude and Longitude of CityName """

        citycode = self.citycode2normalize(code)
        if citycode:
            city = self.cities.loc[self.cities['cityCode'] == citycode]
            geodetic = Geodetic( city['latitude'].values[0],
                         city['longitude'].values[0] )
        else:
            geodetic = None    # type: ignore
        return geodetic

    @citycode2geodetic.register(list)
    def _citycode2geodetic_list(self,
            code_list: list,
            ignore_case: bool=False
        ) -> list:
        """ Return Latitude and Longitude of CityName """
        city_codes = [ self.citycode2normalize(x) for x in code_list ]
        geodetic = list()
        try:
            for c in city_codes:
                city = self.cities.loc[self.cities['cityCode'] == c]
                pos = Geodetic( city['latitude'].values[0],
                        city['longitude'].values[0] )
                geodetic.append(pos)
        except:
            geodetic = list()

        if len(geodetic) == 0:
            geodetic = None    # type: ignore
        return geodetic

    @citycode2geodetic.register(pd.Series)
    def _citycodegeodetic_series(self,
            code_series: pd.Series,
            ignore_case: bool=False
        ) -> pd.DataFrame:
        """ Return Latitude and Longitude of CityName """
        city_codes =  code_series.map(self.citycode2normalize)
        geodetic = self.cities.loc[( self.cities['cityCode']
                                         .isin(city_codes.values)),
                                     ['cityCode','latitude','longitude']]
        return geodetic

    @singledispatchmethod
    def validate_city(self, arg: Any) -> Optional[Union[bool,list,pd.Series]]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @validate_city.register(type(None))
    def _validate_city_none(self,
            name: None,
            ignore_case: bool=False
        ) -> bool:
        """ Catch None and return None """
        return False

    @validate_city.register(str)
    def _validate_city_str(self,
            name: str,
            ignore_case: bool=False
        ) -> bool:
        """ validate_city a cityName """
        try:
            name = name.title() if ignore_case else name
            v = name in self.__cityname2code.keys()
        except:
            v = False
        return v

    @validate_city.register(list)
    def _validate_city_list(self,
            name_list: list,
            ignore_case: bool=False
        ) -> list:
        """ validate_city list of cityName """
        try:
            v = [ self.validate_city(x,ignore_case) for x in name_list]
        except:
            v = [False]
        return v

    @validate_city.register(pd.Series)
    def _validate_city_series(self,
            name_series: pd.Series,
            ignore_case: bool=False
        ) -> pd.Series:
        """ validate_city pandas series of cityName """
        try:
            v = [ self.validate_city(x,ignore_case)
                                     for x in np.asarray(name_series)]
        except KeyError:
            v = [False]
        return pd.Series(v)

jp_cities = JpCity()
