from typing import List


class Solution:
    def wordBreak(
        self,
        s: str,
        wordDict: List[str]
    ) -> List[str]:
        pass
        # so what's the step?
        # write a fn that takes a string.
        # and an array, `chunksFound`
        
        # it should know how to check for a chunk
        self.validChunks = set(wordDict)
        # it should know how to save the result
        self.resArr = []
        
        self.exploreChunks(s, [])
        
        return self.resArr
        
        
    def exploreChunks(self, s, chunksFound):
        if s == "":
            self.saveChunks(chunksFound)
            return

        chunk = ""
        for idx, ch in enumerate(s):
            
            chunk += ch
        
            if chunk in self.validChunks:
                nextS = s[idx + 1:]
                chunksFound.append(chunk)
                self.exploreChunks(nextS, chunksFound)
                chunksFound.pop()
                
                
    def saveChunks(self, chunksFound):
        delim = " "
        chunksConcat = delim.join(chunksFound)
        
        self.resArr.append(chunksConcat)