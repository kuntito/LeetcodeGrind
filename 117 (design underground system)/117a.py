# https://leetcode.com/problems/design-underground-system/description/

class UndergroundSystem:

    def __init__(self):
        pass
        self.purgatory = {}
        # (start, end) => durations[]
        self.journeys = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        pass
        self.purgatory[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        pass
    
        start_station, start_time = self.purgatory[id]
        
        journey = (start_station, stationName)
        duration = t - start_time
        
        if journey not in self.journeys:
            self.journeys[journey] = []
            
        self.journeys[journey].append(duration)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        pass
        jour = (startStation, endStation)
        lst = self.journeys[jour]
        
        return sum(lst)/len(lst)
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)