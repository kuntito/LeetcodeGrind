# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List


# i have a bag of marbles, the weights of each marble is represented with an integer array
# `weights`

# i have `k` bags and want to distribute all the marbles such that every bag contains
# at least one marble

# and any bag with multiple marbles must have marbles with consecutive indices
# i.e. (weights[i], weights[i+1], weights[i+2])

# after distribution, i want to determine the score of each bag
# to do this we need to two things, the weight at the smallest index in the bag
# and the weight at the largest index in the bag

# since each bag maintains the consecutive order of indices
# score = bag[0] + bag[-1]

# the marble distributed can occur in multiple ways
# of all the ways, one would yield the lowest total Score
# and one would yie;d the highest total score

# find these scores, lowestTotalScore and highestTotalScore
# and return `highestTotalScore - lowestTotalScore`

# bruteforce, explore every distribution
# track the lowestTotal and highestTotal


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pass
        # we're guaranteed `k` is at least the length of `weights`
        # if we have as many bags as marbles, the highest total is the lowest total
        # and the difference would be zero
        if k == len(weights):
            return 0

        # if we have more marbles than bags
        # we'd experiment by putting one marble in each bag
        # the put another marble in the second bag and repeat
        # till we hit the last bag and dump the remaining marbles

        # since, we'd have exhausted the marbles, we track highest and lowest
        # then what?

        # we return to the previous recursive calls and use put two marbles in the bag
        # instead of one and continue

        # the base case would be we've exhausted the marbles and bags

        # how would you implement putting marbles in a bag?
        # we're placing marbles incrementally

        # first, we place one then explore onwards
        # then, we place two and explore...

        # we would need two indices
        # `start` and `end`

        # first, `start == end`
        # then, we increment `end += 1`

        # for each exploration
        # `explore(start, end, bagIdx, score)`

        # how then do you calculate the score at the end
        # we can keep an array of intervals?
        # or keep track of the score as we go along

        self.lowestScore = float("inf")
        self.highestScore = float("-inf")

        self.weights = weights
        self.maxBags = k

        self.explore(0, 0, 0, 0, set())

        return self.highestScore - self.lowestScore

    def explore(self, start: int, end: int, bagIdx: int, score: int, memo):
        mitem = (start, end, bagIdx, score)
        if mitem in memo:
            return
        memo.add(mitem)
        
        isRunOutMarble = end == len(self.weights)
        isRunOutBags = bagIdx == self.maxBags

        if isRunOutMarble and isRunOutBags:
            self.lowestScore = min(score, self.lowestScore)
            self.highestScore = max(score, self.highestScore)

            return

        # reaching this point means we have marbles but no bags
        # or bags with no marbles
        # either way, we can't proceed
        if isRunOutMarble or isRunOutBags:
            return


        self.explore(
            start,
            end + 1,
            bagIdx,
            score,
            memo
        )
        self.explore(
            end + 1,
            end + 1,
            bagIdx + 1,
            score + self.weights[start] + self.weights[end],
            memo
        )


arr = [
    [[1, 3, 5, 1], 2],
    [[1, 3], 2],
    [[46,37,46,17,40,50,54,11,1,25,43,21,31,29,58,49,73,54,5,52,73,54,6,22,58,9,34,21,58,68,63], 30],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.putMarbles(foo, bar)
print(res)
