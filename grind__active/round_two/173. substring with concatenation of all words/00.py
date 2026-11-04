from typing import List


class Solution:
    def findSubstring(
        self,
        s: str,
        words: List[str]
    ) -> List[int]:
        dim = len(s)
        self.s = s
        self.words = words
        self.wordDict = self.getDict(words)
        
        res = []
        for idx in range(dim):
            if self.isGroup(idx):
                res.append(idx)
                
        return res
    
    def getDict(self, arr):
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
            
        return counter
    
    
    def getSliceAt(self, startIdx):
        dim = len(self.words)
        itemLen = len(self.words[0])
        
        groupLen = dim * itemLen
        slice = self.s[startIdx: startIdx + groupLen]
        
        return slice if len(slice) == groupLen else None
    
    
    def isGroup(self, startIdx):
        slice = self.getSliceAt(startIdx)
        if slice is None:
            return False
        
        # print(slice)
        
        itemLen = len(self.words[0])
        wordDict = self.wordDict.copy()
        for i in range(0, len(slice), itemLen):
            candidate = slice[i:i+itemLen]
            
            if candidate in wordDict:
                wordDict[candidate] -= 1
                
                if wordDict[candidate] == 0:
                    del wordDict[candidate]
            else:
                return False
            
            
        return True


arr = [
    [
        "wordgoodgoodgoodbestword",
        ["word","good","best","word"],
    ],
    [
        "barfoofoobarthefoobarman",
        ["bar","foo","the"],
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findSubstring(foo, bar)
print(res)