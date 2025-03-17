# https://leetcode.com/problems/minimum-number-of-keypresses/description/

from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        pass
        # since there are 9 distinct keypads
        # the optimal way is to assign the first 9 distinct characters
        # of `s` to each keypad
        # and subsequently fill other keypad slots as we go along
        
        
        # use a hashmap, you want to determine how many key strokes it takes to get a character
        # keep a global count for all unique characters seen so far
        # for the first 9 characters, their key strokes would map to `1`
        
        # if the global count is greater than 9
        # each character strokes become 2
        # if the global count is greater than 18
        # strokes become 3
        
        # the general idea is correct, but for optimal performance
        # the mapping should be based on the frequency of the characters in the string
        
        # the most frequent characters should be the ones mapped first
        
        arr = list(s)
        counter = Counter(arr)
        
        arr.sort(key=lambda a: counter[a], reverse=True)
        
        charMap = self.getCharMap(arr)
        
        return sum(charMap[ch] for ch in arr)
        
        


    def getCharMap(self, chars):
        charMap = {}

        count = 0
        for ch in chars:
            if ch not in charMap:
                count += 1
                
                if count <= 9:
                    strokes = 1
                elif count <= 18:
                    strokes = 2
                else:
                    strokes = 3
                    
                charMap[ch] = strokes
        
        return charMap                
    

arr = [
    "apple",
    "abcdefghijkl",
    "aaaaaaaabcdefgggghijkllllllllllmmmnoppponono",
]
foo = arr[-1]
sol = Solution()
res = sol.minimumKeypresses(foo)
print(res)