# https://leetcode.com/problems/minimum-window-substring/description/

# TODO https://neetcode.io/solutions/minimum-window-substring
# TODO write your implementation

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        # this would work by creating a counter for `t`
        # and a temporary counter for the sliding window in `s`
        counter = Counter(t)
        window = Counter()
        
        # the trick here is a variable called `matches`
        # `matches` is incremented when
        # the count of a character in the window == the count of the character in `counter`
        matches = 0
        need = len(counter)
        
        res = None
        # iterate through `s`, adding each character to the `window`
        # declare a variable, `left` to determine the start of the window
        left = 0
        for idx, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            
            if window[ch] == counter[ch]:
                matches += 1
            
            # when `matches == len(counter)`
            # the window is valid, store the `result`
            if matches == need:
                pass
                if res is None:
                    res = [left, idx + 1]
                
                # keep moving `left` forward, updating the matches
                # stop moving when `matches` is invalid and s[left] in counter
                while True:
                    leftCh = s[left]
                    window[leftCh] -= 1
                    
                    if window[leftCh] < counter[leftCh]:
                        matches -= 1
                        
                    # if matches != need and s[left] in ..
                    
                    left += 1
        
        

    
arr = [
    ["ADOBECODEBANC", "ABC"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minWindow(foo, bar)
print(f'res is "{res}"')