#!/usr/bin/env python3
""" Basic Caching"""


class BasicCache(BaseCaching):
    """a caching class that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Adds to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item


    def get(self, key):
        """Gets an item by key"""
        if key is None or key not in sel.cache_data:
            return None
        return self.cache_data[key]
