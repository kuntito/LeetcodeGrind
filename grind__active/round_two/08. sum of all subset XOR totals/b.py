# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/



# i'm given an array of numbers, `nums`
# i want to explore every subset of `nums`
# for each subset, calculate it's XOR total
# a XOR total is the result of XORing every element in a subset
# say the subset is [1, 2, 3], the XOR total is (1 ^ 2 ^ 3)
# in Python, XOR is represented by ^

# then we want to sum up all XOR totals
# and return that

# in essence, find the XOR totals for every subset in `nums`
# and return the total sum

# from experience, i know you can explore every subset
# using two path recursion

# sounds a bit fancy but simplified, it allows to explore every subset combination
# in essence, we'd be exploring every index, but with different comfigurations

# not sure, i'm doing a good job explaining here..
# but say you have [1, 2, 3]
# what would each subset look like, intuitively, you'd have an empty subset, a subset for each value, a subset for two values
# a subset for three values which is the entire thing..

# i.e. [], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]

# while i don't have the words to connect the above to the two path recursion
# i'd explain either way

# we would have a currIndex, initialized to 0
# for every recursive call, you increase currIndex by 1, i.e. currIndex + 1

# in each recursive call, we will do two things
# * start another recursive call
# * track the element at currIndex, then start another recursive call

# it's obvious, we'd need something to track these elements
# that's where an array comes in

# say, `recursiveCall(currIndex, trackingArr, nums)`
# say, `nums = [1, 2, 3]`

# in call 1, currIndex = 0, trackingArr = [], nums = [1, 2, 3]
# what do we do?

# one, do nothing, start another recursive call
#   recursiveCall(currIndex + 1, trackingArr, nums)
#   in essence, you'd have this.. recursiveCall(1, [], [1, 2, 3])

# two, track the element at currIndex, then start another recursive call
# i'd like to pause here, since we can't actually start this branch until
# we've fully explored the left branch

# writing out the code makes it easier to understand
# def recursiveCall(currIndex, trackingArr, nums):
#   // step one
#   recursiveCall(currIndex + 1, trackingArr, nums)

#   // step two, tracj elem at curr index then recurs..
#   trackingArr.append(nums[currIndex])
#   recursiveCall(currIndex + 1, trackingArr, nums)

# looking at this, once we start the first one..
# it would start another function call to `recursiveCall` with new arguments
# and it would keep doing this until, well..

# that's where the base case comes in..
# when does this recursion end..
# when we run out of current index

# in essence, at the top, i should add a check
# if currIndex == len(nums):
#   return

# it's only when we get here, we ever get to explore the next path of
# our two path recursion..

# let's reexplore this with a simpler example, nums = [1]
# the claim is our 2-path recursion would give me all the subsets in `nums`

# let's explore it..
# on the first call

# currIndex = 0, trackingArr = [], nums = [1]

# path one, recurs(1, [], [1])
#   we get into another recursive call, see that currIndex == len(nums)
#   we return, this way we stopped the recursion at trackingArr = []


# now, path two,
# recurs(1, [1], [1])
#   same thing, we see currIndex == len(nums)
#   we return here, where trackingArr = [1]

# if you pay attention, every time, we hit our base case, we hit a subset
# in our case, [] and [1] are the two subsets..

# let's take on a bigger example, [1, 2]
# from root, 0, [], [1, 2]
#   path one,
#       1, [], [1, 2]
#       path one's path one
#          2, [], [1, 2]
#          we stop here, since currIndex == len(nums), note..one subset is []

#       now, we're back in the parent function call, (path one), about to explore path 2
#       we add to tracking array, nums[currIndex] = nums[1] = 2

#       path one's path two
#          2, [2], [1, 2]
#          we stop here, since currIndex == len(nums), note..one subset is [2]

#       back in the parent function call (path one)
#       function ends, return to the next parent function call, (root)

#   now we're back in the root function call, about to explore path two
#   now, somethin interesting happens here..
#   from pathOne exploration, trackingArray = [2]
  
#   but the way the algorithm works is for every path two
#   every element you append you have to remove
#   this makes things a bit harder to understand since i'm simply stating it
#   but i know it works..

#   in essence, in `path one's path two`, after adding `2`, and exploring the recursive call
#   we'd remove this value before getting back to `root`, hence `trackingArr.pop`

#   this way, when we get back in root, trackingArr is the way we had it when we started
#   the path one exploration, []

#   and as is the custom, in path two's
#   append the element at the `curIndex`
#   at this point, root, `curIndex = 0`

#   trackingArr.append(nums[0]), trackingArr = [1]
#   and now, we explore path two

#   path two, (1, [1], [1, 2])
#         inside path two, we explore path two's path one
#         keep the tracking array as is, but increase curIndex

#         path two's path one
#         (2, [1], [1, 2])
#             inside here, we realize curIndex == len(nums), so we return, but also note we've found a subset, [1]

#         back in path two..
#         as is custom, append the element at currIndex
#         in this case, currIndex = 1, trackingArr.append(nums[1])
#         nums[1] = 2

#         trackingArr = [1, 2]

#         then we explore path two's path two
#         (2, [1, 2], [1, 2])
#             inside, we hit the base case, currIndex(2) == len(nums)
#             we return, but note we've found another subset [1, 2]

#         then we get back to path two..
#         as is the rule to clean up `trackingArr`
#         we pop.. trackingArr.pop()

#     and now we're back in root..
#     there's nothing more to do in root..

#     than to pop.. but we didn't even add anythin..
#     but that's the crux of recursion

#     you're doing the same thing in every function
#     and there would be some cases where your logic does nothing..
#     but it is what it is..

#     i'm impressed by whoever figured this out first..
#     it's a bit of mind bender

# okay, that's a lengthy explanation but how does it help me solve 
# XOR sum, well, instead of a tracking array, we'd have a tracking product..
# we'd be tracking the product across each subset path..

# a XOR b XOR c until we reach base case
# after which we'd unXOR c..

# we'd start with trackProd = 0
# for XOR, anything XOR'd with zero is the same thing..

# a XOR 0 = a
# in math, it's the same thing as `1`, anything multiplied by `1` is the same
# so `0` is good for a starting point

# how do we unXOR though, in math if i did, 2x3 to get 6, and wanted to get rid of 3
# i'd divide by 2

# same vein, if i did a XOR b to get c and wanted to get rid of c, what do i do?
# Claude says, XOR is it's own inverse

# hence, if i a XOR b to get c
# to remove `b`, i'd need to do `c XOR b` and i'd get back my a

# okay, this explains how to get the XOR's for every subset, how do we sum them..
# each recursive call would return it's own XOR prod, 
# we'd sum the left and right branches, return the total to the parent..
# we'd keep doing this till we hit the finish line...


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        prod = 0
        currIndex = 0
        
        return self.explore(currIndex, prod, nums)
    
    def explore(self, currIndex, prod, nums):
        if currIndex == len(nums):
            return prod
        
        leftProd = self.explore(
            currIndex + 1,
            prod,
            nums
        )
        
        prod ^= nums[currIndex]
        
        rightProd = self.explore(
            currIndex + 1,
            prod,
            nums
        )
        
        # this line is not needed, we don't need to unXOR since `prod` is not an array
        # hence, immutable, each recursive call maintains the same `prod` value as it started with
        
        # prod ^= nums[currIndex]
        
        return leftProd + rightProd
        
        
            
arr = [
    [1, 2],
    [1, 2, 3],
    [1, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.subsetXORSum(foo)
print(res)