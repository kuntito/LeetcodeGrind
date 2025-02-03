# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass
        count = sum(1 for ch in s[:k] if self.is_vowel(ch))
        maxCount = count

        dim = len(s)
        for idx in range(k, dim):
            pass
            prevCh = s[idx - k]
            currCh = s[idx]
            
            if self.is_vowel(prevCh):
                count -= 1
            
            if self.is_vowel(currCh):
                count += 1
                maxCount = max(count, maxCount)
                
        return maxCount
            
        
    def is_vowel(self, ch):
        return ch in 'aeiou'
    
arr = [
    ["abciiidef", 3],
    ["aeiou", 2],
    ["leetcode", 3],
    ["a", 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maxVowels(foo, bar)
print(res)