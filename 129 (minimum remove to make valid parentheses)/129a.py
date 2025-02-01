# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# TODO rewrite pseudocode
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass
        dim = len(s)
        open_par = '('
        close_par = ')'
        
        to_remove = set()
        # two arrays
        # one stores all the opens and their indices
        # for the opens, iterate through `s` in reverse
        # so the last open added is the first in the string
        # for O(1) access to the first open
        opens  = []
        for idx in range(dim-1, -1, -1):
            ch = s[idx]
            if ch == open_par:
                opens.append(idx)
        
        
        # the second array stores all the closes and their indices
        closes = []
        for idx, ch in enumerate(s):
            if ch == close_par:
                closes.append(idx)
        
        
        
        # compare the earliest open with the last closing
        # if they're invalid, increment `count` by 2
        # do this until until at least one array becomes empty
        
        count = 0
        while opens and closes:
            open_idx = opens.pop()
            close_idx = closes.pop()
            if not self.is_valid(open_idx, close_idx, s):
                # count += 2
                to_remove.add(open_idx)
                to_remove.add(close_idx)
        
        # increment count by the length of the non-array if any
        while opens:
            to_remove.add(opens.pop())
            
        while closes:
            to_remove.add(closes.pop())
            
            
        res = ''.join(ch for idx, ch in enumerate(s) if idx not in to_remove)
        return res
    
    def is_valid(self, idxOne, idxTwo, chars):
        if idxOne > idxTwo:
            return False
        
        dim = len(chars)
        charAfter = chars[idxOne + 1] if idxOne + 1 < dim else None
        charBefore = chars[idxTwo - 1] if idxTwo - 1 >= 0 else None
        
        return charAfter and charBefore and charAfter.isalpha() and charBefore.isalpha()
        
        
arr = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "a)b(cd",
]
foo = arr[-1]
sol = Solution()
res = sol.minRemoveToMakeValid(foo)
print(res)