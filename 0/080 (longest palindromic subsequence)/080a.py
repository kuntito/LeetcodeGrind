# https://leetcode.com/problems/longest-palindromic-subsequence/description/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        res = 0
        for idx in range(len(s)):
            lenOne = self.explore(idx, idx, s, memo)
            lenTwo = self.explore(idx, idx + 1, s, memo)

            larger = max(lenOne, lenTwo)

            res = max(
                res,
                larger
            )

        return res
    
    def explore(self, left, right, s, memo):
        cacheNode = (left, right)
        if cacheNode in memo:
            return memo[cacheNode]

        if left < 0 or right == len(s):
            memo[cacheNode] = 0
            return memo[cacheNode]
        
        count = 0
        if s[left] == s[right]:
            count = 1 if left == right else 2
            count += self.explore(left-1, right+1, s, memo)
        else:
            a = self.explore(left-1, right, s, memo)
            b = self.explore(left, right+1, s, memo)
            count += max(a, b)
        
        memo[cacheNode] = count
        return memo[cacheNode]



arr = [
    "abcdef",
    "cbbd",
    "bbbab",
]
foo = arr[-1]
sol = Solution()
res = sol.longestPalindromeSubseq(foo)
# print(res)