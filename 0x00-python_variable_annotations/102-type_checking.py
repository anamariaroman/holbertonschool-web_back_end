#!/usr/bin/env python3
"""zoom_array module"""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list
    Args:
        lst (Tuple): a tuple
        factor (int, optional): range. Defaults to 2.
    Returns:
        List: list with range 2 or factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
