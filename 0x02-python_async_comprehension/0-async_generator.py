#!/usr/bin/env python3
"""async generator module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generator of random float number
    Returns:
        Generador[float, None, None]: 10 random float numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
