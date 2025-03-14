# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/

class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        uno_sum, uno_slots = self.get_sum_and_zero_count(nums1)
        dos_sum, dos_slots = self.get_sum_and_zero_count(nums2)

        uno_max_sum = uno_slots + uno_sum
        dos_max_sum = dos_slots + dos_sum

        if uno_max_sum < dos_max_sum and uno_slots == 0: return -1
        if uno_max_sum > dos_max_sum and dos_slots == 0: return -1
        
        return max(uno_max_sum, dos_max_sum)



    def get_sum_and_zero_count(self, nums):
        summa, zero_count = 0, 0

        for n in nums:
            summa += n
            if n == 0:
                zero_count += 1

        return summa, zero_count

arr = [
    [
        [2,0,2,0],
        [1,4],
    ],
    [
        [3,2,0,1,0],
        [6,5,0],
    ],
]

foo, bar = arr[-1]
sol = Solution()
res = sol.minSum(foo, bar)

print(res)