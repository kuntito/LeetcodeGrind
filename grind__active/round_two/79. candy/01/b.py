# https://leetcode.com/problems/candy/
from typing import List

# right, what we doing today?

# i'm given an array of integers called `ratings`

# every element of this array, represents the rating of a child.

# okay..
# and i want to give these children candy.

# there's three rules

# every child must have at least one candy.
# every child must have more candy than it's left neighbor if that child has a higher rating than it's left neighbor
# every child must have more candy than it's right neighbor if that child has a higer rating than it's right neighbor.

# what's the minimum amount of candy i need to ensure these rules are met?

# i'd say sort the children by rating
# give them all one candy.

# run through each child in the sorted ratings.
# and ask..
# does this child have a higher rating than it's left neighbor?
# if yes, does the child's candy count exceed it's left neighbor?
#   if yes, let it be.
#   if no, set the child's candy count to `leftNeighbourCandyCount + 1`
# if no, leave the child's candy count as is.

# then ask..
# does this child have a higher rating than it's right neighbor?
# if yes, does the child's candy count exceed it's right neighbor?
#   if yes, let it be
#   if no, set the child's candy count to `rightNeighborCandyCount + 1`
# if no, leave the child's candy count as is.

# this looks like it'd work off the dome.
# but why am i sorting by rating in the first place?

# rating determines who gets more candy.
# well rating and who's next to who?

# yes, but why do we need to sort?

# consider:
# [1, 3, 2, 1]

# if i ran the algorithm without sorting on this..
# i'd give the first child the customary one candy.

# the first child has no left neighbor and has a less rating to it's right neighbor
# so it stays as one candy.

# the candy given array would be [1, _, _, _]
# now, the second child..`3`

# this gets the customary one candy
# to it's left, it has a neighbor with a lesser rating..
# and it's candy count doesn't exceed it's left neighbors candy count.
# hence, it becomes `leftNeighborCandyCount + 1`

# obtaining two candies.
# we do the same check for the right neighbor
# and yes, the second child has a higher rating than it's right neighbor.
# but it's candy count is already greater than it's right neighbors,
# which in this case is `0`

# but the problem here becomes apparent.
# because we haven't gotten to the right neighbor, the third child,
# so we don't know how many candies they'd get.

# hence, why sorting by the ratings is necessary.
# the lesser rated children should be addressed first.

# that way, the bigger ratings are ensured to have their lesser neighbors assigned candies by the time we get to them.

# when done, sort back by index
# and return the result.

# how would the code work?
# two things..
# an array of tuples, (idx, rating)
# an array of candy results.

# you iterate through this sorted array
# for each element, you check it's left neighbor
# from the original array, `ratings`

# perform the algo, then store the candy cound in `candyResults[idx]`
# return the sum of candy results.

# error, i didn't sort the array by ratings..
# i merely added the tuple of (idx, ratings)
# perhaps, i was too excited to get to the solution.

# TODO this works.. but perhaps there's a simpler way.
# and more readable way.

# use a set to store the indices you've addressed.
# the problem we ran into earlier was we were at the second child
# and wanted to know the candy assigned to the the right neighbor, the third child
# but at this point we don't know what the third child is.
# so it makes sense to explore the third child right there.

# and we'd be back where we started.
# third child checks the left, see it's higher rating.
# so it only checks it right..

# there's nothing there, so it assigns itself one candy.
# i can use the array candy count for this.
# and it can also serve as the cache to know if to explore a particular index or not.

# it's sounding like a recursive step..
# it is.. iterate through ratings..
# on each iteration start a function call..

# pass curIdx, ratings, candyCount


class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        sortedRatings = sorted(
            [
                (idx, rat) for idx, rat in enumerate(ratings)
            ],
            key=lambda x: x[1]
        )
        candyCount = [0 for _ in ratings]
        
        for idx, rat in sortedRatings:
            leftNeighborRat = ratings[idx - 1] if idx - 1 >= 0 else None
            rightNeighborRat = ratings[idx + 1] if idx + 1 < len(ratings) else None
            
            curCandy = 1
            if leftNeighborRat is not None and\
                rat > leftNeighborRat and\
                curCandy <= candyCount[idx - 1]:
                    curCandy = candyCount[idx - 1] + 1
                    
            if rightNeighborRat is not None and\
                rat > rightNeighborRat and\
                curCandy <= candyCount[idx + 1]:
                    curCandy = candyCount[idx + 1] + 1
                    
            candyCount[idx] = curCandy
            
        return sum(candyCount)
    
arr = [
    [1, 0, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)
            
            