# https://leetcode.com/problems/monotonic-array/description/


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        order = None
        dim = len(nums)

        for idx in range(1, dim):
            n = nums[idx]
            prev_n = nums[idx - 1]

            # if the previous number is different from the current
            # an order has been established
            if order is None and n != prev_n:
                # `True` means increasing order
                # `False` measns decreasing order
                order = True if n > prev_n else False
            
            if order and prev_n > n:
                return False
            elif order is False and n > prev_n:
                return False
            
        return True

arr = [
    [1,3,2],
    [6,5,4,4],
    [1,2,2,3],
    [2, 2, 2, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.isMonotonic(foo)
print(res)