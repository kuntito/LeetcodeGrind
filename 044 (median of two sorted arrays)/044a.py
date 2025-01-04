# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# TODO would solution work for [], [1] or [], [] or [1, 2, 3], []
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # if either array is empty
        if bool(nums1) ^ bool(nums2):
            return self.find_median(nums1) if nums1 else self.find_median(nums2)
        
        short, longer = self.get_short_long(nums1, nums2)
        total = len(short) + len(longer)
        
        midIdx = total // 2
        
        ls_idx = 0
        # because `short` is the shorter array, the farthest it's right index can be is always the last index
        # since `len(short) <= len(longer)` 
        rs_idx = len(short) - 1 
        
        ll_idx = 0
        rl_idx = None
        # if the middle index overlaps into the long array
        if midIdx >= len(short):
            rl_idx = midIdx - len(short)
            
        
        # the right place is where max(rightShortValue, rightLongValue) < min([rightShort + 1]Value, [rightLong + 1]Value )
        
        # since, i start out maximizing the short array
        # there's no way `rs_idx` moves right
        rsValue = short[rs_idx] if rs_idx >= 0 else float("-inf")
        rsAfterValue = short[rs_idx + 1] if rs_idx + 1 < len(short) else float("inf")
        
        rlValue = longer[rl_idx]
        rlAfterValue = longer[rl_idx + 1] if rl_idx + 1 < len(longer) else float("inf")
        
        while max(rsValue, rlValue) >= min(rsAfterValue, rlAfterValue):
            rs_idx -= 1
            rl_idx += 1
            
            rsValue = short[rs_idx] if rs_idx >= 0 else float("-inf")
            rsAfterValue = short[rs_idx + 1] if rs_idx + 1 < len(short) else float("inf")
            
            rlValue = longer[rl_idx]
            rlAfterValue = longer[rl_idx + 1] if rl_idx + 1 < len(longer) else float("inf")
            
        # TODO when all said and done, what's the median?
        

    def find_median(self, arr):
        if not arr:
            return 0
        
        mid = len(arr)//2

        res = arr[mid]
        return res if len(arr) % 2 else (res + (arr[mid-1])/2)


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
