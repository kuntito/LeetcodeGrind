class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.explore(s1, s2)
    
    def explore(self, s1, s2):
        if len(s1) == 1 and len(s2) == 1:
            return s1 == s2
        
        firstSplit, firstScrambledSplit, secondSplit, secondScrambledSplit = self.getSplits(s1, s2)
        
        return self.explore(firstSplit, firstScrambledSplit) and self.explore(secondSplit, secondScrambledSplit)
    
    def getSplits(self, s1, s2):
        startCh, endCh = s2[0], s2[-1]
        
        idxStart = s1.find(startCh)
        if idxStart == -1:
            return False
                
        idxEnd = s1.find(endCh)
        if idxEnd == -1:
            return False
        
        if idxStart > idxEnd:
            secondSplit = s1[idxStart:]
            secondScrambledSplit = s2[:len(secondSplit)]
            
            firstSplit = s1[:idxStart]
            firstScrambledSplit = s2[len(secondSplit):]
            
            return firstSplit, firstScrambledSplit, secondSplit, secondScrambledSplit
        elif idxEnd > idxStart:
            secondSplit = s1[idxEnd:]
            secondScrambledSplit = s2[-len(secondSplit):]
            
            firstSplit = s1[:idxEnd]
            firstScrambledSplit = s2[:-len(secondSplit)]
            
            return firstSplit, firstScrambledSplit, secondSplit, secondScrambledSplit
        
        
        

arr = [
    ["great", "rgeat"],
    ["ab", "ba"],
]


foo, bar = arr[-1]
sol = Solution()

res = sol.isScramble(foo, bar)
print(res)