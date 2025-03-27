# https://leetcode.com/problems/shortest-completing-word/description/

from collections import defaultdict
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        pass
        # get a counter for all alphabets in `licensePlate`
        counter = defaultdict(int)
        for ch in licensePlate:
            if not ch.isalpha(): continue
            
            ch = ch.lower()
            counter[ch] += 1
        
        # sort words by length
        words.sort(key=lambda x: len(x))
        
        # iterate through words and return the first word who's counter matches
        # `licensePlateCounter`
        for w in words:
            if self.isMatch(counter.copy(), w):
                return w
            
            
    def isMatch(self, licenseCounter, word):
        # iterate through all the characters in words
        # convert chars to lowercase
        # if a character is not present in licensePlate
        # continue, since we're only concerned with present characters
        
        # if it exists in licensePlate
        # decrement count by 1
        # if count becomes `0`, remove that char from licensePlate
        # if `word` is a match, `licenseCounter` should be empty

        for ch in word:
            ch = ch.lower()
            if ch not in licenseCounter:
                continue
            licenseCounter[ch] -= 1
            if licenseCounter[ch] == 0:
                del licenseCounter[ch]
        
        return not licenseCounter
    
arr = [
    ["1s3 PSt", ["step","steps","stripe","stepple"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shortestCompletingWord(foo, bar)
print(res)
    
