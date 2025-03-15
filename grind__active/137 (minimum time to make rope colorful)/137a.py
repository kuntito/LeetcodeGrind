# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

import heapq
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        pass
        # find a consecutive streak chars in `colors`
        count = 0
        
        # put all the time for all the chars in the streak inside `minHeap`
        # at the end of the streak add all the times except the last one to
        # `count`
        
        uno, dos = 0, 0
        dim = len(colors)
        
        while dos < dim:
            pass
            c = colors[dos]
            
            # this is the end of a streak
            if (dos + 1 == dim) or (dos + 1 < dim and c != colors[dos + 1]):
                dist = (dos - uno) + 1
                
                if dist >= 2:
                    tmp = 0
                    highest = None
                    while uno <= dos:
                        tmp += neededTime[uno]
                        if highest is None:
                            highest = neededTime[uno]
                        else:
                            highest = max(
                                highest,
                                neededTime[uno]
                            )
                    
                        uno += 1
                    if highest:
                        count += tmp - highest
                else:
                    uno = dos + 1
                
                    
            dos += 1
            
        return count
    
arr = [
    ["abc", [1,2,3]],
    ["aabaa", [1,2,3,4,1]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minCost(foo, bar)
print(res)