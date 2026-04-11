# https://leetcode.com/problems/candy/description/

from typing import List

# what we doing in this joint?
# i'm given an array of integers, `ratings`

# each integer represents the rating of a child

# the children are lined up in a queue
# and i'm to give the kids candy.

# each child must have at least one candy
# and children with a higher rating get more candies than their neighbors

# what's the minimum number of candies i would need
# to make this distribution happen..

# every kid has one candy. okay.

# how do i deal with the ratings.
# if a child has a higher rating than their neighbor
# they should have more candy.

# in that sense, i need to know what the neighbor has to know what the child has
# so for each child, their number of candys would 1 if their neighbors have same or higher ratings
# however, if the child's rating is higher than either neighbor

# if the child's rating is higher..

# nah, for each child..
# i'm asking, is this child rated higher than their left neighbor
# if yes, set child = leftNeighbor rating + 1

# i think it's easier to first filter by range
# are the neighbor ratings less than the child's rating

# if yes, which of the neighbor ratings is higher
# once we have that, we can set the childs rating to be 
# `highestNeighborLowerThanMe + 1`

# period.

# it's giving recursion, you can start at anywhere.
# you'd explore left, explore right

# what does each recursive call return
# it's rating.

# this way, you can solve it..
# every one keeps checking left and right until out of bounds
# or no rating is lower

# error, no need for cache, `candyGiven` is the `cache`
# it tells you what children have been given candies.

# error, the question is not that simple..
# say i start at the first cell, idx = 0

# i go right, now i'm at idx = 1
# at this point, i want to go left and go right..
# but left is where i'm coming from..

# left needs me to know what to do..
# creating the infinite recursion i seen..

# what would be the better way to approach this
# it would be to explore the children in order of lowest ratings..

# the lowest ones don't care about they neighbors
# so, we simply assign them 1s

# now we go to the higher rated ones, at this point, we're guaranteed
# to have visited the lower rated ones..

# we then check for the ratings of the left and right neighbors
# if any of the neighbors are rated lower, we'd have seen them
# and so.. we can determine the number of candies to give the current child.

# right and how would this rating map go..
# create a mapping of index to rating...

# TODO continue this..

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyGiven = [0 for _ in ratings]
        
        self.explore(0, ratings, candyGiven)
        
        return sum(candyGiven)
        
    def explore(self, curIdx, ratings, candyGiven):
        dim = len(ratings)
        if curIdx < 0 or curIdx == dim:
            return 0
        
        if candyGiven[curIdx] != 0:
            return candyGiven[curIdx]
        
        leftRating = self.explore(curIdx - 1, ratings, candyGiven)
        rightRating = self.explore(curIdx + 1, ratings, candyGiven)

        childRating = ratings[curIdx]
        leftRating = None if leftRating > childRating else leftRating
        rightRating = None if rightRating > childRating else rightRating
        
        # what do i want to do here..
        # i have the left rating, i have the right rating..
        
        # i want to first verify which one of them are lower than the current rating
        # you've done that with the None assignment..
        
        bestRatingHere = 0
        # what next, i want to know..
        # if left is valid, best rating here, would be number of candyGiven at left
        if leftRating:
            bestRatingHere = candyGiven[curIdx-1]
        # if right is valid and right candyGiven is higher than best rating here
        # take right, reassign best rating
        if rightRating:
            bestRatingHere = max(
                candyGiven[curIdx + 1],
                bestRatingHere
            )
        
        # add 1 to best rating case closed.
        # you probably want to cache the results too
        candyGiven[curIdx] = bestRatingHere + 1
        
        return candyGiven[curIdx]


arr = [
    [1, 0, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)