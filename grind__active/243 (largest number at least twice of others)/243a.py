# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        # find the largest and second largest
        # return largest/2 > second largest

        largest = 0, float("-inf")
        second_largest = 0, float("-inf")

        for idx, n in enumerate(nums):
            if n > largest[1]:
                second_largest = largest
                largest = (idx, n)
            elif n > second_largest[1]:
                second_largest = (idx, n)

        print(largest[1], second_largest[1])
        if largest[1] / 2 >= second_largest[1]:
            return largest[0]

        return -1

arr = [
    [0,0,1,2],
]
foo = arr[-1]
sol = Solution()
res = sol.dominantIndex(foo)
print(res)