# https://leetcode.com/problems/next-greater-element-i/description/

# TODO https://neetcode.io/solutions/next-greater-element-i
# 07:55
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # put all elems of `nums1` into a map, each value should be -1
        num_map = {n: -1 for n in nums1}

        # loop through `nums2` in reverse, maintaining a monotonically decreasing stack
        stack = []
        for idx in range(len(nums2)-1, -1, -1):
            n = nums2[idx]

            while stack and n > stack[-1]:
                stack.pop()
            # for every element in `num2` that's in `num1`,
            # if the last element of the stack is greater than the current element in `num2`
            if n in num_map and stack and n < stack[-1]:
                num_map[n] = stack[-1]

            stack.append(n)
            # set it's hash map value to that number else `-1`

        for idx, n in enumerate(nums1):
            nums1[idx] = num_map[n]

        return nums1


arr = [
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[4, 1, 2], [1, 3, 4, 2]],
    [[2, 4], [1, 2, 3, 4]],
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.nextGreaterElement(foo, bar)

print(res)