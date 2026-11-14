# https://leetcode.com/problems/dota2-senate/

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()


        dim = len(senate)
        for idx in range(dim-1, -1, -1):
            ch = senate[idx]
            if ch == 'R':
                radiant.appendleft(idx)
            elif ch == 'D':
                dire.appendleft(idx)
              
        while dire and radiant:
            newDire = deque()
            newRadiant = deque()
            while dire or radiant:
                if dire and radiant:
                    if dire[0] < radiant[0]:
                        newDire.appendleft(dire.popleft())
                        radiant.popleft()
                    elif radiant[0] < dire[0]:
                        newRadiant.appendleft(radiant.popleft())
                        dire.popleft()
                elif dire:
                    newDire.appendleft(dire.popleft())
                    if newRadiant:
                        newRadiant.popleft()
                elif radiant:
                    newRadiant.appendleft(radiant.popleft())
                    if newDire:
                        newDire.popleft()
                    
                    
            dire = newDire
            radiant = newRadiant
                 
        if radiant:
            return 'Radiant'
        
        return 'Dire'


arr = [
    "RDD",
    "RD",
    "DDRRRR",
]
foo = arr[-1]
sol = Solution()

res = sol.predictPartyVictory(foo)
print(res)