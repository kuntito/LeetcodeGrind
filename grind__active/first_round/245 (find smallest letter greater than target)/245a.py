# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for ch in letters:
            if ord(ch) > ord(target):
                return ch

        return letters[0]
    
print(ord('a'))