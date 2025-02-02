# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

# TODO https://neetcode.io/solutions/special-array-with-x-elements-greater-than-or-equal-x
# 11:40
# TODO skip to his second solution, 
# the first solution is similar to mine but deep overcomplicates the first solution
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
                # [0,3,6,7,7]
                # when idx is at `2`, there are 3 elements from that point onwards
                # and nums[idx] >= 3 but the question demands that `nums[idx:]` should be the only elements >= `x|3`
                # and nums[1] vioates that so you have to check if the count is greater than the previous element
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