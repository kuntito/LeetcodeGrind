# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

# i'd suggest a sliding window
# since we want to know not to exceed `k` chars
# for every ch we add to the window, we want to ensure, we're not crossing
# the k boundary

# if we do, we run a while loop till we don't
from collections import defaultdict

# trying to hit the timer, i've misread the question again.
# i want a substring such that the amount of unique characters are not more than `k`

# i don't need a hashmap
# i need a set, if adding a char to a set would make it's length greater than `k`
# move the left pointer forward


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        
        leftIdx = 0
        longest = 0
        window = defaultdict(int)
        
        for rightIdx, ch in enumerate(s):
            while leftIdx < rightIdx and ch not in window and len(window) == k:
                leftCh = s[leftIdx]
                window[leftCh] -= 1
                
                if window[leftCh] == 0:
                    del window[leftCh]
                
                leftIdx += 1

            window[ch] += 1
                
            winLen = (rightIdx - leftIdx) + 1
            if winLen > longest:
                longest = winLen
                
        return longest
            

    
arr = [
    ["eceba", 2],
    ["aa", 1],
    ["abaccc", 2],
    ["a", 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.lengthOfLongestSubstringKDistinct(foo, bar)
print(res)