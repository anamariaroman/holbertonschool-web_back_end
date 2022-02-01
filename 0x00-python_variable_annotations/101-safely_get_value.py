#!/usr/bin/env python3
"""safely_get_value module"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Gets value safely.
    Args:
        dct (Mapping): dictionary
        key (Any): a key
        default (Union[T, None], optional): default value. Defaults to None.
    Returns:
        Union[Any, T]: value in key position of dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
