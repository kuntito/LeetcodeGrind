from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        
        for string in words:
            prefix = ""
            number = 0
            for ch in string:
                prefix += ch
                
                number += self.howManyStarts(prefix, words)
                
            res.append(number)
            
        return res
    
    
    def howManyStarts(self, prefix, words: list[str]):
        count = 0
        for wd in words:
            if wd.startswith(prefix):
                count += 1
                
        return count
        