from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        dim = len(words)
        count = 0
        
        for firstPos in range(dim):
            for secondPos in range(firstPos + 1, dim):
                firstPosStr = words[firstPos]
                secondPosStr = words[secondPos]
                
                if self.isPrefixAndSuffix(firstPosStr, secondPosStr):
                    count += 1
                    
        return count
    
    def isPrefixAndSuffix(self, uno: str, dos: str):
        return dos.startswith(uno) and dos.endswith(uno)