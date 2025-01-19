
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# TODO https://neetcode.io/solutions/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # determine the short and long array
        short, longg = self.get_short_long(nums1, nums2)
            
        # determine the total length of both arrya
        total = len(nums1) + len(nums2)
        
        # `half`, represents the mid point index
        # [1, 2, 3] => 1 because (3 // 2)
        # [1, 2, 3, 4] => 2 because (4 // 2)
        half = total // 2

        l, r = 0, len(short) - 1
        while True:
            # mid point of the short index
            ix_sh = (l + r) // 2
            # TODO why `-2`?
            ix_lg = half - ix_sh - 2

            Aleft = short[ix_sh] if ix_sh >= 0 else float("-infinity")
            Aright = short[ix_sh + 1] if (ix_sh + 1) < len(short) else float("infinity")
            Bleft = longg[ix_lg] if ix_lg >= 0 else float("-infinity")
            Bright = longg[ix_lg + 1] if (ix_lg + 1) < len(longg) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = ix_sh - 1
            else:
                l = ix_sh + 1
    
    def get_short_long(self, a, b):
        short, longg = a, b
        if len(short) > len(longg):
            short, longg = longg, short
            
        return short, longg
            

arr = [
    [[1, 3], [2]],
    [[1, 2,], [3, 4]],
    [[1, 3, 3, 5], [5]],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.findMedianSortedArrays(foo, bar)
print(res)
