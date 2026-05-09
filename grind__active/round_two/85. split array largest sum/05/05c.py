from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # so what do i want to do?
        # i want explore every variation of a split,
        # once, i pick one variant,
        # i'd start another call
        # looking for every variation of the next split
        # and so on..
        # i'd keep going till i've gotten a path.
        # i'd have picked one split variant on each recursive path
        # when i reach the end, what do i want to do?

        # at the end, i'd simply return the sum of that variant.
        # since, it's the last split, there's only one variant.
        # and that's both the largest split and the smallest 

        # then i go to it's parent call.
        # at this point, i'd compare the sum of the parent's split variant
        # with what i just returned.

        # the question of this is, which of these split sums is greater.
        # both represent a path at whatever `startIdx` is at that point.
        # and finding the greater one, is finding the max split at that start index

        # once you have it, you then store it as the smallest max you've found
        # then you explore the next variant at that point.
        # with the variant gotten, you explore the next split
        # and it's the same story.
        # base split returns, you compare it with the parent split sum,
        # which is bigger
        # whatever the result is, you then compare with the smallest max you've found

        # all said and done, you'd have had the smallest max at that `startIdx`
        # and that's what you return.

        # now the parent of that, receives it as what?
        # the smallest max sum after itself.
        # so what does it do?

        # before that, the idea is, the parent, can form several other paths
        # we've just explored those other paths and determined what the smallest max would be
        # and that's we only cared about
        # the only question now, is whether, 
        # the current parent split sum is greater than the smallest max after it
        # so again, we compare them to see which is bigger then..
        # store as the smallest max seen...

        # it's recursion all the way..
        self.totalSpace = len(nums)
        self.nums = nums

        startIdx = 0
        splitsLeft = k
        cache = {}
        return self.exploreSplits(startIdx, splitsLeft, cache)

    def exploreSplits(self, startIdx, splitsLeft, cache):
        if splitsLeft == 1:
            return sum(
                self.nums[startIdx:]
            )

        mitem = (startIdx, splitsLeft)

        if mitem in cache:
            return cache[mitem]

        # now, what do i want?
        # every variant of the split...
        # i want to know how many variants, i can get.
        # that'd be subtract the number of other splits left
        # from the total space available
        # whatever's left can belong to this split

        finalDest = self.totalSpace - (splitsLeft - 1)

        smallestMax = None
        curSplitSum = 0
        for idx in range(startIdx, finalDest):
            curSplitSum += self.nums[idx]

            maxAlongPath = max(
                curSplitSum,
                self.exploreSplits(
                    idx + 1,
                    splitsLeft - 1,
                    cache
                )
            )

            if smallestMax is None:
                smallestMax = maxAlongPath
            elif maxAlongPath < smallestMax:
                smallestMax = maxAlongPath

        cache[mitem] = smallestMax
        return cache[mitem]