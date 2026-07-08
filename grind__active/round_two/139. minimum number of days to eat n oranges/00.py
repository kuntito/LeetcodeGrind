class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        
        # TODO it gets a TLE,
        # but the pressing question is why am i deducting `1`
        return self.explore(n, memo) - 1
    
    def explore(self, n, memo):
        pass
        # and how would this go?
        # recursion, one function that encapsulates
        # the decisions
        # iterate through each decision
        # but what each one, see what happens next before iterating.
        # so, backtracking.
        # what's the recursive fn take, `days`?
        # well, the recursion depth, tells the story.
        # fair.
        # return one on arrival.
        # to be fair, i don't even need to explore the `one orange` path
        # that's obvious, it'd take however many oranges of days
        # to finish that.
        # so, it's really one decision.
        # well, yes, but that's one way of the numerous ways you can pick one orange
        # what do you mean?
        # you've described the path where you successively pick ones.
        # but what you've ignored is when you can pick one
        # then pick half
        # after every one you pick, you have three decisions again
        # after every half or two thirds, you can pick one.
        # you have three decisions not two.
        # act accordingly.
        if n == 0:
            return 1
        if n in memo:
            return memo[n]
        
        days = float("inf")
        
        # eat one
        resOne = self.explore(n-1, memo)
        days = min(
            days,
            resOne
        )
        
        # if even, eat half
        if n % 2 == 0:
            resHalf = self.explore(n/2, memo)
            days = min(
                days,
                resHalf
            )
            
        # if can split three equal ways, eat two thirds.
        if n % 3 == 0:
            resThirds = self.explore(n/3, memo)
            days = min(
                days,
                resThirds
            )
        
        memo[n] = days + 1
        return memo[n]
    
    
arr = [
    3,
    10,
    6,
]
foo = arr[-1]
sol = Solution()
res = sol.minDays(foo)
print(res)
    
    