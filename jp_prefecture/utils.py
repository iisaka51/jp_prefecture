import pandas as pd
from typing import Union

def is_alpha(word: str)-> bool:
    """ Check word is alphabet.
    Parameters
    ----------
    word: str
        any string

    Returns
    -------
    validate result: bool
        if all characters of word, return ``True`` otherwise return ``False``
    """
    try:
        return word.encode('ascii').isalpha()
    except:
        return False

def is_alnum(word: str)-> bool:
    """ Check word is alphabet and digits.
    Parameters
    ----------
    word: str
        any string

    Returns
    -------
    validate result: bool
        if all characters of word, return ``True`` otherwise return ``False``
    """
    try:
        return word.encode('ascii').isalnum()
    except:
        return False



def df_compare(
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        diff_count: bool=False
    ) -> Union[int,bool]:
    """ Compare DataFrame
    Parameters
    ----------
    df1: pd.DataFrame, df2: pd.DataFrame
        any DataFrame to compare
    diff_count: bool
        if set to ``True`, Return counts of diffs.

    Returns
    -------
    validate result: Union[bool,int]
    """

    diff_df = pd.concat([df1,df2]).drop_duplicates(keep=False)
    diffs = len(diff_df)
    result = diffs if diff_count else diffs == 0
    return result
