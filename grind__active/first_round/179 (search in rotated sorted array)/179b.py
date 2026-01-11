# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        pass

        # use binary search to find the start index
        # the `startIndex` is where the value at `startIndex - 1`
        # is greater than the value at `startIndex`
        
        # if the previous value is less
        # shift the midpoint right
    
arr = [
    [[2,5,6,0,0,1,2], 0],
    [[2,5,6,0,0,1,2], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.search(foo, bar)
print(res)