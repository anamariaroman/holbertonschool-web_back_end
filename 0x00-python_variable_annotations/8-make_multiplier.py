#!/usr/bin/env python3
"""make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier
    Args:
        multiplier (float): number
    Returns:
        Callable[[float], float]: [description]
    """
    return lambda x: x * multiplier
