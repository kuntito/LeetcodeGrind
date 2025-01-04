# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        setOne = set(nums1)
        setTwo = set(nums2)

        a = []
        for n in setOne:
            if n in setTwo: continue
            a.append(n)

        b = []
        for n in setTwo:
            if n in setOne: continue
            b.append(n)

        return [a, b]
    
arr = [
    [[1, 2, 3, 3], [1, 1, 2, 2]],
]
foo = arr[-1]
sol = Solution()