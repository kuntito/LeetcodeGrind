from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.dim = len(nums)

        return self.exploreSplits(0, k)

    def exploreSplits(
        self,
        startIdx,
        splitsLeft
    ):
        # if start index is out of bounds
        # regarding splits left, there's two scenarios:
        # 'no splits left' and 'some splits left'
        # if no splits, return `0`
        # if some splits, return `float("inf")`
        # why? not yet sure, it depends on what the fn is actually doing
        if startIdx == self.dim:
            return 0 if splitsLeft == 0 else float("inf")

        # here, he's doing something different.
        # if no splits left, return `float("inf")`
        # how's this different from the earlier situation
        # here, we aren't at the last index but ran out of splits
        # and so, `float("inf")`
        # seems to me float infinity is used when we need a split but ran out of numbers 
        if splitsLeft == 0:
            return float("inf")

        # we start off out result as float infinity
        res = float("inf")
        
        # then define a current sum, not sure what this represents.
        curSum = 0
        
        # we determine the maxChunkSize, what is this?
        # the most numbers a sub array chunk can contain
        # and how's it work?
        # here, you take out the number of splits from the total count of numbers
        # and then add `1`
        
        # what's it doing? in essence, when you take the number of splits out of total number
        # you're saying, if every split was of size `1`, i'd be left with ..
        # i can go on, but it's not intuitive
        # even though it's correct.
        
        # `maxChunkSize = self.dim - splitsLeft + 1`
        # the framing that works here is, with each recursive function
        # we're exploring every size the current split can be.
        # at minimum, it can be `1`
        # at maximum??
        # that's where the calculation comes in.
        # what's the biggest a split can get?
        # the biggest it can get would be if every other split was as small as possible.
        # if every other split was `1`, then we know the biggest this split can be
        # so deduct the sum of every other split being 1 from the total slots available.
        
        # total of every other split being `1`
        # this works because `splitsLeft` can represent every split being size `1`
        # so for every other split being `1`, we just deduct the split we care about
        everyOtherSplitTotal = splitsLeft - 1 
        
        # i'm renaming the variable too
        maxSplitSize = self.dim - everyOtherSplitTotal
        
        # now, we iterate from startIdx to maxSplitSize
        # but what is this doing?
        # we're going through every number within our max split window
        # and what for?
        # well, to explore the different sizes of the split
        # each index is the next size for the split
        # we start with `j == startIdx`, then address the number at j
        # when j progresses, or rather if since, there might only be one element.
        # say there's more, if j progresses, the next iteration would be considering two numbers
        # but we'd need a way to track the previous numbers
        # so we can get the sum of the current split.
        # one way, would be to the range, we know the starting point is `startIdx`
        # and we're currently at `j`, so...
        # fair, but Neet did it differently.
        
        # he summed up every value at j as he iterated through.
        # this way, we don't need to slice and sum..
        # we maintain the sum as we iterate.
        
        # a more efficient approach, i'd concede.
        for j in range(startIdx, maxSplitSize):
            curSum += self.nums[j]
            
            # now, that we have the sum of one possible split in this function
            # what to do?
            # i want to compare this sum with the biggest split sum down the line
            # and track the bigger one.
            
            # the compare that result with subsequent split paths.
            # what's a split path.
            # for every first, split, there might be more than one way to get a second split
            # and a third, and a fourth..
            # but there's only one being considered per time.
            # if you follow this till the end, this forms the split path
            # the exact split you chose at each point.
            
            # which is what this alog attempts to explore
            # each fn is exploring the different ways we can select the first split
            # we go from, however small the split can go, `1`
            # to however large it can go, `maxSplitSize`
            
            # at each point, we explore..
            # if the current split was size 1? 
            # what happens at the second split, and now we'd be back in a similar situation.
            # how many second splits can we have.. we'd explore every possibility..
            # the way, this'd pan out, is we'd pick the smallest of each split..
            # as we go along and eventually reach a point where we can split no more..
            # that'd be the path...
            # and along each path, i want to know the largest split sum.
            # and compare with the one i have here..
            # perhaps.. too much is going on in-between to intuitively understand what's going on.
            
            # it'd be best if i considered the case where each split only had one option
            # TODO.. carry on from here..
            res = min(
                res, 
                max(
                    curSum, 
                    self.exploreSplits(j + 1, splitsLeft - 1)
                )
            )

        return res
    

arr = [
    [[1,2], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)