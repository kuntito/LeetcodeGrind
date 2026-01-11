# https://leetcode.com/problems/integer-break/description/

# https://neetcode.io/solutions/integer-break
# TODO 11:35, view dp solution
class Solution:
    def integerBreak(self, n: int) -> int:
        pass
        # it's a dynamic programming problem
        # the idea is to consider all possible integer breaks
        # and memoize the results
        
        # for instance, `4` can be broken down into `1, 3` and `2, 2`
        
        # the way to consider the breaks is a for loop that runs from
        # `1` up until half of num inclusive i.e. `range(1, num//2 + 1)`
        # reason for the using halfway is to avoid redundant checks
        # i.e. the halfway point for `4` is `2`
        # if we pass that, we'd have to explore `1, 3` and `3, 1`
        
        # then explore each break on a separate recursive function
        # then track the breaks with the highest products
        self.root = n
        return self.explore(n, {})
    
    def explore(self, num, memo):
        if num in memo:
            return memo[num]
        
        if num == 1:
            return 1

        memo[num] = 0 if num == self.root else num

        endRange = num // 2 + 1        
        for leftBreak in range(1, endRange):
            
            rightBreak = num - leftBreak
            
            leftRes = self.explore(leftBreak, memo)
            rightRes = self.explore(rightBreak, memo)
            
            memo[num] = max(
                memo[num],
                leftRes * rightRes
            )
            
        return memo[num]
    
arr = [
    2,
    10,
]
foo = arr[-1]
sol = Solution()
res = sol.integerBreak(foo)
print(res)
    

    
