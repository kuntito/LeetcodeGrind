# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer_idx, curr_idx = 0, 1

        count = 1
        while curr_idx < len(nums):
            if nums[curr_idx] != nums[curr_idx - 1]:
                pointer_idx += 1
                nums[pointer_idx] = nums[curr_idx]

                count = 1
            elif nums[curr_idx] == nums[curr_idx - 1] and count < 2:
                pointer_idx += 1
                nums[pointer_idx] = nums[curr_idx]

                count += 1


            curr_idx += 1

        return pointer_idx + 1

arr = [
    [1, 1, 1, 2, 2, 3],
    [0,0,1,1,1,1,2,3,3],
]
foo = arr[-1]
sol = Solution()
res = sol.removeDuplicates(foo)
print(res)