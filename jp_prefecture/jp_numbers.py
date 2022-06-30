from typing import Union, Optional, Any, NamedTuple, Literal
import math
import re

Style = Literal['kanji', 'arabic', 'mix', 'finance', 'daiji']

# Grok for Japanese Number
NUMBERS = (
    r'('
      r'[01-9]+'
    r')'
)

NOT_NUMBERS = (
    r'([^01-9]+)?'
)

KANJI_DIGITS = (
    r'〇一二三四五六七八九'
    r'０１２３４５６７８９'
)
KANJI_ARABIC_DIGITS = (
    r'０１２３４５６７８９'
)

KANJI_UNITS = (
    r'十百千万億兆京垓𥝱'
)

# Old style numbers.
DAIJI_DIGITS = (
    r'零壱弐参肆伍陸漆捌玖'
    r'拾佰仟萬'
)

YEN_SYMBOL = (
    r'[円圓]'
)

NOT_KANJI_NUMBERS = (
    r'([^'
       f'{KANJI_DIGITS}十'
    r']*)?'
)

KANJI_NUMBERS = (
    r'(['
      f'{KANJI_DIGITS}十'
    r']+)'
)

KANJI_ARABIC_NUMBERS = (
    r'(['
      f'{KANJI_ARABIC_DIGITS}'
    r']*)'
)

NOT_KANJI_ARABIC_NUMBERS = (
    r'([^'
      f'{KANJI_ARABIC_DIGITS}'
    r']*)'
)

class JpNumber(NamedTuple):
    as_int: Optional[int]=None
    as_str: Optional[str]=None
    as_kanji: Optional[str]=None

class ParseNumber(NamedTuple):
    prefix: str
    number: JpNumber
    suffix: str

class Token(NamedTuple):
    as_int: int
    as_str: str
    unit: int

class JpNumberParser(object):

    __KANJI_DIGITS=(
        '〇', '一', '二', '三', '四', '五', '六', '七', '八', '九')
    __MULTIBYTE_DIGITS=(
        '０', '１', '２', '３', '４', '５', '６', '７', '８', '９')
    __DAIJI_DIGITS=(
        '零', '壱', '弐', '参', '肆', '伍', '陸', '漆', '捌', '玖')

    __KANJI_MINOR_UNITS = {
        '千': 1000,
        '百': 100,
        '十': 10,
    }
    __KANJI_MAJOR_UNITS = ( '𥝱', '垓', '兆', '京', '億', '万' )

    __KANJI_UNIT_MAPPER = {
        '万':   pow(10, 4),
        '十万': pow(10, 5),
        '百万': pow(10, 6),
        '千万': pow(10, 7),
        '億':   pow(10, 8),
        '十億': pow(10, 9),
        '百億': pow(10, 10),
        '千億': pow(10, 11),
        '兆':   pow(10, 12),
        '十兆': pow(10, 13),
        '百兆': pow(10, 14),
        '千兆': pow(10, 15),
        '京':   pow(10, 16),
        '十京': pow(10, 17),
        '百京': pow(10, 18),
        '千京': pow(10, 19),
        '垓':   pow(10, 20),
        '十垓': pow(10, 21),
        '百垓': pow(10, 22),
        '千垓': pow(10, 23),
        '𥝱':   pow(10, 24),
        '十𥝱': pow(10, 25),
        '百𥝱': pow(10, 26),
        '千𥝱': pow(10, 27),
    }

    def __init__(self):
        self.__NUMERICS = list(map(str, range(0, 10)))
        self.__Number2KanjiNumber = {
            **{ num: kanji
                for num, kanji in enumerate(self.__KANJI_DIGITS)},
            **{ str(num): kanji
                for num, kanji in enumerate(self.__KANJI_DIGITS)}
            }
        self.__Number2ArabicNumber = {
            **{ num: kanji
                for num, kanji in enumerate(self.__MULTIBYTE_DIGITS)},
            **{ str(num): kanji
                for num, kanji in enumerate(self.__MULTIBYTE_DIGITS)}
            }
        self.__KanjiNumber2Number = {
            **{ kanji: num
                for num, kanji in enumerate(self.__KANJI_DIGITS)},
            **{ kanji: num
                 for num, kanji in enumerate(self.__MULTIBYTE_DIGITS)}
            }
        self.__unit_mapper = {
            **{ unit: kanji_unit
                for kanji_unit, unit in self.__KANJI_MINOR_UNITS.items()},
            **{ unit: kanji_unit
                for kanji_unit, unit in self.__KANJI_UNIT_MAPPER.items()},
            **{ kanji_unit: unit
                for kanji_unit, unit in self.__KANJI_MINOR_UNITS.items()},
            **{ kanji_unit: unit
                for kanji_unit, unit in self.__KANJI_UNIT_MAPPER.items()},
            }

    def _number_tokenizer(self,
            as_str
        )->list:
        size = len(as_str)
        token_list = list()
        if size == 1:
              if as_str[0] in self.__Number2KanjiNumber:
                  c = self.__Number2KanjiNumber[as_str[0]]
              token_list.append(Token(int(as_str[0]), as_str[0], -1))
              return token_list

        unit = pow(10, size)
        for c in as_str:
            if c in self.__Number2KanjiNumber:
                unit = int(unit / 10)
                if unit not in self.__unit_mapper:
                    unit = 1
                token_list.append(Token(int(c), c, unit))
        return token_list

    def _number2kanji_parser(self,
            token_list: list,
            style: Style
        )->list:
        stack = list()         # type: ignore
        if style not in ['kanji', 'daiji']:
            return stack

        base_unit = 1
        for token in token_list:
            as_int = token.as_int
            unit = token.unit
            if as_int != 0:
                stack.append(self.__Number2KanjiNumber[as_int])
            base_unit *= 10
            if unit in self.__unit_mapper:
                kanji_unit = self.__unit_mapper[unit]
            elif unit < 0:
                if as_int == 0:
                    stack.append(self.__Number2KanjiNumber[as_int])
                break
            else:
                kanji_unit = ""
            if len(kanji_unit) >= 1:
                kanji_unit = kanji_unit[0]
            if as_int != 0:
                if kanji_unit in self.__KANJI_MINOR_UNITS:
                    stack.append( kanji_unit )
                count = 0
            else:
                count += 1
            if ( count <4 and kanji_unit in self.__KANJI_UNIT_MAPPER):
                    stack.append( kanji_unit )
        return stack

    def _number2mix_parser(self,
            token_list: list,
            style: Style
        )->list:

        count = 0
        stack = list()     # type: ignore
        if style not in ['mix']:
            return stack

        for token in reversed(token_list):
            as_int = token.as_int
            unit = token.unit
            v = self.__Number2ArabicNumber[as_int]

            if unit in self.__unit_mapper:
                kanji_unit = self.__unit_mapper[unit]
            else:
                kanji_unit = '一'

            if len(kanji_unit) != 1:
                kanji_unit = kanji_unit[0]

            if kanji_unit in self.__KANJI_MAJOR_UNITS:
                if count < 4:
                    for _ in range(count):
                        stack.pop(-1)
                    stack.append(kanji_unit)
                else:
                    stack.append(kanji_unit)
                count = 0

            stack.append(v)
            if as_int != 0:
                count = 0
            else:
                count += 1
            if count >= 4:
                del(stack[-5:])

        return reversed(stack)    # type: ignore

    def _number2arabic_parser(self,
            token_list: list,
            style: Style
        )->list:

        stack = list()            # type: ignore
        if style not in ['arabic', 'finance']:
            return stack

        for token in token_list:
            c = token.as_int
            v = self.__Number2ArabicNumber[c]
            stack.append(v)

        if style == 'finance':
            new_stack=list()
            sub_unit = 1
            for c in reversed(stack):
                new_stack.append(c)
                sub_unit *= 10
                if sub_unit % 1000 == 0:
                    new_stack.append('，')
                    sub_unit = 1
            if new_stack[-1] == '，':
                new_stack.pop(-1)
            stack = reversed(new_stack)   # type: ignore
        return stack

    def number2kanji(self,
            val: Union[int, str],
            style: Style='kanji',
            trim: bool=True,
        )-> JpNumber:
        """ Conver Number to Kanji Number
        Parameters
        ----------
        val: Union[str, int]
            any positive number
        syle: Style
             output style.  default is ``kanji``
               'kanji': '一万二千三百'
              'arabic': '１２３００'
                 'mix': '１万２３００'
             'finance': '１２，３００'

        trim: bool
            if set ``True``, drop '一' from '一百' or '一千'.
            default is ``True``

        Returns:
           converted number: JpNumber
        """

        replace_chars = {
            '^一千': '千',
            '^一百': '百',
            '^一十': '十',
            '^１千': '千',
            '^１百': '百',
            '^１十': '十',
        }

        replace_daiji = {
            '〇': '零',
            '一': '壱',
            '二': '弐',
            '三': '参',
            '四': '肆',
            '五': '伍',
            '六': '陸',
            '七': '漆',
            '八': '捌',
            '九': '玖',
            '十': '拾',
            '百': '佰',
            '千': '仟',
            '万': '萬',
        }

        action = {
            'arabic': self._number2arabic_parser,
            'finance': self._number2arabic_parser,
            'kanji': self._number2kanji_parser,
            'daiji': self._number2kanji_parser,
            'mix': self._number2mix_parser,
        }

        if isinstance(val, int):
            number = val
            as_str = str(val)
        else:
            number = int(val)
            as_str = val

        if number <0:
            return JpNumber( number, as_str, '')

        token_list = self._number_tokenizer(as_str)
        stack = action[style](token_list, style)
        as_kanji = str().join(stack)

        if style == 'daiji':
            for src, dst in replace_daiji.items():
                as_kanji = re.sub(src, dst, as_kanji)
        elif trim:
            for src, dst in replace_chars.items():
                as_kanji = re.sub(src, dst, as_kanji)
        return JpNumber( number, as_str, as_kanji)

    def kanji2arabic_parser(self,
           val : str,
        )-> int:
        # １２３０００００
        unit = 1
        number = 0
        for c in reversed(val):
            if c in self.__KanjiNumber2Number:
                number += self.__KanjiNumber2Number[c] * unit
                unit *= 10
        return number

    def kanji2mix_parser(self,
           val : str,
        )-> int:

        # val １億２千２３０万
        #  conver strings from kanji arabic char to numeric digits.
        #  stack [1, 100000000, 2, 1000, 230, 10000]
        # calc
        #  stack[1 x 100000000, (2 x 1000 + 230) x 10000]
        # sum(stack)

        stack = list()      # type: ignore
        as_str = ''
        for c in val:
            if c in self.__KanjiNumber2Number:
                as_str += str(self.__KanjiNumber2Number[c])
                continue
            elif c in self.__KANJI_MAJOR_UNITS:
                stack.append(int(as_str))
                stack.append(self.__unit_mapper[c])
                as_str=''
            elif c in self.__KANJI_MINOR_UNITS.keys():
                stack.append(int(as_str))
                stack.append(self.__KANJI_MINOR_UNITS[c])
                as_str=''

        number = 0
        base_unit = unit = 1
        for elm in reversed(stack):
            if elm in self.__KANJI_UNIT_MAPPER.values():
                base_unit = elm
                unit = 1
                continue
            elif elm in self.__KANJI_MINOR_UNITS.values():
                unit = elm
                continue
            else:
                number += elm * unit * base_unit
                unit = 1
        return number

    def kanji2number_parser(self,
           val : str,
        )-> int:
        """
        Parameters
        ----------
        val: str
             any positive integer as string

        Logic
        -----
            val: 一億二百三十万
            Step1:  Split Major Unit
                 stack[一, 100000000, 二百三十, 10000]
            Step2:  Split Minor Unit
                 stack[一, 100000000, 二, 100, 三十, 10000]
                 stack[一, 100000000, 二, 100, 三, 10, 10000]
            Step3:   convert kanji digits to interger
                 stack[1 , 10000000, 2, 100, 3, 10, 10000]
            Step4:  calculartion
                 1 x 100000000 + (2 x100 + 3 x 30) x 10000
        """
        as_str = val
        number = 0
        stack = list()      # type: ignore
        for sp in self.__KANJI_MAJOR_UNITS:
            r = as_str.split(sp)
            if len(r) != 1:
                if r[0] == '':
                    stack.append('一')
                else:
                    stack.append(r[0])
                if r[1] == '':
                    stack.append(self.__unit_mapper[sp])
                    break
                else:
                    as_str = r[1]
                    stack.append(self.__unit_mapper[sp])
            elif r[0] != '':
                as_str = r[0]
        else:
           stack.append(as_str)

        stack2 = list()
        for word in reversed(stack):
            if isinstance(word, int):
                 stack2.append(word)
                 continue

            if word in self.__KanjiNumber2Number:
                stack2.append(word)
                continue

            as_str = word
            for sp in self.__KANJI_MINOR_UNITS.keys():
                r = as_str.split(sp)
                if len(r) != 1:
                    stack2.append(self.__KANJI_MINOR_UNITS[sp]) # type: ignore
                    if r[0] == '':
                        stack2.append('一')
                    else:
                        if r[0] in self.__KanjiNumber2Number:
                            stack2.append(r[0])
                    if r[1] == '':
                        stack2.append(self.__unit_mapper[sp])
                        break
                    else:
                        as_str = r[1]
                else:
                    as_str = r[0]
            else:
                if as_str in self.__KanjiNumber2Number:
                    stack2.append(as_str)

        number = 0
        base_unit = unit = 1
        for word in stack2:
            if word in self.__KANJI_UNIT_MAPPER.values():
                base_unit = word          # type: ignore
                unit = 1
                continue
            elif word in self.__KANJI_MINOR_UNITS.values():
                unit = word               # type: ignore
                continue
            else:
                number += self.__KanjiNumber2Number[word] * unit * base_unit
                unit = 1
        return number

    def kanji2number(self,
           val : str,
        )-> JpNumber:
        """ Conver Number to Kanji Number
        Parameters
        ----------
        val: str
            any number as string
        Returns:
           converted number: JpNumber
        """
        replace_comma = {
            '，': '',
            ',': '',
        }

        as_kanji = val

        replace_daiji = {
            '零': '〇',
            '壱': '一',
            '弐': '二',
            '参': '三',
            '肆': '四',
            '伍': '五',
            '陸': '六',
            '漆': '七',
            '捌': '八',
            '玖': '九',
            '拾': '十',
            '佰': '百',
            '仟': '千',
            '萬': '万',
        }
        daiji_contain = any( x in val for x in replace_daiji.keys() )
        if daiji_contain:
            for src, dst in replace_daiji.items():
                val = re.sub( src, dst, val)

        for src, dst in replace_comma.items() :
                val = re.sub(src, dst, val)

        stack = list()      # type: ignore
        for c in val:
            if ( c in self.__unit_mapper
                 or c in self.__KanjiNumber2Number):
                 stack.append(c)

        as_str = str().join(stack)
        if as_str == '':
            return JpNumber( -1, '', as_kanji)

        number = 0

        all_unit = ( list(self.__KANJI_MINOR_UNITS.keys())
                     + list(self.__KANJI_UNIT_MAPPER.keys()) )
        unit_contain = any(x in val for x in all_unit)
        arabic_contain = any( x in val for x in self.__MULTIBYTE_DIGITS )

        if not unit_contain:
            number = self.kanji2arabic_parser(as_str)
        elif  arabic_contain :
            number = self.kanji2mix_parser(as_str)
        else:
            number = self.kanji2number_parser(as_str)

        as_str = str(number)
        return JpNumber( number, as_str, as_kanji)

    def parse_kanjinumber(self,
            text: str,
            startwith: Optional[re.Pattern]=None,
            endwith: Optional[re.Pattern]=None,
        ) -> Optional[ParseNumber]:

        if not startwith:
            startwith = f'{NOT_KANJI_ARABIC_NUMBERS}'          # type: ignore

        if not endwith:
            endwith = f'{NOT_KANJI_ARABIC_NUMBERS}' + r'(.*)?' # type: ignore

        kanji_number = re.compile(
             startwith + f'{KANJI_ARABIC_NUMBERS}' + endwith,  # type: ignore
             re.UNICODE
        )

        match =  kanji_number.search(text)

        if match:
            if len(match.groups()) == 1 :
                if isinstance(startwith, str):
                    prefix = text.split(startwith)[0] + startwith
                else:
                    prefix = ''
                if isinstance(endwith, str):
                    suffix = endwith + text.split(endwith)[1]
                else:
                    suffix = ''
                text = match.group(1)
            else:
                prefix = match.group(1)
                text = match.group(2)
                if match.group(3):
                    suffix = str().join(match.groups()[2:])
                else:
                    suffix = ''
            number = self.kanji2number(text)
            result = ParseNumber(prefix,  number, suffix)
        else:
            result = None

        return  result

    def parse_number(self,
            text: str,
            startwith: Optional[re.Pattern]=None,
            endwith: Optional[re.Pattern]=None,
        ) -> Optional[ParseNumber]:

        if not startwith:
            startwith = f'{NOT_NUMBERS}'             # type: ignore

        if not endwith:
            endwith = f'{NOT_NUMBERS}' + r'(.*)?'    # type: ignore

        number = re.compile(
             startwith + f'{NUMBERS}' + endwith,     # type: ignore
             re.UNICODE
        )

        match =  number.search(text)

        if match:
            if len(match.groups()) == 1 :
                if isinstance(startwith, str):
                    prefix = text.split(startwith)[0] + startwith
                else:
                    prefix = ''
                if isinstance(endwith, str):
                    suffix = endwith + text.split(endwith)[1]
                else:
                    suffix = ''
                text = match.group(1)
            else:
                prefix = match.group(1)
                text = match.group(2)
                if match.group(3):
                    suffix = str().join(match.groups()[2:])
                else:
                    suffix = ''
            number = self.number2kanji(text)               # type: ignore
            result = ParseNumber(prefix,  number, suffix)  # type: ignore
        else:
            result = None

        return  result

    def normalize_kanjinumber(self,
            text: str,
            startwith: Optional[re.Pattern]=None,
            endwith: Optional[re.Pattern]=None,
            max_try: int=5
        ) -> Optional[str]:
       """
        Parameters
        ----------
        text: str
            text which cotain numbers
        startwith: re.Pattern
            if set pattern. serach with this values for text
        endwith: re.Pattern
            if set pattern. serach with this values for text
        max_try: int
            maxium try to normalize. default is 5.

        Returns
        -------
            normalized text
       """

       normalized_text =''
       do_normalize  = True
       count = max_try
       while do_normalize and count >0:
           result = self.parse_number(text, startwith, endwith)
           if result:
               if text != result.number.as_kanji:
                   kanji_number = self.number2kanji(result.number.as_int) # type: ignore
                   normalized_text  = ( str(result.prefix)
                                + str(kanji_number.as_kanji)
                                + str(result.suffix) )
                   text = normalized_text


           result = self.parse_kanjinumber(text, startwith, endwith)
           if result:
               if text != result.number.as_kanji:
                   kanji_number = self.number2kanji(result.number.as_int) # type: ignore
                   normalized_text  = ( str(result.prefix)
                                + str(kanji_number.as_kanji)
                                + str(result.suffix ) )
                   text = normalized_text

           count -= 1
           arabic_contain = any( x in text for x in self.__MULTIBYTE_DIGITS )
           digits_contain = any( str(x) in text for x in range(10))
           do_normalize = arabic_contain or digits_contain

       return text

