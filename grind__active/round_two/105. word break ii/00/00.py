# https://leetcode.com/problems/word-break-ii/description/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.resultArr = []
        self.trackingArr = []
        
        setOfWords = set(wordDict)
        
        self.explore(s, setOfWords)
        
        return self.resultArr
    
    def explore(self, s, setOfWords):
        if s == "":
            self.resultArr.append(
                " ".join(self.trackingArr)
            )
            return
        
        for idx, _ in enumerate(s):
            substr = s[:idx + 1]
            
            if substr in setOfWords:
                self.trackingArr.append(substr)
                self.explore(s[idx + 1:], setOfWords)
                self.trackingArr.pop()