# is to explore every way you can split `nums` into `k` parts.
# and for each split, note the part with the largest sum.

# and of all the largest sums, you find, return the smallest one.

from typing import List

# TODO seems to work but is inefficient.. TLE...
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        pass
    
        # and how do i explore every split..
        # well, start with one split..
        
        # each part can have a max size..
        # reason being, the least size every other part can have is `1`
        
        # so if every other part has size 1,
        # the worst case, total size for every other part is `k-1`
        
        # the most elements the current part can have is
        # len(nums) - (k-1)
        # let's call this, `elemMaxCount`
        
        # so we experiment, we take one element
        # the figure out the size of the next part.
        
        # it lends itself to recursion..
        # and each recursive step, we run a loop
        # where we explore every size the current part can take..
        
        # we do this until we exhaust all the paths..
        # and we'd pass the sum of each path to the next recursive function.
        
        # this keeps going until we've explored all the parts in the current split.
        # at this point, we can update the global, `smallestLargestSum`
        # then go back..
        
        
        self.smallestLargest = float("inf")
        
        largestAlongSplit = 0
        self.explore(nums, k, largestAlongSplit)
        
        return self.smallestLargest
    
    def explore(self, nums, k, largestAlongSplit):
        if k == 1:
            return self.explore(
                [],
                0,
                max(
                    largestAlongSplit,
                    sum(nums)
                )
            )
            
        
        if k == 0:
            self.smallestLargest = min(
                self.smallestLargest,
                largestAlongSplit,
            )
            return
        
        maxCountCurPart = len(nums) - (k - 1)
        
        for idx in range(maxCountCurPart):
            partSum = sum(nums[:idx+1])
            
            self.explore(
                nums[idx + 1:],
                k-1,
                max(
                    largestAlongSplit,
                    partSum
                )
            )
            
arr = [
    [[1,4,4], 3],
    [[2,3,1,2,4,3], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)