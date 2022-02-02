#!/usr/bin/env python3
"""wait random module"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a task
    Args:
        max_delay (int): max dalay number
    Returns:
        asyncio.Task: task to return
    """
    return asyncio.create_task(wait_random(max_delay))
