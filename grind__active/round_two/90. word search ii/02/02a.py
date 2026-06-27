from typing import List


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:
        pass
    
        charWordsMap = self.getCharWordsMap(words)
        for ri, row in enumerate(board):
            for ci, ch in enumerate(row):
                if ch in charWordsMap:
                    self.exploreMatchingWords(
                        ch,
                        charWordsMap[ch]
                    )
                    
                    
    def exploreMatchingWords(self, ch, matchingWords):
        # what are we doing here?
        # every word in `matchingWords` begins with ch.
        # so...
        # TODO, probably needs a rewrite logic.
        # once, you have a char and matching word..
        # what do you want to do next?
                
                
    def getCharWordsMap(self, words):
        charWordsMap = {}
        
        for w in words:
            ch = w[0]
            
            if ch not in charWordsMap:
                charWordsMap[ch] = []
                
            charWordsMap[ch].append(w)
            
        return charWordsMap