# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        pass
    
        # run recursive algorithm to move elements to their appropriate index
        # if you're placing an element in a slot where it already exists then
        # it's a duplicate, append it to `self.res`
        
        self.res = []
        
        for idx, n in enumerate(nums):
            # if `n` is not in the right spot
            # place it in the right spot
            right_spot = n-1
            
            if right_spot != idx:
                pass
                # since we're moving `n` to `right_spot`
                # `nums[idx]` becomes vacant
                nums[idx] = None
                self.place(n, right_spot, nums)
                
        return self.res
                
    def place(self, num, right_spot, nums):
        pass
        occupant = nums[right_spot]
        
        if occupant and occupant != num:
            occupant_right_spot = occupant - 1
            nums[right_spot] = None
            self.place(occupant, occupant_right_spot, nums)
            
        if nums[right_spot] == num:
            self.res.append(num)
        nums[right_spot] = num
        
arr = [
    [1,1,2],
    [2, 2],
    [4,3,2,7,8,2,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findDuplicates(foo)

print(res)