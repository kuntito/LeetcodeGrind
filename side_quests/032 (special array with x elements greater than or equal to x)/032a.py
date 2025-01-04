# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

# TODO https://www.youtube.com/watch?v=Z51jYCeBLVI
# TODO why does this solution work?
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        # sort `nums`
        nums.sort()

        # loop through `nums` with item index
        # if the count of elements from `idx` till the end is less than or equal elem[idx]
        # return count

        for idx, elem in enumerate(nums):
            count = len(nums) - idx
            if count <= elem:
                if idx == 0 or count > nums[idx - 1]:
                    return count
            
        return -1
    
arr = [
    [3,5],
    [0,0],
    [0,4,3,0,4],
    [0,3,6,7,7],
]
foo = arr[-1]
sol = Solution()
res = sol.specialArray(foo)
print(res)