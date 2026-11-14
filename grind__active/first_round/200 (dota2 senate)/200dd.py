# https://leetcode.com/problems/dota2-senate/

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        totalRadiant = sum(1 for ch in senate if ch == 'R')
        totalDire = len(senate) - totalRadiant
        
        iterating = deque(senate)
        iterated = deque()
        
        skipDire = 0
        skipRadiant = 0
        
        while totalRadiant > 0 and totalDire > 0:
            for p in iterating:
                if p == 'R':
                    if skipRadiant:
                        skipRadiant -= 1
                        continue
                    iterated.append(p)
                    
                    skipDire += 1
                    totalDire -= 1
                elif p == 'D':
                    if skipDire:
                        skipDire -= 1
                        continue
                    
                    iterated.append(p)
                    
                    skipRadiant += 1
                    totalRadiant -= 1
                    
            iterating = iterated
            iterated = deque()
                    
        if totalRadiant > 0:
            return 'Radiant'
        
        return 'Dire'

arr = [
    "DDRRRR",
    "RD",
    "RRDDD",
    "RDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRDRRDRDDRRDDRDRRDRDDRDRRDDRRDRDDRRDDRDRRDDRRDRDDRDRRDRDDRR",
    "RDD",
]
foo = arr[-1]
sol = Solution()

res = sol.predictPartyVictory(foo)
print(res)