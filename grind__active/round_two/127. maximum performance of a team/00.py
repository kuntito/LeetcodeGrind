from typing import List


class Solution:
    def maxPerformance(
        self, 
        n: int, 
        speed: List[int],
        efficiency: List[int],
        k: int
    ) -> int:
        self.highestPerformance = 0
        
        self.speed = speed
        self.efficiency = efficiency
        self.maxSize = k
        self.dim = n
        
        self.exploreTeams(0, [])
        
        return self.highestPerformance % (10**9 + 7)
    
    def exploreTeams(self, startIdx, team):
        if len(team) == self.maxSize:
            # print(team)
            hi = self.getPerformance(team)
            if hi > self.highestPerformance:
                self.highestPerformance = hi
            return
        
        for curIdx in range(startIdx, self.dim):
            team.append(curIdx)
            self.exploreTeams(curIdx + 1, team)
            team.pop()
        
    def getPerformance(self, team):
        totalSpeeds = sum(self.speed[idx] for idx in team)
        lowestEfficiency = min(self.efficiency[idx] for idx in team)
        
        return totalSpeeds * lowestEfficiency
    
arr = [
    [
        6,
        [2,10,3,1,5,8],
        [5,4,3,9,7,2],
        2,
    ]
]
uno, dos, tres, qua = arr[-1]
sol = Solution()
res = sol.maxPerformance(uno, dos, tres, qua)

print(res)