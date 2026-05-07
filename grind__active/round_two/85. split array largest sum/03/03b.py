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
        # 1. 
        # also, removed the conditional here.
        # with the endRange logic, there would never be a time when
        # start index is out of bounds and splits remain.
        # start index can only travel as far as it can travel.
        # as far as it's valid. it never becomes invalid.
        if startIdx == self.dim:
            return 0

        if splitsLeft == 0:
            return float("inf")

        res = float("inf")
        
        curSum = 0
        
        everyOtherSplitTotal = splitsLeft - 1 
        
        # 0.
        # i renamed it to make it descriptive.
        # it's not `maxSplitSize`, it tells how far a split can grow
        # from `startIdx`
        
        # the idea is, you subtract every other split
        # from the array end range.
        # this way, whatever's left belongs to the current split
        endRange = self.dim - everyOtherSplitTotal
        
        for j in range(startIdx, endRange):
            curSum += self.nums[j]

            maxHereOnwards = max(
                curSum, 
                self.exploreSplits(
                    j + 1,
                    splitsLeft - 1
                )
            )

            # 2. i think, `res` might be smallest max at each point
            # but i'd leave that exploration for tomorrow.
            res = min(
                res,
                maxHereOnwards
            )

        return res
    

arr = [
    [[1,2], 2],
    [[1,2,3], 3],
    [[3,1,2], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)