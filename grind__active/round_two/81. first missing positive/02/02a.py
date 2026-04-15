from typing import List

# TODO it works but the explanation could be clearer.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx, number in enumerate(nums):
            # is the number in right place?
            is_num_in_right_place = idx + 1 == number
            
            if is_num_in_right_place: continue
            
            # create a gap here...
            nums[idx] = None
            
            # if number is negative or zero,
            # no need to move anything, simply leave the gap
            if number <= 0: continue
            
            rightfulIdx = number - 1
            if rightfulIdx >= len(nums): continue
            
            self.moveNumber(number, rightfulIdx, nums)
            
        for idx, number in enumerate(nums):
            if number is None:
                return idx + 1
            
        return nums[-1] + 1
    
            
    def moveNumber(self, number, rightfulIdx, nums):
        occupant = nums[rightfulIdx]
        
        if occupant is not None:
            # create gap
            nums[rightfulIdx] = None
            occupantRightfulIndex = occupant - 1
            
            if occupantRightfulIndex >= 0 and occupantRightfulIndex < len(nums):            
                self.moveNumber(occupant, occupantRightfulIndex, nums)
                
        
        nums[rightfulIdx] = number
        
arr = [
    [1],
    [1, 2, 0],
]
foo = arr[-1]
sol = Solution()
res = sol.firstMissingPositive(foo)
print(res)