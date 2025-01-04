# https://leetcode.com/problems/interleaving-string/description/

# TODO https://neetcode.io/solutions/interleaving-string
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False

        # recursively use
        # two pointers, `idxOne` and `idxTwo`, for each word, `s1` and `s1` 
        # a third pointer, `idxThree` representing the `s3`

        # if the value at at `idxOne` or `idxTwo` word matches the value at `idxThree`
        # move the matching pointer forward and `idxThree` forward and explore another
        # recursive function
        # the base case is when `idxOne == len(s1)` and `idxTwo == len(s2)`
        # if during the recursive calls, neither pointer's value matches `idxThree`'s value
        # return False

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

        return self.explore(0, 0, 0, {})
    
    def explore(self, idxOne, idxTwo, idxThree, memo):
        foo = (idxOne, idxTwo, idxThree)
        if foo in memo:
            return memo[foo]
        

        dimOne = len(self.s1)
        dimTwo = len(self.s2)
        if idxOne == dimOne and idxTwo == dimTwo:
            return True
        
        chThree = self.s3[idxThree]
        if idxOne < dimOne:
            chOne = self.s1[idxOne]
            if chOne == chThree:
                res = self.explore(
                    idxOne + 1,
                    idxTwo,
                    idxThree + 1,
                    memo,
                )
                if res:
                    memo[foo] = res
                    return res
                
        if idxTwo < dimTwo:
            chTwo = self.s2[idxTwo]
            if chTwo == chThree:
                res = self.explore(
                    idxOne,
                    idxTwo + 1,
                    idxThree + 1,
                    memo,
                )
                memo[foo] = res
                return res
            
        memo[foo] = False
        return memo[foo]



arr = [
    ["a", "b", "a"],
    ["", "", ""],
    ["aabcc", "dbbca", "aadbbbaccc"],
    ["aabcc", "dbbca", "aadbbcbcac"],
]
foo, bar, sir = arr[-1]
sol = Solution()
res = sol.isInterleave(foo, bar, sir)
print(res)