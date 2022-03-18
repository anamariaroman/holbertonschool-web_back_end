#!/usr/bin/env python3
"""
Cache web module
"""

import redis
import requests
from typing import Callable
from functools import wraps

rd = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """requests"""

    @wraps(method)
    def wrapper(url):
        """wrapper"""
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """pages"""
    req = requests.get(url)
    return req.text
