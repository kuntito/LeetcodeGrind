class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        longest = 0
        
        streakStartIdx = 0
        firstNegIdx = None
        
        negCount = 0
        
        for idx, n in enumerate(nums):
            if n == 0:
                streakStartIdx = idx + 1
                firstNegIdx = None
                negCount = 0
                continue
            
            
            if n < 0:
                negCount += 1
                if firstNegIdx is None:
                    firstNegIdx = idx
                
            if negCount % 2 == 0:
                streakLen = idx - streakStartIdx + 1
            else:
                streakLen = idx - firstNegIdx
                
            if streakLen > longest:
                longest = streakLen
                
        return longest
    
    
arr = [
    [-1,2],
    [-1,-2,-3,0,1],
    [0,1,-2,-3,-4],
    [1,-2,-3,4],
]
foo = arr[-1]
sol = Solution()
res = sol.getMaxLen(foo)

print(res)