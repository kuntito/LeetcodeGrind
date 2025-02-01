# https://leetcode.com/problems/rotate-array/description/

# TODO, i think your intution is wrong
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass
        if k <= 1:
            return
        self.nums = nums
        self.k = k
        
        start = nums[-1]
        idx = len(nums) - 1
        
        nums[idx] = None
        right_spot = self.get_right_spot(idx)
        
        
        self.place(start, right_spot)
        
    def place(self, num, right_spot):
        occupant = self.nums[right_spot]
        if occupant and occupant != num:
            pass
            self.nums[right_spot] = None
            self.place(
                occupant,
                self.get_right_spot(right_spot)
            )
            
        self.nums[right_spot] = num
        
        
        
    def get_right_spot(self, idx):
        dim = len(self.nums)
        return (idx + self.k) % dim
    
arr = [
    [[-1,-100,3,99], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.rotate(foo, bar)
print(foo)