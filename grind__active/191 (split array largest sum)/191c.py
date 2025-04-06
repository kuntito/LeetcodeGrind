# https://leetcode.com/problems/split-array-largest-sum/description/

# TODO neet solution
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res