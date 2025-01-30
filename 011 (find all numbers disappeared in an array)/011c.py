# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# TODO https://neetcode.io/solutions/find-all-numbers-disappeared-in-an-array
# TODO why's it not working?
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        dim = len(nums)
        
        for idx in range(dim):
            n = nums[idx]
            num_idx = n - 1
            
            if num_idx != idx:
                nums[idx] = None
                self.place(n, num_idx, nums)
                
        res = []
        for idx, n in enumerate(nums):
            if n is None:
                res.append(idx + 1)
        return res
            
                
    def place(self, n, target_idx, nums):
        occupant = nums[target_idx]
        if occupant and occupant != n:
            occupant_idx = occupant - 1
            
            # TODO ???
            nums[occupant_idx] = None
            
            self.place(occupant, occupant_idx, nums)
            
        nums[target_idx] = n
        
arr = [
    [3, 2, 1],
    [4,3,2,7,8,2,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findDisappearedNumbers(foo)
print(res)
