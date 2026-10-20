class Solution:
    def beautifulSubstrings(
        self,
        s: str,
        k: int
    ) -> int:
        self.dim = len(s)
        self.chars = s
        self.k = k
        
        arr = []
        res = 0
        for idx in range(self.dim):
            # the problem is here. i'm not sure memo is doing what i want it to.
            #  currently, i memoize the end of the string.
            #  perhaps, i should talk about what i should be doing
            #  now what i've done.
            
            # and what happens if i drop the memo?
            # it works, the memo was the problem, what really was the problem?
            # say you find a valid string at index 4.
            # you memoize and say, at index 4. a valid string.
            # but it matters because, you need to know where you were coming from.
            # at index 4, starting from zero, there was a valid string.
            # in which case, would you ever repeat substrings?
            # think about it?
            # is every path not unique.
            # you start with the first char, either stop or continue.
            # every new branch comes with the history of the former.
            
            # TODO you'd need to dive deep on where repeated work is done
            # and what the shape of the memo'd look like?
            res += self.explore(idx, 0, 0, arr)
            
        return res
    
    def explore(self, curIdx, vowelCount, consCount, arr):
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
            
        res += self.explore(curIdx + 1, vowelCount, consCount, arr)
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