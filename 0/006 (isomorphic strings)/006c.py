# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashOne = {}
        hashTwo = {}

        for chOne, chTwo in zip(s, t):
            a = chOne in hashOne and hashOne[chOne] != chTwo
            b = chTwo in hashTwo and hashTwo[chTwo] != chOne

            if a or b:
                return False
            
            hashOne[chOne] = chTwo
            hashTwo[chTwo] = chOne

        return True