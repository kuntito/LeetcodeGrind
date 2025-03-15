# https://leetcode.com/problems/search-insert-position/description/

# TODO https://neetcode.io/solutions/search-insert-position
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            val = nums[mid]
            if target == val:
                return mid
            elif target > val:
                left = mid + 1
            else:
                right = mid - 1

        if right > left:
            return left
        if left > right:
            return left


            
arr = [
    [[1, 3, 5, 6], 18],
    [[1, 3, 5, 6], 5],
    [[1, 3, 5, 6], 2],
    [[1, 3], 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.searchInsert(foo, bar)
print(res)