from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        
        cache = [
            [float("inf")] * (k + 1)
            for _ in range(numsLen)
        ]

        for splitsLeft in range(1, k + 1):
            self.populateCache(
                nums,
                splitsLeft,
                cache
            )

        return cache[0][k]

    
    def populateCache(self, nums, splitsLeft, cache):
        numsLen = len(nums)
        
        # here i go through every number in reverse?
        # it would seem so, since you're iterating through `nums` indices.
        for idx in range(numsLen - 1, -1, -1):
            curSum = 0
            
            # i determine, how far i can travel from the current index
            endRange = numsLen - (splitsLeft - 1)
            for numIdx in range(idx, endRange):
                # i begin travel, tracking the sum i've travelled so far
                curSum += nums[numIdx]
                
                # now, i check the cache
                # but what am i checking for?
                # for the context of the question, i imagine,
                # it's the..
                # let's rewrite,
                # after the current split, there exists several split paths
                # one can take to obtain all splits.
                # of all those paths, one of them'd have the smallest max split
                # it's assumed at this point in exploration, we'd have explored all those paths
                # determined the smallest max split and then cached it.
                # so the cache check is asking?
                # of all the paths that continue from here..
                # what was the smallest max split sum along any path
                # and that's what the cache is doing.
                
                # but why the indices, `numIdx + 1` and `splitsLeft - 1`
                # `numIdx` refers to the current index, this is where the current split sum ends
                # and so, whatever split happens next, must have done so starting at the next index
                # hence, `numIdx + 1`
                # next up, is `splitsLeft - 1`, what is this one?
                # i'd say this is, the number of splits left.
                
                # subtracting `1` is subtracting the current split from the total splits left to make
                # so the cache exists for this.
                
                # starting at this index, with these number of splits left
                # what's the smallest max split sum, you could find.
                
                # the reason, it's a downward left movement is
                
                # the number of splits left move left to right
                # the indices of each number move top to down
                
                # each number's index matches the row index
                # and there's a final row index that doesn't match any number index
                # this row, solves the index out of bounds problem, 
                # when we're at the last split and check for the next row, less split.
                # the cache doesn't throw out of bounds, because there's space for this.
                # however, i do think, this can be handled without this.
                
                # if numIdx goes out of bounds, no more splits.
                # and what should i return? zero.
                
                # what about when splitsLeft - 1 == 0?
                # well, i don't think i need a base case for this two..
                # since the cache check needs two variables, `numIdx` and `splitsLeft`
                
                # unless there's a scenario, where `numIdx + 1` is in bounds
                # and splitsLeft is zero.
                
                # it would have to be when splits left is `1`
                # splits left is `1` on every row.
                
                # i can justify removing the bottom row.
                # not the first column.
                
                # perhaps, it too can be removed, if i deep this enough.
                # let's remove the bottom row then see if the left column can be removed too.
                
                # the algorithm works.. after being removed.
                # removing the first column is not as simple, is it not?
                # well, it's being used to calculate the end range
                # and the convenience of using the 1-based indexing to represent the number of splits left.
                
                if numIdx + 1 == numsLen:
                    smallestMaxSumAlongRemainingPaths = 0
                else:
                    smallestMaxSumAlongRemainingPaths = cache[numIdx + 1][splitsLeft - 1]
                
                maxB = max(
                    curSum, 
                    smallestMaxSumAlongRemainingPaths
                )
                
                cache[idx][splitsLeft] = min(
                    cache[idx][splitsLeft],
                    maxB
                )
    
arr = [
    [[1,2,3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)