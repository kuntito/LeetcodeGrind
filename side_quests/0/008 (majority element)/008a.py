# https://leetcode.com/problems/majority-element/submissions/1439931525/


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_map = {}
        for n in nums:
            count = nums_map.get(n, 0) + 1
            if count > len(nums)/2:
                return n
            nums_map[n] = count

arr = [
    [3, 2, 3],
]
foo = arr[-1]

sol = Solution()
res = sol.majorityElement(foo)
print(res)
