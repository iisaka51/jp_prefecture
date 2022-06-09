import numpy as np
import pandas as pd
from typing import List, Optional, Any
from .singledispatchmethod import singledispatchmethod
from .immutable_dict import ImmutableDict

class JpPrefecture(object):
    def __init__(self):
        self.__prefecture_names = {
            "北海道" : 'Hokkaido',
            "青森県" : 'Aomori',
            "岩手県" : 'Iwate',
            "宮城県" : 'Miyagi',
            "秋田県" : 'Akita',
            "山形県" : 'Yamagata',
            "福島県" : 'Fukushima',
            "茨城県" : 'Ibaraki',
            "栃木県" : 'Tochigi',
            "群馬県" : 'Gunma',
            "埼玉県" : 'Saitama',
            "千葉県" : 'Chiba',
            "東京都" : 'Tokyo',
            "神奈川県" : 'Kanagawa',
            "新潟県" : 'Niigata',
            "富山県" : 'Toyama',
            "石川県" : 'Ishikawa',
            "福井県" : 'Fukui',
            "山梨県" : 'Yamanashi',
            "長野県" : 'Nagano',
            "岐阜県" : 'Gifu',
            "静岡県" : 'Shizuoka',
            "愛知県" : 'Aichi',
            "三重県" : 'Mie',
            "滋賀県" : 'Shiga',
            "京都府" : 'Kyoto',
            "大阪府" : 'Osaka',
            "兵庫県" : 'Hyogo',
            "奈良県" : 'Nara',
            "和歌山県" : 'Wakayama',
            "鳥取県" : 'Tottori',
            "島根県" : 'Shimane',
            "岡山県" : 'Okayama',
            "広島県" : 'Hiroshima',
            "山口県" : 'Yamaguchi',
            "徳島県" : 'Tokushima',
            "香川県" : 'Kagawa',
            "愛媛県" : 'Ehime',
            "高知県" : 'Kochi',
            "福岡県" : 'Fukuoka',
            "佐賀県" : 'Saga',
            "長崎県" : 'Nagasaki',
            "熊本県" : 'Kumamoto',
            "大分県" : 'Oita',
            "宮崎県" : 'Miyazaki',
            "鹿児島県" : 'Kagoshima',
            "沖縄県" : 'Okinawa',
        }

        # Index is code (JIS X 0401-1973)
        self.prefectures = pd.DataFrame(
            dict(
                name = [p for p in self.__prefecture_names.keys()],
                short_name = [p[:-1] for p in self.__prefecture_names.keys()],
                alphabet_name = [p for p in self.__prefecture_names.values()],
            ),
            index = pd.Index(range(1, 1 + len(self.__prefecture_names)),
                             name="code"),
        )

        self.__code2name = ImmutableDict({
            code: name
            for name, code in zip(self.prefectures.name,
                                  self.prefectures.index)
        })

        self.__code2alphabet = ImmutableDict({
            code: alphabet
            for alphabet, code in zip(self.prefectures.alphabet_name,
                                  self.prefectures.index)
        })

        self.__name2code = ImmutableDict({
            **{name: code
               for name, code in zip(self.prefectures.name,
                                     self.prefectures.index)},
            **{name: code
               for name, code in zip(self.prefectures.short_name,
                                     self.prefectures.index)},
            **{name: code
               for name, code in zip(self.prefectures.alphabet_name,
                                     self.prefectures.index)},
            **{name.lower(): code
               for name, code in zip(self.prefectures.alphabet_name,
                                     self.prefectures.index)},
            **{name.upper(): code
               for name, code in zip(self.prefectures.alphabet_name,
                                     self.prefectures.index)},
        })

        self.__alphabet2name = ImmutableDict({
            **{alphabet: name
            for alphabet, name in zip(self.prefectures.alphabet_name,
                                      self.prefectures.name)},
            **{alphabet.lower(): name
            for alphabet, name in zip(self.prefectures.alphabet_name,
                                              self.prefectures.name)},
            **{alphabet.upper(): name
            for alphabet, name in zip(self.prefectures.alphabet_name,
                                              self.prefectures.name)},
            **{alphabet: name
            for alphabet, name in zip(self.prefectures.name,
                                      self.prefectures.name)},
            **{alphabet: name
            for alphabet, name in zip(self.prefectures.short_name,
                                      self.prefectures.name)},
        })

        self.__name2alphabet = ImmutableDict({
            **{name: alphabet
              for name, alphabet in zip(self.prefectures.name,
                                        self.prefectures.alphabet_name)},
            **{name: alphabet
              for name, alphabet in zip(self.prefectures.short_name,
                                        self.prefectures.alphabet_name)},
            **{name: alphabet
              for name, alphabet in zip(self.prefectures.alphabet_name,
                                        self.prefectures.alphabet_name)},
            **{name.lower(): alphabet
              for name, alphabet in zip(self.prefectures.alphabet_name,
                                        self.prefectures.alphabet_name)},
            **{name.upper(): alphabet
              for name, alphabet in zip(self.prefectures.alphabet_name,
                                        self.prefectures.alphabet_name)},
    })

    @singledispatchmethod
    def name2code(self, arg: Any) -> Optional[int]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2code.register(str)
    def _name2code_str(self, name: str) -> Optional[int]:
        """ Convert prefecture name to code """
        try:
            code = self.__name2code[name]
        except KeyError:
            code = None
        return code

    @name2code.register(list)
    def _name2code_list(self, name_list: List) -> List:
        """ Convert list of prefecture name to code """
        code = [self.name2code(x) for x in name_list]
        return code

    @name2code.register(pd.Series)
    def _name2code_series(self, name_series: pd.Series) -> pd.Series:
        """ Convert pandas series of prefecture name to code """
        try:
            code = name_series.map(self.__name2code)
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def code2name(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @code2name.register(int)
    def _code2name_int(self, code: int) -> Optional[str]:
        """ Convert prefecture code to name """
        try:
            name = self.__code2name[code]
        except KeyError:
            name = None
        return name

    @code2name.register(list)
    def _code2name_list(self, code_list: List) -> List:
        """ Convert list of prefecture code to name """
        name = [self.code2name(x) for x in code_list]
        return name

    @code2name.register(pd.Series)
    def _code2name_series(self, code_series: pd.Series) -> pd.Series:
        """ Convert pandas series of prefecture code to alphabet_name """
        try:
            name = code_series.map(self.__code2name)
        except KeyError:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def code2alphabet(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @code2alphabet.register(int)
    def _code2alphabet_int(self, code: int) -> Optional[str]:
        """ Convert prefecture code to name """
        try:
            alphabet = self.__code2alphabet[code]
        except KeyError:
            alphabet = None
        return alphabet

    @code2alphabet.register(list)
    def _code2alphabet_list(self, code_list: List) -> List:
        """ Convert list of prefecture code to name """
        alphabet = [self.code2alphabet(x) for x in code_list]
        return alphabet

    @code2alphabet.register(pd.Series)
    def _code2alphabet_series(self, code_series: pd.Series) -> pd.Series:
        """ Convert pandas series of prefecture code to alphabet_name """
        try:
            alphabet = code_series.map(self.__code2alphabet)
        except KeyError:
            alphabet = pd.Series([])
        return alphabet

    @singledispatchmethod
    def alphabet2code(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @alphabet2code.register(str)
    def _alphabet2code_str(self, alphabet_name: str) -> Optional[str]:
        """ Convert a prefecture alphabet_name to code """
        try:
            code = self.__alphabet2code[alphabet_name]
        except KeyError:
            code = None
        return code

    @alphabet2code.register(list)
    def _alphabet2code_list(self, alphabet_name_list: List) -> List:
        """ Convert list of prefecture alphabet_name to code """
        code = [self.alphabet2code(x) for x in alphabet_name_list]
        return name

    @alphabet2code.register(pd.Series)
    def _alphabet2code_series(self, alphabet_name_series: pd.Series) ->pd.Series:
        """ Convert pandas series of prefecture alphabet_name to code """
        try:
            code = alphabet_name_series.map(self.__alphabet2code)
        except KeyError:
            code = pd.Series([])
        return name

    @singledispatchmethod
    def name2alphabet(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2alphabet.register(str)
    def _name2alphabet_str(self, name: str) -> Optional[str]:
        """ Convert a prefecture name to alphabet_name """
        try:
            alphabet = self.__name2alphabet[name]
        except KeyError:
            alphabet = None
        return alphabet

    @name2alphabet.register(list)
    def _name2alphabet_list(self, name_list: List) -> List:
        """ Convert list of prefecture name to alphabet_name """
        alphabet = [self.name2alphabet(x) for x in name_list]
        return alphabet

    @name2alphabet.register(pd.Series)
    def _name2alphabet_series(self, name_series: pd.Series) ->pd.Series:
        """ Convert pandas series of prefecture name to alphabet_name """
        try:
            alphabet = name_series.map(self.__name2alphabet)
        except KeyError:
            alphabet = pd.Series([])
        return alphabet

    @singledispatchmethod
    def alphabet2name(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @alphabet2name.register(str)
    def _alphabet2name_str(self, alphabet_name: str) -> Optional[str]:
        """ Convert a prefecture alphabet_name to name """
        try:
            name = self.__alphabet2name[alphabet_name]
        except KeyError:
            name = None
        return name

    @alphabet2name.register(list)
    def _alphabet2name_list(self, alphabet_name_list: List) -> List:
        """ Convert list prefecture alphabet_name to name """
        name = [self.alphabet2name(x) for x in alphabet_name_list]
        return name

    @alphabet2name.register(pd.Series)
    def _alphabet2name_series(self, alphabet_name_series: pd.Series) -> pd.Series:
        """ Convert list prefecture alphabet_name to name """
        try:
            name = alphabet_name_series.map(self.__alphabet2name)
        except KeyError:
            name = pd.Series([])
        return name

    @singledispatchmethod
    def validator(self, arg: Any) -> Optional[str]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @validator.register(str)
    def _validator_str(self, name: str) -> Optional[str]:
        """ Validator a prefecture name """
        try:
            v = name in self.__name2code.keys()
        except:
            v = False
        return v

    @validator.register(list)
    def _validator_list(self, name_list: List) -> List:
        """ Validator list of prefecture name """
        try:
            v = [ self.validator(x) for x in name_list]
        except:
            v = [False]
        return v

    @validator.register(pd.Series)
    def _validator_series(self, name_series: pd.Series) -> pd.Series:
        """ Validator pandas series of prefecture name """
        try:
            v = [ self.validator(x) for x in np.asarray(name_series)]
            print(v)
        except KeyError:
            v = [False]
        return pd.Series(v)

jp_prefectures = JpPrefecture()
