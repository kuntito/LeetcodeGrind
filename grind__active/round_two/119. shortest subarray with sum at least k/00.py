from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pass
    
        windowSum = 0
        windowStartIdx = 0
        
        shortestWinLen = None
        
        for idx, n in enumerate(nums):
            windowSum += n
            
            while (windowStartIdx < len(nums) and nums[windowStartIdx] < 0) or windowSum >= k:
                if windowSum >= k:#
                    winLen = (idx - windowStartIdx) + 1
                    if shortestWinLen is None:
                        shortestWinLen = winLen
                    elif winLen < shortestWinLen:
                        shortestWinLen = winLen
                
                windowSum -= nums[windowStartIdx]
                windowStartIdx += 1
                
            
        return shortestWinLen if shortestWinLen is not None else -1
    
                
arr = [
    [[1], 1],
    # [[84,-37,32,40,95], 167],
    # [[1, 2, 2], 4],
    [[45,95,97,-34,-42], 21],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shortestSubarray(foo, bar)
print(res)