# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        setOne = set(nums1)
        setTwo = set(nums2)

        res = []
        a = list(setOne - setTwo)
        b = list(setTwo - setOne)

        res.append(a)
        res.append(b)

        return res
    