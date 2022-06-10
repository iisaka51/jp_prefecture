import numpy as np
import pandas as pd
from typing import List, Optional, Any
from pathlib import Path
from .singledispatchmethod import singledispatchmethod
from .immutable_dict import ImmutableDict
from .checkdigit import calc_checkdigit, validate_checkdigit

class JpCityCode(object):
    def __init__(self):
        # Cities Code: JIS X 0402

        self.cities = pd.read_csv(Path(__file__).parent / 'data/cities.csv',
                                  index_col = 0)

        self.__code2name = ImmutableDict({
            code: name
            for name, code in zip(self.cities.cityName,
                                  self.cities.cityCode)
        })

        self.__name2code = ImmutableDict({
            **{name: code
               for name, code in zip(self.cities.cityName,
                                     self.cities.cityCode)},
        })

    @singledispatchmethod
    def name2code(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2code.register(str)
    def _name2code_str(self,
            name: str,
            with_checkdigit=False
        ) -> Optional[int]:
        """ Convert cityName to cityCode """
        try:
            code = self.__name2code[name]
            if with_checkdigit:
                code = calc_checkdigit(code)
        except KeyError:
            code = None
        return code

    @name2code.register(list)
    def _name2code_list(self,
            name_list: List,
            with_checkdigit=False
        ) -> List:
        """ Convert list of cityName to cityCode """
        code = [self.name2code(x, with_checkdigit) for x in name_list]
        return code

    @name2code.register(pd.Series)
    def _name2code_series(self,
            name_series: pd.Series,
            with_checkdigit=False
        ) -> pd.Series:
        """ Convert pandas series of cityName to cityCode """
        try:
            code = name_series.map(self.__name2code, with_checkdigit)
            if with_checkdigit:
                code = calc_checkdigit(code)
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def code2name(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @code2name.register(int)
    def _code2name_int(self, code: int) -> Optional[str]:
        """ Convert cityCode to cityName """
        if len(str(code)) == 6:
            code = validate_checkdigit(code)
        try:
            name = self.__code2name[code]
        except KeyError:
            name = None
        return name

    @code2name.register(str)
    def _code2name_int(self, code: str) -> Optional[str]:
        """ Convert cityCode to cityName """
        if len(code) == 6:
            code = validate_checkdigit(int(code), 5)
        else:
            code = int(code)
        try:
            name = self.__code2name[code]
        except:
            name = None
        return name

    @code2name.register(list)
    def _code2name_list(self, code_list: List) -> List:
        """ Convert list of cityCode to CityName """
        name = [self.code2name(x) for x in code_list]
        return name

    @code2name.register(pd.Series)
    def _code2name_series(self, code_series: pd.Series) -> pd.Series:
        """ Convert pandas series of cityCode to cityName """
        try:
            code_series.astype(int)
            name = code_series.map(self.__code2name)
        except:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def validator(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @validator.register(str)
    def _validator_str(self, name: str) -> Optional[str]:
        """ Validator a cityName """
        try:
            v = name in self.__name2code.keys()
        except:
            v = False
        return v

    @validator.register(list)
    def _validator_list(self, name_list: List) -> List:
        """ Validator list of cityName """
        try:
            v = [ self.validator(x) for x in name_list]
        except:
            v = [False]
        return v

    @validator.register(pd.Series)
    def _validator_series(self, name_series: pd.Series) -> pd.Series:
        """ Validator pandas series of cityName """
        try:
            v = [ self.validator(x) for x in np.asarray(name_series)]
            print(v)
        except KeyError:
            v = [False]
        return pd.Series(v)

jp_cities = JpCityCode()
