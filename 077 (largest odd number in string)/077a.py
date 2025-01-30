# https://leetcode.com/problems/largest-odd-number-in-string/description/

# TODO https://neetcode.io/solutions/largest-odd-number-in-string
class Solution:
    def largestOddNumber(self, num: str) -> str:
        pass
        # iterate from behind with index
        # the first odd number you find
        # return num[:idx + 1]
        
        dim = len(num)
        for idx in range(dim-1, -1, -1):
            n = int(num[idx])
            if n % 2:
                return f"{num[:idx+1]}"
        
        return ""
    
arr = [
    "35427",
    "4206",
    "52",
]
foo = arr[-1]
sol = Solution()
res = sol.largestOddNumber(foo)

print(res)