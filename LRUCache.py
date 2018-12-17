from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.cache.pop(key)     
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
        
lruCache = LRUCache(2)
lruCache.put("one", 1)
lruCache.put("two", 2)
assert(lruCache.get("two")==2)
lruCache.put("three", 3)
assert(lruCache.get("one")==-1)
assert(lruCache.get("three")==3)
assert(lruCache.get("two")==2)
lruCache.put("four", 4)
assert(lruCache.get("one")==-1)
assert(lruCache.get("three")==-1)
assert(lruCache.get("two")==2)
assert(lruCache.get("four")==4)
lruCache.put("five", 5)
assert(lruCache.get("one")==-1)
assert(lruCache.get("three")==-1)
assert(lruCache.get("two")==-1)
assert(lruCache.get("four")==4)
assert(lruCache.get("five")==5)