# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx, count = len(s) - 1, 0
        space = ' '

        while s[idx] == space:
            idx -= 1

        while idx > -1 and s[idx] != space:
            count += 1
            idx -= 1
        
        return count