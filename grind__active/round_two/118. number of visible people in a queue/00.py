from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = []
        
        dim = len(heights)
        for idx in range(dim):
            visNeiCount = 0
            lastNei = None
            for idxSearch in range(idx + 1, dim):
                curNei = heights[idxSearch]
                if lastNei is None or curNei > lastNei:
                    visNeiCount += 1
                    lastNei = curNei
                
            res.append(visNeiCount)
            
        return res
    
arr = [
    [10,6,8,5,11,9],
]
foo = arr[-1]
sol = Solution()
res = sol.canSeePersonsCount(foo)
print(res)