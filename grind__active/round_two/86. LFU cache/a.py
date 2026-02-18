# https://leetcode.com/problems/lfu-cache/

# what's today's situation?

# i want to implement a data structure.
# i want to write a class.

# i want to implement a class.
# three methods.

# the constructor,`__init__`
# a `get` and a `put` method.

# okay, what are we doing in these functions?

# let's start with the class.
# the class helps us store integers.

# every integer has a `key`
# so the put method takes two parameters.

# two integer parameters

# `key` and `value`

# the get method takes one parameter, `key`
# and returns the associated value.

# so what's the catch?
# there's a maximum number of keys we can store.

# once, we're at capacity.
# adding another key would mean removing the least frequently used key.

# if multiple keys tie in their least frequency..
# remove the one least recently used.

# a key is considered used on both `get` and `put` operations.

# we want to sort integers by frequency
# no, we want to sort integer keys by use frequency

# i'd need a counter to track use frequency for every key

# `useFreqCounter`

# every time, i add a key..
# i update the `useFreqCounter`, set the freq to `1`
# what if the `useFreqCounter` is full.

# we remove the least frequent least recent key
# but how do we know this?

# sounds like a heap problem..
# the top of the heap handles the least frequent least recent key

# and how do these heap items look like
# (keyFreq, keyRecency, key)

# the least frequent value would be the lowest value.. so min heap
# the least recent key would also be the lowest value..

# Python naturally handles the tie..
# if two keys have the same frequency, the min heap sorts by recency

# so i can simply remove the topmost heap item and it's a day.

# i'd need a heap, `minHeap`

# and `get`, this simply returns the value associated with a key
# if no value is associated, it returns `-1`

# i left something out with the put operation
# when at capacity, we remove the least frequent least recent key
# and we should make sure to remove this key from `useFreqCounter`

# and `keyMap`, `keyMap` is mentioned here for the first time.
# this is where i store the key to value mappings.

# removing the topmost heap item invalidates the key in both variables.
# `useFreqCounter` and `keyMap`

# i failed to mention, how i'd track the recency..
# every key should be paired with it's recency..

# when you store a key, you're doing two things..
# key => (value, recency)

# but what is this recency?
# a global integer, `self.recency`

# incremented on every get and every put..
# the lower the number, the less the recency..

# so the key map now takes `key => (value, recency)`
# and the frequency counter? stays as is.

# when you get a value.. you have to update the recency..
# yes, you do..
# but how do you update the heap?

# the recency is tied to the key.
# the key is only added to the heap on put operations.

# what if we also add the key on get operations?
# wouldn't this result in duplicate keys in the heap..

# yes, but we would know which one is legit
# using `useFreqCounter` and `keyMap`
# both variables know the correct frequency and recency for any given key.

# so for every key, we can always cross-check
# if both frequency and recency match, we know we're dealing with the real one.

# and now, how does the put operation change?
# well, we add recency to the map..

# and the get..
# we add a new heap item.. to minHeap

# error, i tried to access the element of a hashmap without
# using square brackets or it's get method.

# i did `_, keyRecency = self.keyMap` instead of
# `_, keyRecency = self.keyMap[key]`

# perhaps, a consequence of juggling several mental tasks.

# error, i stored the keyMap values as tuples (value, recency)
# and attempted to update `recency` inside the keyMap.. by accessing the tuple..

# this wouldn't work, either i make it a list
# or i add a new tuple to the `self.keyMap`

# since, i wrote it with the assumption that it's a list
# i'd simply just change it to a list [value, recency]

# TODO the test case failed.
# fix it.

# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

import heapq

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.keyMap = {}
        self.useFreqCounter = {}
        self.minHeap = []
        self.recency = 0

    def get(self, key: int) -> int:
        # so what are we doing here..
        # does the key exist?
        if key not in self.keyMap:
            return -1
        
        # and if the key exists..
        # update frequency, recency and add a new heap item..
        
        self.useFreqCounter[key] += 1
        
        keyValAndRecency = self.keyMap[key]
        
        val = keyValAndRecency[0]
        keyValAndRecency[1] = self.recency
        
        keyNewFreq = self.useFreqCounter[key]
        keyNewRecency = self.keyMap[key][1]
        
        # (keyFreq, keyRecency, key)
        heapItem = (keyNewFreq, keyNewRecency, key)
        
        heapq.heappush(self.minHeap, heapItem)
        
        self.recency += 1
        
        return val
        
        
        

    def put(self, key: int, value: int) -> None:
        if len(self.keyMap) == self.capacity:
            self.removeHeapTop()
            
        self.keyMap[key] = [value, self.recency]
        self.useFreqCounter[key] = self.useFreqCounter.get(key, 0) + 1
        
        keyFreq = self.useFreqCounter[key]
        _, keyRecency = self.keyMap[key]
        
        # (keyFreq, keyRecency, key)
        heapq.heappush(
            self.minHeap, 
            (
                keyFreq,
                keyRecency,
                key
            ),
        )
        
        self.recency += 1
            
    def removeHeapTop(self):
        # how would this work..
        # remove the top heap item
        
        # if it's frequency and recency match the current values in 
        # self.keyMap and self.useFreqCounter
        
        # you're done..
        # if not, remove another value.. until this is True..
        
        # is it possible to remove the wrong value?
        # nah, the topmost element is always the least frequen and least recent
        
        # the only reason it would be invalid is say
        # you add (3, 1, 5)
        
        # the freq is 3
        # recency is 1
        # and key is 5
        
        # say you call get(5)
        # this adds a new item to the heap
        # (3, 2, 5)
        
        # the freq is still 3
        # recency is now 2, invalidating the previous entry
        # and key is still 5
        
        # so the valid least frequent least element is (3, 2, 5)
        # even though (3, 1, 5) is on top of the heap
        
        while True:
            keyFreq, keyRecency, key = heapq.heappop(self.minHeap)
            
            if keyFreq == self.useFreqCounter[key] and keyRecency == self.keyMap[key][1]:
                return
