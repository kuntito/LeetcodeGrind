# https://leetcode.com/problems/majority-element/description

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elem, count = nums[0], 1

        for n in nums[1:]:
            if elem == n:
                count += 1
            else:
                count -= 1

            if count < 0:
                elem = n
                count = 1

        return elem

arr = [
    [3, 2, 3],
    [10,9,9,9,10],
]
foo = arr[-1]

sol = Solution()
res = sol.majorityElement(foo)
print(res)
