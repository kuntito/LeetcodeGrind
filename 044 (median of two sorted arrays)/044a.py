# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# TODO https://neetcode.io/solutions/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # TODO would it work with this if either array is empty
        if bool(nums1) ^ bool(nums2):
            return self.find_median(nums1) if nums1 else self.find_median(nums2)
        
        short, longer = self.get_short_long(nums1, nums2)
        # run binary search on the short index
        # use the short index to calculate the position of the long index
        # if the short index value is greater than long index + 1
        # move the bin search leftwards
        # if the long index value is greater than short index + 1
        # move the bin search rightwards


    def get_short_long(self, a, b):
        return (a, b) if len(a) < len(b) else (b, a)

        



        
            

arr = [
    [[1, 3], [2]],
    [[1, 2,], [3, 4]],
    [[1, 3, 3, 5], [5]],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.findMedianSortedArrays(foo, bar)
print(res)
