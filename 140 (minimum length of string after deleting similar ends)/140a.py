# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/

class Solution:
    def minimumLength(self, s: str) -> int:
        # two indices
        dim = len(s)
        left, right = 0, dim - 1
        
        # ensure the characters at `left` and `right` are the same
        # once true, move them towards each other one step at a time
        # both cannot meet
        
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
            # check if either one can still move forward without overlapping the next index
            while left <= right and s[left] == s[left-1]:
                left += 1
                
            while left < right and s[right] == s[right + 1]:
                right -= 1
                
        
        # print(left, right)
        # return the length of the substring s[left: right+1]
        return len(s[left: right+1]) 
        
    
arr = [
    "abbba",
    "abbbbbbbbbbbbbbbbbbba",
    "aabccabba",
    "cabaabac",
    "ca",
    
]
foo = arr[-1]
sol = Solution()
res = sol.minimumLength(foo)
print(res)
