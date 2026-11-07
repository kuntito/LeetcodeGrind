class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        substrs = self.splitAndJoin(s1)
        return s2 in substrs
    
    
    def splitAndJoin(self, chars):
        # now you can split the string at anywhere
        # so, i'd explore every split.
        dim = len(chars)
        if dim == 1:
            return {chars}
        
        res = set()
        for spliceIdx in range(1, dim):
            firstPart = chars[:spliceIdx]
            secondPart = chars[spliceIdx:]
            
            setOne = self.splitAndJoin(firstPart)
            setTwo = self.splitAndJoin(secondPart)
            
            for subOne in setOne:
                for subTwo in setTwo:
                    res.add(
                        subOne + subTwo
                    )
                    
                    res.add(
                        subTwo + subOne
                    )
        
        
        return res
        

arr = [
    ["great", "rgeat"],
    
]
foo, bar = arr[-1]
sol = Solution()

res = sol.isScramble(foo, bar)
print(res)