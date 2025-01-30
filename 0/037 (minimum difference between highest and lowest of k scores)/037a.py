# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

class Solution:
    def minimumDifference(self, nums: int, k: int) -> int:
        # sort `nums`
        nums.sort()
        # set indices `left` and `right` representing a window of size `k`
        left = 0
        right = k - 1
        
        # move the window from left to right, updating the minimum difference
        res = nums[-1]
        while right < len(nums):
            diff = nums[right] - nums[left]
            res = min(
                res,
                diff
            )

            left += 1
            right += 1

        return res

arr = [
    [[9,4,1,7], 2],
    [[90], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minimumDifference(foo, bar)
print(res)
