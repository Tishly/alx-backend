#!/usr/bin/env python3
"""
LFU Cache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU cache class
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.freq = {}
        self.min_freq = 0

    def put(self, key, item):
        """
        Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_item()
                self.cache_data[key] = item
                self.freq[key] = 1
                self.min_freq = 1

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        return self.cache_data[key]

    def remove_item(self):
        """Remove the least frequency used item (LFU algorithm)"""
        items = list(self.cache_data.items())
        lfu_items = sorted(items, key=lambda x: self.freq[x[0]])
        lfu_items = [(k, v) for k, v in lfu_items
                     if self.freq[k] == self.freq[lfu_items[0][0]]]
        if len(lfu_items) == 1:
            key, _ = lfu_items[0]
            del self.cache_data[key]
            del self.freq[key]
        else:
            lru_key = self.get_lru_key(lfu_items)
            del self.cache_data[lru_key]
            del self.freq[lru_key]

        print("DISCARD:", lru_key)

    def get_lru_key(self, items):
        """
        Get the least recently used item key (LRU algorithm)
        """
        lru_key = items[0][0]
        lru_time = self.timestamps[lru_key]
        for key, _ in items[1:]:
            if self.timestamps[key] < lru_time:
                lru_key = key
                lru_time = self.timestamps[key]
        return lru_key
