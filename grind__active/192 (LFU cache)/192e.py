# https://leetcode.com/problems/lfu-cache/description/

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}
        self.keyToFreqMap = {}  # Maps key to its current frequency count

        # Maps frequency count to an OrderedDict of keys (to maintain LRU order among same frequency)
        self.freqMap = defaultdict(OrderedDict)

        self.minFreq = 0

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.get(key)  # Update frequency as this is also an access
            return

        # If cache is full, evict the least frequently used and least recently used key
        if len(self.cache) == self.capacity:
            key_to_remove, _ = self.freqMap[self.minFreq].popitem(last=False)
            del self.cache[key_to_remove]
            del self.keyToFreqMap[key_to_remove]

        # Insert the new key with frequency 1
        self.cache[key] = value
        self.keyToFreqMap[key] = 1
        self.freqMap[1][key] = None  # Value is irrelevant; we're only using the keys
        self.minFreq = 1  # Reset min frequency for new key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found

        # you get the frequency of the key
        currFreq = self.keyToFreqMap[key]
        
        # Remove key from current frequency list
        del self.freqMap[currFreq][key]
        
        # if there are no more items with that frequency
        # delete that frequency from the frequencyMap
        if not self.freqMap[currFreq]:
            del self.freqMap[currFreq]
            if self.minFreq == currFreq:
                self.minFreq += 1  # Increment min frequency if needed

        # Add key to next frequency list
        new_frequency = currFreq + 1
        self.keyToFreqMap[key] = new_frequency
        self.freqMap[new_frequency][key] = None  # Maintain order for LRU

        return self.cache[key]




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