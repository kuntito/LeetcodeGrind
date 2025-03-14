# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
    
        return self.explore(0, 0, {})
    
    def explore(self, idxOne, idxTwo, memo):
        foo = (idxOne, idxTwo)
        if foo in memo:
            return memo[foo]
        
        if idxOne == len(self.text1) or idxTwo == len(self.text2):
            return 0
        
        chOne = self.text1[idxOne]
        chTwo = self.text2[idxTwo]

        if chOne == chTwo:
            memo[foo] = 1 + self.explore(idxOne + 1, idxTwo + 1, memo)
            return memo[foo]

        res = max(
            self.explore(idxOne + 1, idxTwo, memo),
            self.explore(idxOne, idxTwo + 1, memo),
        )
        memo[foo] = res
        return memo[foo]
    

arr = [
    ["abc", "def"],
    ["abcde", "ace"],
    ["abc", "abc"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.longestCommonSubsequence(foo, bar)
print(res)