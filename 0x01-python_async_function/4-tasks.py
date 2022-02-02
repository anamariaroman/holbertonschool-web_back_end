#!/usr/bin/env python3
"""task wait n module"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with max_delay.
    Args:
        n (int): times
        max_delay (int): max number delay
    Returns:
        List[float]: list with result of called task_wait_random n times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
