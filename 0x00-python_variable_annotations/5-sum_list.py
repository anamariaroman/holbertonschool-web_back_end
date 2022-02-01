#!/usr/bin/env python3
"""sum_list module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of float list
    Args:
        input_list (List[float]): list of float numbers
    Returns:
        float: return sum of all float number in a list
    """
    return float(sum(input_list))
