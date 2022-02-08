#!/usr/bin/python3
"""LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class
    Args:
        BaseCaching (class): Basic class for this class
    """
    def __init__(self):
        """constructor"""
        super().__init__()
        self.__keys = []
        self.__counter = {}

    def put(self, key, item):
        """put item into cache_data with LFU algorithm
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if not key or not item:
            return
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            self.discard()
        if key not in self.cache_data:
            self.__counter[key] = 1
        else:
            self.__counter[key] += 1
            self.__keys.remove(key)
        self.__keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self.__counter[key] += 1
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]

    def discard(self):
        """discard item and print
        """
        m_time = min(self.__counter.values())
        keys = [k for k, v in self.__counter.items() if v == m_time]
        low = 0
        while self.__keys[low] not in keys:
            low += 1
        discard = self.__keys.pop(low)
        del self.cache_data[discard]
        del self.__counter[discard]
        print('DISCARD: {}'.format(discard))
