# https://leetcode.com/problems/reorganize-string/

# what's the challenge?
# we are to implement a function, `reorganizeString`
# this function takes a string argument, `s`

# and we are to reorder the characters in `s` such that no two consecutive characters
# are the same
# i.e. s = "aabc"
# this is invalid because of "aa.."

# after reordering, we can have "abac" or "acab" or "abca"
# we can order however we want but back to back characters should be distinct

# the way to about this is to pick a character from `s`
# add it to the result, `res`
# then pick a different character from `s`
# and keep doing this until we run out

# we would need a way to track the characters in `s` though
# and can we select characters in any order?
# consider "aab"

# if we selected "b" first, then added "a"
# we would have painted ourself into a corner since our only option is "baa"

# however, if we picked "a" first, then "b", we can have "aba"
# which is valid. in other words, we want to pick the most frequent different element first
# we need to store each element with it's frequency

# it's sounding like heap
# one thing i left out, if it's impossible to rearrange the string how we want
# we should return an empty string

# back to the heap
# let's use a maxheap where we store (freq, ch)
# declare our result variable, `res`

# while there's values in the max heap
# we take the topmost value and compare it with the last value in `res`
# if they are different, we add that ch to res, update the frequency of the heap item
# (freq, ch) and re-add it to the heap

# what if the topmost character is the same as the last value in `res`
# do we return ""
# well, it's possible there's two characters with the same top frequency
# so we'd need to check twice, if there's no second character with topmost frequency, then we return ""

# let's write the code
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        pass
        # we need the frequency of all ch's
        # hashmap way
        charCounter = {}
        for ch in s:
            charCounter[ch] = charCounter.get(ch, 0) + 1
            
        # now, we add (freq, ch) to the maxHeap
        # i.e. (-1 * freq, ch) since python has no maxHeap
        
        maxHeap = []
        for ch, freq in charCounter.items():
            heapq.heappush(maxHeap, (-1 * freq, ch))
            
        # declare `res`
        res = []
        # now while maxHeap has values
        while maxHeap:
            topMost = heapq.heappop(maxHeap)
            freq, ch = topMost
            
            if not res or res[-1] != ch:
                self.appendChar(topMost, res, maxHeap)
            elif res[-1] == ch:
                # in this case we need to check if there's another topmost
                # if the heap still contains values, if it does, we take that as the topmost
                # but make sure to re-add the old topmost
                # if the heap is empty, we return ""
                
                if not maxHeap:
                    return ""
                
                
                oldTopMost = topMost
                
                topMost = heapq.heappop(maxHeap)
                self.appendChar(topMost, res, maxHeap)
                    
                heapq.heappush(maxHeap, oldTopMost)
                
        return "".join(res)
    
    def appendChar(self, topMost, res, maxHeap):
        freq, ch = topMost
        res.append(ch)
        # now we update frequency and re-add to the heap
        # remember, `freq` is negative, so adding is reducing
        freq += 1
        # if `freq` hits zero, we shouldn't re-add
        if freq < 0:
            heapq.heappush(maxHeap, (freq, ch))
