# https://leetcode.com/problems/rotate-array/description/

# TODO, the problem is when k=2 and len(nums) == 4
# the function only rotates the last element
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass
        if k == 0 or len(nums) == 1:
            return
        
        dim = len(nums)
        
        originIdx = dim - 1
        new_idx = self.get_new_idx(originIdx, nums, k)
        
        origin = nums[originIdx]
        nums[originIdx] = None
        self.place(origin, new_idx, nums, k)
        
    def place(self, value, idx, arr, steps):
        pass
        currentOccupant = arr[idx]
        if currentOccupant is not None:
            pass
            arr[idx] = None
            # move current occupant
            new_idx = self.get_new_idx(idx, arr, steps)
            self.place(currentOccupant, new_idx, arr, steps)
        
        arr[idx] = value
    
    
    def get_new_idx(self, currIdx, arr, steps):
        return (currIdx + steps) % len(arr)
    
arr = [
    [[-1,-100,3,99], 2],
    [[1,2,3,4,5,6,7], 3],
    [[1,2,3,4], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.rotate(foo, bar)
print(foo)