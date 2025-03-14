class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer, runner = 0, 0

        while runner < len(nums):
            count = 1
            while runner + 1 < len(nums) and nums[runner] == nums[runner + 1]:
                count += 1
                runner += 1

            limit = min(2, count)
            for _ in range(limit):
                nums[pointer] = nums[runner]
                pointer += 1
            runner += 1

        return pointer
    
arr = [
    [0,0,1,1,1,1,2,3,3],
    [1, 1, 1, 2, 2, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.removeDuplicates(foo)
print(res)