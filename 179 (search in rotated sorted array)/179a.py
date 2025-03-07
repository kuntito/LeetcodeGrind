# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# TODO write O(log n) solution
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        pass
        # binary search problem
        # determine ths start index and end index
        # the start index is the first index where the previous index is greater than itself
        
        # initialize the startIdx to `0`
        # but if you find any other idx where `nums[idx-1] > nums[idx]`
        # update the startIdx to that index and break the loop
        
        # end index = startIdx + len(nums)
        # in your binary search, get the actual index by modding with len(nums)
        self.dim = len(nums)
        
        startIdx = self.get_start_idx(nums)
        endIdx = (startIdx + self.dim) - 1
        
        return self.binSearch(startIdx, endIdx, nums, target)
        
        
    def get_start_idx(self, nums):
        pass
        startIdx = 0
        for idx in range(1, self.dim):
            if nums[idx - 1] > nums[idx]:
                return idx
            
        return startIdx
    
    def binSearch(self, left, right, nums, target):
        pass
        while left <= right:
            mid = (left + right) // 2
            
            actualIdx = mid % self.dim
            midVal = nums[actualIdx]
            if midVal == target:
                return True
            elif target > midVal:
                left = mid + 1
            else:
                right = mid - 1
            
            
        return False
    
    
arr = [
    [[2,5,6,0,0,1,2], 0],
    [[2,5,6,0,0,1,2], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.search(foo, bar)
print(res)