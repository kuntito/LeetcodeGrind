from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.totalCheckpoints = len(tickets) + 1
        
        self.destinationGraph = self.getDestinationGraph()
        
