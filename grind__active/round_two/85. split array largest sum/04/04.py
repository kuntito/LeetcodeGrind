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
        if startIdx == self.dim:
            return 0

        # i no longer need this since, i simply sum up the final split
        # rather than iterate through.
        # if splitsLeft == 0:
        #     return float("inf")

        
        if splitsLeft == 1:
            finalSplitSum = sum(
                self.nums[startIdx:]
            )
            
            return finalSplitSum
        else:
            smallestMaxSplit = self.exploreSplitVariations(
                splitsLeft,
                startIdx
            )

        return smallestMaxSplit
    
    
    def exploreSplitVariations(self, splitsLeft, startIdx):
        smallestMaxSplit = float("inf")
        curSum = 0
        
        everyOtherSplitTotal = splitsLeft - 1 
        
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

            smallestMaxSplit = min(
                smallestMaxSplit,
                maxHereOnwards
            )
            
        return smallestMaxSplit
    

arr = [
    [[1,2], 2],
    [[1,2,3], 3],
    [[3,1,5], 2],
    [[7,2,5,10,8], 2]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)