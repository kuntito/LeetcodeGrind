# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # this was written after the code below
        # since all the numbers are in the range `1, n`
        # each number can be representd by the index of `nums`
        
        # the idea is to recursively place each number in it's appropriate index
        # and set vacant indexes to `None`
        
        # then iterate through the array
        # and note the empty slots and the numbers that belong there

        dim = len(nums)
        
        for idx in range(dim):
            n = nums[idx]
            # the number's actual index
            num_idx = n - 1

            # make the index vacant
            nums[idx] = None
            # place the number where it should be
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
            nums[target_idx] = None
            
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
