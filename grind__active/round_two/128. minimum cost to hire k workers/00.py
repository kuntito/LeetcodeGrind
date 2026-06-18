from typing import List


class Solution:
    def mincostToHireWorkers(
        self,
        quality: List[int],
        wage: List[int],
        k: int
    ) -> float:
        self.quality = quality
        self.wage = wage
        self.teamSize = k
        
        startIdx = 0
        teamIndices = []
        self.cheapestTeamCost = float("inf")
        
        self.exploreTeam(startIdx, teamIndices)
        
        return self.cheapestTeamCost
    
    def exploreTeam(self, startIdx, teamIndices):
        dim = len(self.quality)
        workersLeft = dim - startIdx
        workersNeeded = self.teamSize - len(teamIndices)
        
        if workersNeeded == 0:
            teamCost = self.getTeamCost(teamIndices)
            if teamCost < self.cheapestTeamCost:
                self.cheapestTeamCost = teamCost
            return
        elif workersLeft < workersNeeded:
            return
        
        for idx in range(startIdx, dim):
            teamIndices.append(idx)
            self.exploreTeam(idx + 1, teamIndices)
            teamIndices.pop()
            
    def getTeamCost(self, teamIndices):
        # TODO impl the algo to calculate team cost
        # you want to start with the highest quality
        # and work your way downwards, quality wise.
        
        # that guys pay is determined by the guys lesser.
        # this could take a minute to untangle, till then..
