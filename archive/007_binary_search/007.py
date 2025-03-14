# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target

        return self.explore_dfs_binary(0, len(nums))


    def explore_dfs_binary(self, start: int, end: int):
        if end - start == 0: return -1
        if (end - start) == 1:
            return start if self.nums[start] == self.target else -1
        
        mid = start + (end - start) // 2
        if self.nums[mid] > self.target:
            end = mid
        else:
            start = mid

        return self.explore_dfs_binary(start, end)


arr = [
    [[2, 3, 10], 10],
    [[-1,0,3,5,9,12], 2],
    [[-1,0,3,5,9,12], 9],
]
nums, target = arr[-1]

sol = Solution()
res = sol.search(nums, target)

print(res)