# https://leetcode.com/problems/minimum-window-substring/description/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        # create a counter for string `t`, `t_count`
        t_count = Counter(t)
        
        # create a counter for the window, `count`
        count = Counter()

        # two pointers, `left` and `right`
        # `right` keeps track of every character in `count`
        
        
        res = None
        
        left, right = 0, 0
        while right < len(s):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
                
            # when `count` contains enough characters to match `t_count`
            # move `left` forward removing every character from `count` and updating the window
            # do this until the match no longer exists
            while (t_count & count) == t_count:
                print('cheers')
                res = self.update_res(left, right, res)
                count[s[left]] -= 1
                left += 1
                
            # while the left pointer is valid and it's character is not in `t_count`
            # move it forward until it reaches a character in `t_count` or goes out of bounds
            while left < len(s) and s[left] not in t_count:
                chLeft = s[left]
    
                if chLeft in count:
                    count[chLeft] -= 1
    
                left += 1

            if left > right:
                right = left
            else:
                right += 1
                
            
        if res is None:
            ans = ""
        else:
            start, end = res
            ans = s[start:end]
            
        return ans


    def update_res(self, left, right, res):
        if res is None:
            return (left, right + 1)
        
        s, e = res
        currLen = e - s
        
        newLen = (right + 1) - left
        if newLen < currLen:
            return (left, right + 1)
        return res

    
arr = [
    ["ADOBECODEBANC", "A"],
    ["ab", "b"],
    ["ADOBECODEBANC", "ABC"],
    ["a", "b"],
    ["bba", "ab"],
    ["cabwefgewcwaefgcf", "cae"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minWindow(foo, bar)
print(f'res is "{res}"')