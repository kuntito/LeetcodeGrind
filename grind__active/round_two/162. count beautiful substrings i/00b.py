class Solution:
    def beautifulSubstrings(
        self,
        s: str,
        k: int
    ) -> int:
        self.dim = len(s)
        self.chars = s
        self.k = k
        
        memo, arr = {}, []
        res = 0
        for idx in range(self.dim):
            # TODO the problem is here. i'm not sure memo is doing what i want it to.
            #  currently, i memoize the end of the string.
            #  perhaps, i should talk about what i should be doing
            #  now what i've done.
            
            # and what happens if i drop the memo?
            res += self.explore(idx, 0, 0, memo, arr)
            
        return res
    
    def explore(self, curIdx, vowelCount, consCount, memo, arr):
        if curIdx in memo:
            return memo[curIdx]
        
        if self.is_out_of_bounds(curIdx):
            return 0
        
        ch = self.chars[curIdx]
        arr.append(ch)
        
        if self.is_vowel(ch):
            vowelCount += 1
        else:
            consCount += 1
            
        res = 0
        isValid = self.get_is_valid(vowelCount, consCount)
        if isValid:
            res += 1
            
        res += self.explore(curIdx + 1, vowelCount, consCount, memo, arr)
        
        memo[curIdx] = res
        return res
    
    def get_is_valid(self, v, c):
        isSame = v == c
        isMultiple = (v * c) % self.k == 0
        
        return isSame and isMultiple
        
    def is_vowel(self, ch):
        return ch in "aeiou"
        
        
    def is_out_of_bounds(self, idx):
        return idx >= self.dim
    
arr = [
    ["baeyh", 2],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.beautifulSubstrings(foo, bar)
print(res)