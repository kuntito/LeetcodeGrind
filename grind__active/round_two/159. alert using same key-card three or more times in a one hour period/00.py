class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        # pair them up for sorting.
        pairedUpData = []
        for name, time in zip(keyName, keyTime):
            pair = (name, time)
            pairedUpData.append(pair)
        
        
        pairedUpData.sort(key=lambda x: self.getMinutes(x[1]))
        
        found = set()
        personMap = {}
        for pair in pairedUpData:
            person, time = pair
            
            if person in found: continue
            
            if person not in personMap:
                personMap[person] = []
                
            personMap[person].append(time)
            if self.checkViolation(personMap[person]):
                found.add(person)
                
        return sorted(list(found))
    
    def checkViolation(self, times):
        if len(times) < 3:
            return False
        
        targets = [
            times[-1],
            times[-2],
            times[-3],
        ]
        
        targets = [self.getMinutes(x) for x in targets]

        smallest = min(targets)
        largest = max(targets)
        
        return largest - smallest <= 60
        
            
    
    def getMinutes(self, timeStr):
        hours, mins = timeStr.split(":")
        
        sixty = 60
        hoursInMinutes = int(hours) * sixty
        
        return hoursInMinutes + int(mins)
    
    
sol = Solution()

keyName = ["a", "a"]
keyTime = ["11:00", "10:59"]
sol.alertNames(keyName, keyTime)