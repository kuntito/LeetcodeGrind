# https://leetcode.com/problems/climbing-stairs/description/

# there's a staircase with `n` steps
# you're at the bottom, and want to reach the top, the nth step

# if you could only take `1` step or `2` steps per stride
# how many distinct ways can you reach the top?

# say, n=2
# let's explore both approaches
# we start at `step = 0`
# if we take one step,
#     now, we're at step one.. `s = 1`
#     at step one.. we can either take one step or two steps, but in reality
#     since there's only one step left, our only option is taking that step

#     hence, we take another one step..
#         now, we're at `s = 2`
#         we're done here..
#         let's double back
# we've taken one step, seen how it went, we took one step, could only take another, and we arrived at
# destination.

# now, how about two steps?
#     well, with two steps, 
#     we end up at `s = 2`

#     we're done here
#     so go back to the main function call..

# i say function call, because this pattern follows a similar structure
# to the XOR sum problem..

# it's a recursive problem because, with each step, we're faced with two options..
# take one step or take two steps..

# and you need to explore one path exhaustively before you explore the next..

# so how would you approach this..
# recursive function call
# you can either take one step or take two steps

# what arguments are we passing, let's do `n-1` and `n-2`
# so each function call knows how many steps left, naturally,
# base case is when `n <= 0`

# interesting push back here..

# say we in a recursive call, `n=1`
# as is the culture, we'd make two calls
# `n-1 = 0` and `n-2 = -1`

# and we'd reach the base case in both. do we want to treat them differently
# or the same? because in essence, if we have one step left, we can't take two steps..

# so the base cases should be different..
# or rather, two base cases..
# if `n == 0`, we've reached the end..
# if `n == -1`, we've overstepped...

# okay.. works.. and what happens at the base case
# how do we track the number of distinct steps..

# well, at `n == 0`, return `1`
# so the parent function would collate the number of steps for each recursive path
# and send it upward

# how about, `n == -1`, well, return `0`
# that's not a valid path..

# how about a larger example, `n=3`
# okay.. two paths
# one step, 3-1
#     n = 2
#     one step, 2-1
#         n = 1
#         one step, 1-1
#             n = 0, we stop, `path found`
#             we return `1`
#         two step, 1-2
#             n = -1, we stop, `path not found`
#             we return `0`
#         here, we collate scores, `1 + 0`
#         we return `1`
#     we're back here, we know the path for one step, returns `1`
#     now we explore two steps
#     two step, 2 - 2
#         n = 0, we stop, `path found`
#         we return `1`

#     now, we're back here
#     we know the right path returns `1` also
#     we collate, `1 + 1`
#     then return..
# now we're back here.. we know the path for one step returns `2`
# now, we explore two
# two step, 3-2
#     n = 1
#     one step, 1-1
#         n = 0, `path found`
#         we return `1`
#     back in parent, path for one step, returns `1`
#     now, two step..
#     two step = 1 - 2
#         n = -1, we stop, `path not found`
#         return `0`

#     back in parent, we collate, `1 + 0`
#     we return `1`
# we're back in main scope,
# the path one step, returned `2` after full exploration
# the path two step, returned `1` after full exploration
# so we collate, `2+1`, return the result..

# only thing, i'd add, since i already know, is avoiding repeated work..
# consider this, n = 5

# at the beginning, there's two paths, one step, two steps..
# but both paths would have some similarities at some point

# let's consider the one step, without considering it's recursive two step..
# we start with 5, take one out, 4, take another one out, 3..

# let's stop there and consider the two step..
# we start with 5, take two out, 3..

# now.. this shows us both paths would end up exploring `3`
# and since, it's recursion, we do the same thing at each step..

# therefore, we could add some optimization here.. we don't need to explore both `3`s
# since they'd end up in the same destination..

# we can store the result.. cache the result, so when next an exploration path
# hits a `3`, they know how it ends..

# the paths remain unique, because they took different routes to get to `3`
# but after `3`, they do the same thing..

# the technique is called memoization
# you use a hashmap to cache the results.. from earlier, we know when the step is `3`
# the result is `3`

# so the hash map, let's call it `memo[3] = 3`
# where would you put the hash map, pass it in every call
# and at the end of each call during collation, add the result to the hash map..

# also, at the start of each function, check if `n in memo`
# if yes, return `memo[n]`
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.explore(n, {})
        
    def explore(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n == -1:
            return 0
        
        pathOne = self.explore(
            n-1,
            memo
        )
        
        pathTwo = self.explore(
            n-2,
            memo
        )
        
        collate = pathOne + pathTwo
        memo[n] = collate
        
        return memo[n]