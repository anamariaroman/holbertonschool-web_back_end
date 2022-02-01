#!/usr/bin/env python3
"""safe_first_element module"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Gets first element safely.
    Args:
        lst (Sequence[Any]): a sequence.
    Returns:
        Union[Any, None]: None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
