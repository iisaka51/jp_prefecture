import numpy as np
import pandas as pd
from typing import List, Optional, Any
from pathlib import Path
from .singledispatchmethod import singledispatchmethod
from .immutable_dict import ImmutableDict
from .checkdigit import calc_checkdigit, validate_checkdigit
from .jp_prefecture import JpPrefecture

class JpCityCode(JpPrefecture):
    def __init__(self):
        # Cities Code: JIS X 0402

        super().__init__()
        self.cities = pd.read_csv(Path(__file__).parent / 'data/cities.csv',
                                  index_col = 0)

        self.__citycode2name = ImmutableDict({
            code: name
            for name, code in zip(self.cities.cityName,
                                  self.cities.cityCode)
        })

        self.__name2citycode = ImmutableDict({
            **{name: code
               for name, code in zip(self.cities.cityName,
                                     self.cities.cityCode)},
        })

    @singledispatchmethod
    def name2citycode(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2citycode.register(str)
    def _name2citycode_str(self,
            name: str,
            with_checkdigit=False
        ) -> Optional[int]:
        """ Convert cityName to cityCode """
        try:
            code = self.__name2citycode[name]
            if with_checkdigit:
                code = calc_checkdigit(code)
        except KeyError:
            code = None
        return code

    @name2citycode.register(list)
    def _name2citycode_list(self,
            name_list: List,
            with_checkdigit=False
        ) -> List:
        """ Convert list of cityName to cityCode """
        code = [self.name2citycode(x, with_checkdigit) for x in name_list]
        return code

    @name2citycode.register(pd.Series)
    def _name2citycode_series(self,
            name_series: pd.Series,
            with_checkdigit=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to cityCode """
        try:
            code = name_series.map(self.__name2citycode, with_checkdigit)
            if with_checkdigit:
                code = calc_checkdigit(code)
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def name2prefcode(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2prefcode.register(str)
    def name2prefcode_str(self, name: str) -> Optional[int]:
        """ Convert CityName to Prefecture Code"""
        code = self.__name2citycode[name]
        if code:
            prefcode = int(str(code)[:2])
        else:
            prefcode = None
        return prefcode

    @name2prefcode.register(list)
    def _name2prefcode_list(self,
            name_list: List,
        ) -> List:
        """ Convert list of cityName to Prefecture Code """
        code = [self.name2prefcode(x) for x in name_list]
        return code

    @name2prefcode.register(pd.Series)
    def _name2prefcode_series(self,
            name_series: pd.Series,
        ) -> pd.Series:
        """ Convert pandas series of cityName to Prefecture Code """
        try:
            code = name_series.map(self.__name2citycode)
            code = code.map(lambda x: int(str(x)[:2]) if x else x)
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def name2prefecture(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2prefecture.register(str)
    def name2prefecture_str(self, name: str) -> Optional[int]:
        """ Convert CityName to Prefecture Name"""
        code = self.name2prefcode(name)
        name = self.code2name(code)
        return name

    @name2prefecture.register(list)
    def name2prefecture_str(self, name_list: list) -> Optional[int]:
        """ Convert list of CityName to Prefecture Name"""
        code = self.name2prefcode(name_list)
        name = list(map(self.code2name, code))
        return name

    @singledispatchmethod
    def citycode2name(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @citycode2name.register(int)
    def _citycode2name_int(self, code: int) -> Optional[str]:
        """ Convert cityCode to cityName """
        if len(str(code)) == 6:
            code = validate_checkdigit(code)
        try:
            name = self.__citycode2name[code]
        except KeyError:
            name = None
        return name

    @citycode2name.register(str)
    def _citycode2name_int(self, code: str) -> Optional[str]:
        """ Convert cityCode to cityName """
        if len(code) == 6:
            code = validate_checkdigit(int(code), 5)
        else:
            code = int(code)
        try:
            name = self.__citycode2name[code]
        except:
            name = None
        return name

    @citycode2name.register(list)
    def _citycode2name_list(self, code_list: List) -> List:
        """ Convert list of cityCode to CityName """
        name = [self.citycode2name(x) for x in code_list]
        return name

    @citycode2name.register(pd.Series)
    def _citycode2name_series(self, code_series: pd.Series) -> pd.Series:
        """ Convert pandas series of cityCode to cityName """
        try:
            code_series.astype(int)
            name = code_series.map(self.__citycode2name)
        except:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def validate_city(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @validate_city.register(str)
    def _validate_city_str(self, name: str) -> Optional[str]:
        """ validate_city a cityName """
        try:
            v = name in self.__name2citycode.keys()
        except:
            v = False
        return v

    @validate_city.register(list)
    def _validate_city_list(self, name_list: List) -> List:
        """ validate_city list of cityName """
        try:
            v = [ self.validate_city(x) for x in name_list]
        except:
            v = [False]
        return v

    @validate_city.register(pd.Series)
    def _validate_city_series(self, name_series: pd.Series) -> pd.Series:
        """ validate_city pandas series of cityName """
        try:
            v = [ self.validate_city(x) for x in np.asarray(name_series)]
            print(v)
        except KeyError:
            v = [False]
        return pd.Series(v)

jp_cities = JpCityCode()
