# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        pass
        # find the length of the longest window that's <= maxCost
        
        left = 0
        dim = len(s)
        
        maxLen = None
        tmp = 0
        
        for idx in range(dim):
            chOne = s[idx]
            chTwo = s[idx]
            
            diff = self.get_abs_diff(chOne, chTwo)
            tmp += diff
            
            while tmp > maxCost and left < idx:
                leftOne = s[left]
                leftTwo = t[left]
                
                leftDiff = self.get_abs_diff(leftOne, leftTwo)
                tmp -= leftDiff
                left += 1
            
            if tmp <= maxCost and left <= idx:
                currLen = (idx - left) + 1
                if maxLen is None:
                    maxLen = currLen
                else:
                    maxLen = max(maxLen, currLen)
                    
        return maxLen
            
            
            
    def get_abs_diff(self, chOne, chTwo):
        return abs(ord(chOne) - ord(chTwo))
    
arr = [
    ["abcd", "acde", 0],
]
foo, bar, zar = arr[-1]
sol = Solution()
res = sol.equalSubstring(foo, bar, zar)
print(res)