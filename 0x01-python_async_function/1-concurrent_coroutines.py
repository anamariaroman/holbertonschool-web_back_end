#!/usr/bin/env python3
"""wait n times module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute n times wait_random method
    Args:
        n (int): times
        max_delay (int): max number
    Returns:
        List[float]: Result list
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
