# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        big, small = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        # create a set to store all unique characters from one array
        # loop through the other array and store each character that's been seen
        # other array could contain duplicates so remove each character the moment
        # it has been stored

        seen = set()
        for n in big:
            seen.add(n)

        res = []
        for n in small:
            if n in seen:
                res.append(n)
                seen.remove(n)

        return res
    
arr = [
    [[4,9,5], [9,4,9,8,4]],
    [[1,2,2,1], [2,2]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.intersection(foo, bar)
print(res)