#!/usr/bin/env python3
"""element length module"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements of the list with its length
    Args:
        lst (Iterable[Sequence]): list
    Returns:
        List[Tuple[Sequence, int]]: a tuple
    """
    return [(x, len(x)) for x in lst]
