from typing import Union, Optional

def validate_checkdigit(
        number: Union[int, str],
        num_digits: Optional[int]=None,
        weights: Optional[list]=None,
    )-> Optional[Union[int,str]]:
    """ Validate check-digit as mod 11.
    Parameters
    ----------
    number: Union[int, str]
        to validate code
    num_digits: int
        the number of digits or chracters. default is None.
        to use length of number as string.
    weights: Optional[list]
         the weighting factors associated with each digit.
         default is None:
         i.e: to use [6,5,4,3,2] if num_digits is 5
              or length of numbers as string.

    Returns:
        result: return code without checkdigit if code is valid, otherwise None.
    """

    input_as_int = False
    if isinstance(number, int):
        input_as_int = True
        number = str(number)

    for r in ((".", ""),("-","")):
        number = number.replace(*r)

    if num_digits:
        number=number.zfill(num_digits)

    if len(number) != num_digits:
        check_digit = int(number[-1])
        number = number[:-1]
    else:
        return [number, int(number)][input_as_int]   # type: ignore

    len_number = len(number)
    if not num_digits:
        num_digits = len_number

    if len_number != num_digits:
        result=None
    else:
        weights = weights or [x for x in range(num_digits + 1, 1, -1)]
        result = sum(w * (int(x)) for w, x in zip(weights, number))
        result = (11 - (result % 11)) == check_digit

    number = [number, int(number)][input_as_int]     # type: ignore
    result = number if result else None
    return result

def calc_checkdigit(
        number: Union[int, str],
        num_digits: int=0,
        weights: Optional[list]=None,
        only_checkdigit: bool = False,
    ) -> Optional[Union[int, str]]:
    """ Validate check-digit as mod 11.
    Parameters
    ----------
    number: Union[int, str]
        the number or charaters for generate check digits.
    num_digits: int
        the number of digits or chracters. default is None.
        to use length of number as string.
    weights: Optional[list]
         the weighting factors associated with each digit.
         default is None:
         i.e: to use [6,5,4,3,2] if num_digits is 5
              or length of numbers as string.
    only_checkdigit: bool
         if set ``True``, return only check digit.

    Returns:
        result: Optional[Union[int, str]]
        return code is same as type at input type of `number`.
        input str -> return str, input int -> ireturn int.
    """

    if isinstance(number, int):
        input_as_int = True
        number = str(number)
    elif isinstance(number, str):
        input_as_int = False
    else:
        return None

    for r in ((".", ""),("-","")):
        number = number.replace(*r)

    if number and not num_digits:
        num_digits = len(number)

    if num_digits and len(number) < num_digits:
        number = number.zfill(num_digits)

    weights = weights or [x for x in range(num_digits+1, 1, -1)]
    result = sum(w * (int(x)) for w, x in zip(weights, number))
    checkdigit = str(11 - (result % 11))   # type: ignore
    number = number + checkdigit           # type: ignore
    if input_as_int:
        number = int(number)
        checkdigit = int(checkdigit)       # type: ignore
    if only_checkdigit:
        return checkdigit
    else:
        return number

