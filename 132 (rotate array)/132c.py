# https://leetcode.com/problems/rotate-array/description/

# TODO https://neetcode.io/solutions/rotate-array
# 03:56
# TODO view 132c.py
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass
        # this stores all the indices that have been moved
        self.moved = set()
        self.steps = k
        
        # for each unmoved value,
        # determine the new_idx and move it
        for idx, n in enumerate(nums):
            if idx in self.moved: continue
            
            new_idx = self.get_new_idx(idx, nums)
            
            # declare this current position vacant
            nums[idx] = None
            
            # place `n` in it's new position
            self.place(n, new_idx, nums)
            
            
    def place(self, targ, idx, nums):
        if nums[idx] is not None:
            pass
            # determine the occupant
            occupant = nums[idx]
            # move it to where it belongs
            occupant_idx = self.get_new_idx(idx, nums)
            nums[idx] = None
            self.place(occupant, occupant_idx, nums)
        
        nums[idx] = targ
        self.moved.add(idx)
        
    
    def get_new_idx(self, currIdx, arr):
        return (currIdx + self.steps) % len(arr)
    
arr = [
    [[1,2,3,4], 3],
    [[-1,-100,3,99], 2],
    [[1,2,3,4,5,6,7], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.rotate(foo, bar)
print(foo)