import numpy as np
import pandas as pd
from typing import List, Optional, Union, Any
from pathlib import Path
from .singledispatchmethod import singledispatchmethod
from .immutable_dict import ImmutableDict
from .checkdigit import calc_checkdigit, validate_checkdigit
from .jp_prefecture import JpPrefecture
from .utils import is_alpha

class JpCityCode(JpPrefecture):
    def __init__(self):
        # Cities Code: JIS X 0402

        super().__init__()
        self.cities = pd.read_csv(Path(__file__).parent / 'data/cities.csv',
                                  index_col = 0)

        self.cities['prefCode'] = pd.to_numeric(self.cities['prefCode'],
                                                downcast='integer')
        self.cities['cityCode'] = pd.to_numeric(self.cities['cityCode'],
                                                downcast='integer')
        self.cities['bigCityFlag'] = pd.to_numeric(self.cities['bigCityFlag'],
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
    def cityname2code(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @cityname2code.register(type(None))
    def _cityname2code_none(self,
            name: str,
            ignore_case: bool=False,
            checkdigit: bool=False
        ) -> Optional[int]:
        """ Catch None and return None """
        return None

    @cityname2code.register(str)
    def _cityname2code_str(self,
            name: str,
            ignore_case: bool=False,
            checkdigit: bool=False
        ) -> Optional[int]:
        """ Convert cityName to cityCode """
        try:
            name = [name, name.title()][ignore_case]
            code = self.__cityname2code[name]
            code = code and [code, calc_checkdigit(code)][checkdigit]
        except KeyError:
            code = None
        return code

    @cityname2code.register(list)
    def _cityname2code_list(self,
            name_list: List,
            ignore_case: bool=False,
            checkdigit: bool=False
        ) -> List:
        """ Convert list of cityName to cityCode """
        code = [self.cityname2code(x, ignore_case, checkdigit)
                                   for x in name_list]
        return code

    @cityname2code.register(pd.Series)
    def _cityname2code_series(self,
            name_series: pd.Series,
            ignore_case: bool=False,
            checkdigit: bool=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to cityCode """
        try:
            name_series = [name_series,
                           name_series.str.title()][ignore_case]
            code = name_series.map(self.__cityname2code)
            code = [code,
                    code.map(calc_checkdigit)][checkdigit]
        except KeyError:
            code = pd.Series([])
        return code


    @singledispatchmethod
    def citycode2name(self, arg: Any) -> Optional[str]:
        """ Convert cityCode to cityName """
        raise TypeError('Unsupport Type')

    @citycode2name.register(type(None))
    def _citycode2name_int(self,
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
            code = validate_checkdigit(code)
        try:
            name = [ self.__citycode2name[code],
                     self.__citycode2alphabet[code]][ascii]
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
            code = validate_checkdigit(int(code), 5)
        else:
            code = int(code)
        try:
            name = [ self.__citycode2name[code],
                     self.__citycode2alphabet[code]][ascii]
        except:
            name = None
        return name

    @citycode2name.register(list)
    def _citycode2name_list(self,
            code_list: List,
            ascii: bool=False,
        ) -> List:
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
            name = [ code_series.map(self.__citycode2name),
                     code_series.map(self.__citycode2alphabet)][ascii]
        except:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def cityname2normalize(self, arg: Any) -> Optional[int]:
        """ Normalize cityName
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        raise TypeError('Unsupport Type')

    @cityname2normalize.register(type(None))
    def _cityname2normalize_str(self,
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
        ) -> Optional[int]:
        """ Normalize cityName
            if set ``True`` to ascii, return cityName as alphabet_name
        """
        try:
            name = [name, name.title()][ignore_case]
            name = [ self.__cityalphabet2name[name],
                     self.__cityname2alphabet[name] ][ascii]
        except KeyError:
            name = None
        return name

    @cityname2normalize.register(list)
    def _cityname2normalize_list(self,
            name_list: List,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> List:
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
            name_series = [name_series,
                           name_series.str.title()][ignore_case]
            name = [ name_series.map(self.__cityalphabet2name),
                     name_series.map(self.__cityname2alphabet) ][ascii]
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

    @singledispatchmethod
    def cityname2prefcode(self, arg: Any) -> Optional[int]:
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
        name = [name, name.title()][ignore_case]
        code = self.__cityname2code[name]
        prefcode = self.get_prefcode(code)
        return prefcode

    @cityname2prefcode.register(list)
    def _cityname2prefcode_list(self,
            name_list: List,
            ignore_case: bool=False
        ) -> List[Optional[int]]:
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
            name_series = [name_series,
                           name_series.str.title()][ignore_case]
            code = name_series.map(self.__cityname2code)
            code = code.map(self.get_prefcode)
        except KeyError:
            code = pd.Series([None])
        return code

    @singledispatchmethod
    def cityname2prefecture(self, arg: Any) -> Optional[int]:
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
        name = [name, name.title()][ignore_case]
        code = self.cityname2prefcode(name)
        name = code and self.code2name(code, ascii)
        return name

    @cityname2prefecture.register(list)
    def _cityname2prefecture_list(self,
            name_list: list,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> List[Optional[str]]:
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
            name_series = [name_series,
                           name_series.str.title()][ignore_case]
            code = name_series.map(self.cityname2prefcode)
            name = code.apply(self.code2name, ascii=ascii)
        except KeyError:
            # v = [None]
            name = pd.Series([None])
        # return pd.Series(v)
        return name

    @singledispatchmethod
    def validate_city(self, arg: Any) -> Optional[str]:
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
            name = [name, name.title()][ignore_case]
            v = name in self.__cityname2code.keys()
        except:
            v = False
        return v

    @validate_city.register(list)
    def _validate_city_list(self,
            name_list: List,
            ignore_case: bool=False
        ) -> List[bool]:
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

jp_cities = JpCityCode()
