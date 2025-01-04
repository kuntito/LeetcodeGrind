# https://leetcode.com/problems/find-the-duplicate-number/description/


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        new_slow = 0
        while slow != new_slow:
            slow = nums[slow]
            new_slow = nums[new_slow]

        return slow



                
arr = [
    [2, 2, 2, 2, 2],
    [1, 3, 4, 2, 2],
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [3, 3, 3, 3, 3],
    [4,3,1,4,2,],
    [2,5,9,6,9,3,8,9,7,1],
]
foo = arr[-1]
sol = Solution()

res = sol.findDuplicate(foo)
print(res)