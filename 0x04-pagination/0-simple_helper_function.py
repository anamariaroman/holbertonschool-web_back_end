#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index
    Args:
        page (int): number of page
        page_size (int): size of page
    Returns:
        Tuple[int, int]: (start index, end index)
    """
    end: int = page * page_size
    start: int = 0
    for _ in range(page - 1):
        start += page_size
    return (start, end)
