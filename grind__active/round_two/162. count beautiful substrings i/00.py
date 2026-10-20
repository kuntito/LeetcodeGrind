class Solution:
    def beautifulSubstrings(
        self,
        s: str,
        k: int
    ) -> int:
        self.dim = len(s)
        self.string = s
        self.k = k
        
        res = 0
        memo = {}
        arr = []
        
        for idx, ch in enumerate(s):
            res += self.explore(
                idx,
                0,
                0,
                memo,
                arr
            )

        return res
        
        
    def explore(self, curIdx, vowelCount, consonantCount, memo, arr):
        if self.is_out_of_bounds(curIdx):
            return 0
        
        if curIdx in memo:
            return memo[curIdx]
        
        ch = self.string[curIdx]
        arr.append(ch)
        if self.is_vowel(ch):
            vowelCount += 1
        else:
            consonantCount += 1
            
        isValid = self.is_valid(
            vowelCount,
            consonantCount
        )
        
        res = isValid + self.explore(
            curIdx + 1,
            vowelCount,
            consonantCount,
            memo,
            arr,
        )
        
        arr.pop()
        
        memo[curIdx] = res
        return memo[curIdx]
    
    def is_valid(self, vCount, cCount):
        isSame = vCount == cCount
        isMultiple = (vCount * cCount) % self.k == 0
        
        return 1 if isSame and isMultiple else 0
        
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