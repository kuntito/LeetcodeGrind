# https://leetcode.com/problems/merge-strings-alternately/description/

# TODO https://neetcode.io/solutions/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idxOne = 0
        idxTwo = 0

        res = []
        count = 0
        while idxOne < len(word1) and idxTwo < len(word2):
            if count % 2:
                res.append(word1[idxOne])
                idxOne += 1
            else:
                res.append(word2[idxTwo])
                idxTwo += 1
            count += 1

        
        while idxOne < len(word1):
            res.append(word1[idxOne])
            idxOne += 1

        while idxTwo < len(word2):
            res.append(word2[idxTwo])
            idxTwo += 1

        return ''.join(res)