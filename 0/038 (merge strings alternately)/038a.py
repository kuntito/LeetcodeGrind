# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idxOne = 0
        idxTwo = 0

        res = []
        while idxOne < len(word1) and idxTwo < len(word2):
            res.append(word1[idxOne])
            res.append(word2[idxTwo])
            idxOne += 1
            idxTwo += 1

        
        while idxOne < len(word1):
            res.append(word1[idxOne])
            idxOne += 1

        while idxTwo < len(word2):
            res.append(word2[idxTwo])
            idxTwo += 1

        return ''.join(res)