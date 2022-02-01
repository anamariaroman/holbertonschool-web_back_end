#!/usr/bin/env python3
"""sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum mixed list
    Args:
        mxd_lst (List[Union[int, float]]): list to sum
    Returns:
        float: result
    """
    return float(sum(mxd_lst))
