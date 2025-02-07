# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# TODO rewrite to show that you understand it
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        
        nums_map = {}
        start = 0
        res = 0
        for idx, n in enumerate(nums):
            nums_map[n] = nums_map.get(n, 0) + 1

            if nums_map[n] > k:
                res = max(
                    res,
                    idx - start
                )

                while nums_map[n] > k:
                    nums_map[nums[start]] -= 1
                    start += 1

        res = max(
            res,
            idx - start + 1,
        )
        return res