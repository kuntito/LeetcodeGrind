# https://leetcode.com/problems/lfu-cache/description/

from collections import defaultdict, OrderedDict, 

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        oldfreq = self.key2freq[key]
        self.key2freq[key] = oldfreq + 1
        self.freq2key[oldfreq].pop(key)
        if not self.freq2key[oldfreq]:
            del self.freq2key[oldfreq]
        self.freq2key[oldfreq + 1][key] = 1
        if self.minf not in self.freq2key:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return

        if len(self.key2val) == self.cap:
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1




sol = LFUCache(2)
sol.put(1, 1)
sol.put(2, 2)
sol.get(1)
sol.put(3, 3)
sol.get(2)
sol.get(3)
sol.put(4, 4)
sol.get(1)
sol.get(3)
sol.get(4)