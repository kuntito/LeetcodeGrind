class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums: return -1

        start, end = 0, len(nums)

        while (end - start) > 1:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid

        return start if nums[start] == target else -1
    

arr = [
    [[2, 3, 10], 10],
    [[-1,0,3,5,9,12], 9],
    [[-1,0,3,5,9,12], 2],
]
nums, target = arr[-1]

sol = Solution()
res = sol.search(nums, target)

print(res)