#!/usr/bin/env python3
"""to_kv module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv
    Args:
        k (str): string
        v (Union[int, float]): int or float
    Returns:
        Tuple[str, float]: [description]
    """
    return (k, v**2)
