# https://leetcode.com/problems/dota2-senate/description/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass
        # r wants to cancel out  d
        # d wants to cancel out r
        
        # run through senate
        # keep track of rCount, dCount
        # update rCount and dCount
        
        # for every r you see where rCount > 0, decrement dCount by 1
        # for every d you see where dCount > 0, decrement rCount by 1
        
        # return whoever is higher
        
        rCount, dCount = 0, 0
        for ch in senate:
            pass
            if ch == 'R':
                rCount += 1
                if rCount > 0:
                    dCount -= 1
            else:
                dCount += 1
                if dCount > 0:
                    rCount -= 1
                
        # print(dCount)
    
        if rCount == dCount:
            return 'Radiant' if senate[0] == 'R' else "Dire"
        return 'Radiant' if rCount > dCount else "Dire"
    
    
arr = [
    "R",
    "RD",
    "RDD",
    "RRDDD",
    "DDRRR"
]
foo = arr[-1]
sol = Solution()
res = sol.predictPartyVictory(foo)

print(res)
        