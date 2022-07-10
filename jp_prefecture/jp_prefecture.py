import numpy as np
import pandas as pd
from typing import List, Optional, Union, Any
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
        del self.__prefecture_names

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
        })

        self.__alphabet2name = ImmutableDict({
            **{alphabet: name
            for alphabet, name in zip(self.prefectures.alphabet_name,
                                      self.prefectures.name)},
            **{name: code
               for name, code in zip(self.prefectures.short_name,
                                     self.prefectures.name)},
            **{alphabet: name
            for alphabet, name in zip(self.prefectures.name,
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
    })

    @singledispatchmethod
    def name2code(self, arg: Any) -> Union[list,Optional[int],pd.Series]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2code.register(type(None))
    def _name2code_none(self,
            name: None,
            ignore_case: bool=False,
        ):
        """ Catch None and return None """
        return None

    @name2code.register(str)
    def _name2code_str(self,
            name: str,
            ignore_case: bool=False,
        ) -> Optional[int]:
        """ Convert prefecture name to code """
        try:
            name = name.capitalize() if ignore_case else name
            code = self.__name2code[name]
        except KeyError:
            code = None
        return code

    @name2code.register(list)
    def _name2code_list(self,
            name_list: List[str],
            ignore_case: bool=False,
        ) -> list:
        """ Convert list of prefecture name to code """
        code = [self.name2code(x, ignore_case) for x in name_list]
        return code

    @name2code.register(pd.Series)
    def _name2code_series(self,
            name_series: pd.Series,
            ignore_case: bool=False,
        ) -> pd.Series:
        """ Convert pandas series of prefecture name to code """
        try:
            name_series = ( name_series.str.capitalize()
                            if ignore_case else name_series )
            code = name_series.map(self.__name2code)
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def code2name(self, arg: Any) -> Union[Optional[str],list,pd.Series]:
        """ Convert prefecture code to name """
        raise TypeError('Unsupport Type')

    @code2name.register(type(None))
    def _code2name_none(self,
            codeL: None,
            ascii: bool=False,
        ):
        """ Catch None and return None """
        return None

    @code2name.register(int)
    def _code2name_int(self,
            code: int,
            ascii: bool=False,
        ) -> Optional[str]:
        """ Convert prefecture code to name """
        try:
            name = ( self.__code2alphabet[code]
                     if ascii else self.__code2name[code] )
        except KeyError:
            name = None
        return name

    @code2name.register(str)
    def _code2name_str(self,
            code: str,
            ascii: bool=False,
        ) -> Optional[str]:
        """ Convert prefecture code to name """
        try:
            name = ( self.__code2alphabet[int(code)]
                     if ascii else self.__code2name[int(code)] )
        except KeyError:
            name = None
        return name

    @code2name.register(list)
    def _code2name_list(self,
            code_list: list,
            ascii: bool=False,
        ) -> list:
        """ Convert list of prefecture code to name """
        name = [self.code2name(x, ascii) for x in code_list]
        return name

    @code2name.register(pd.Series)
    def _code2name_series(self,
            code_series: pd.Series,
            ascii: bool=False,
        ) -> pd.Series:
        """ Convert pandas series of prefecture code to alphabet_name """
        try:
            code_series = code_series.astype(int)
            name = ( code_series.map(self.__code2alphabet)
                     if ascii else code_series.map(self.__code2name) )
        except KeyError:
            name = pd.Series([])
        return name


    @singledispatchmethod
    def name2normalize(self, arg: Any) -> Union[Optional[str],list,pd.Series]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @name2normalize.register(type(None))
    def _name2normalize_none(self,
            name: None,
            ascii: bool=False,
            ignore_case: bool=False
        ):
        """ Catch None and return None """
        return None

    @name2normalize.register(str)
    def _name2normalize_str(self,
            name: str,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> Optional[str]:
        """ Convert prefecture name to name or alphabet_name """
        try:
            name = name.capitalize() if ignore_case else name
            normalize = ( self.__name2alphabet[name]
                          if ascii else self.__alphabet2name[name] )
        except KeyError:
            normalize = None
        return normalize

    @name2normalize.register(list)
    def _name2normalize_list(self,
            name_list: list,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> list:
        """ Convert list of prefecture name to alphabet_name """
        code = [self.name2normalize(x, ascii, ignore_case) for x in name_list]
        return code

    @name2normalize.register(pd.Series)
    def _name2normalize_series(self,
            name_series: pd.Series,
            ascii: bool=False,
            ignore_case: bool=False
        ) -> pd.Series:
        """ Convert pandas series of prefecture name to alphabet_name """
        try:
            name_series = ( name_series.str.capitalize()
                            if ignore_case else name_series )
            code = ( name_series.map(self.__name2alphabet)
                     if ascii else name_series.map(self.__alphabet2name) )
        except KeyError:
            code = pd.Series([])
        return code

    @singledispatchmethod
    def validate(self, arg: Any) -> Optional[Union[bool,List[bool],pd.Series]]:
        """ dispatch function """
        raise TypeError('Unsupport Type')

    @validate.register(type(None))
    def _validate_none(self,
            name: None,
            ignore_case: bool=False
        ) -> Union[bool,List[bool],pd.Series]:
        """ Catch None and return None """
        return None

    @validate.register(str)
    def _validate_str(self,
            name: str,
            ignore_case: bool=False
        ) -> bool:
        """ validate a prefecture name """
        try:
            name = name.capitalize() if ignore_case else name
            v = name in self.__name2code.keys()
        except:
            v = False
        return v

    @validate.register(list)
    def _validate_list(self,
            name_list: List[str],
            ignore_case: bool=False
        ) -> list:
        """ validate list of prefecture name """
        try:
            v = [ self.validate(x, ignore_case) for x in name_list]
        except:
            v = [False]
        return v

    @validate.register(pd.Series)
    def _validate_series(self,
            name_series: pd.Series,
            ignore_case: bool=False
        ) -> pd.Series:
        """ validate pandas series of prefecture name """
        try:
            v = [ self.validate(x, ignore_case) for x in np.asarray(name_series)]
        except KeyError:
            v = [False]
        return pd.Series(v)

jp_prefectures = JpPrefecture()
