# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums)

        left_sum = 0
        for idx, n in enumerate(nums):
            right_sum -= n
            if left_sum == right_sum:
                return idx
            
            left_sum += n

        return -1
    
arr = [
    [2,1,-1],
    [1,7,3,6,5,6],
    [1,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.pivotIndex(foo)
print(res)
