# https://leetcode.com/problems/majority-element/description

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

arr = [
    [3, 2, 3],
    [10,9,9,9,10],
]
foo = arr[-1]

sol = Solution()
res = sol.majorityElement(foo)
print(res)
