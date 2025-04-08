# https://leetcode.com/problems/find-in-mountain-array/description/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
         self.arr = arr
    
    def get(self, index: int) -> int:
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)


# TODO You made too many calls to MountainArray.get().
class Solution:
    def findInMountainArray(self, target: int, mountainArr: MountainArray) -> int:
        pass
    
        # there exists a point where all the elements before it are in ascending order
        # and all the elements after it are in descending order
        
        # using binary search find the peak of the mountainArr
        
        # using binary seach, check if target is within [:peak]
        
        # or within [peak: len(mountain) - 1]
        
        # if peak is found, return peak else -1

        self.mountain = mountainArr
        dim = self.mountain.length()
        peak_idx = self.findPeak(0, dim)

        
        # find if target is in left slice
        leftRes = self.binSearch(0, peak_idx, target)
        if leftRes != -1:
            return leftRes
        
        return self.binSearchNeg(peak_idx + 1, dim-1, target)
        
    def findPeak(self, left, right):
        while left <= right:
            mid = (left + right) // 2
            midValue = self.mountain.get(mid)
            leftValue = self.mountain.get(mid-1)
            rightValue = self.mountain.get(mid + 1)
            
            is_peak = leftValue < midValue > rightValue
            if is_peak:
                return mid
            elif leftValue < midValue < rightValue:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    def binSearch(self, left, right, targt):
        while left <= right:
            mid = (left + right)//2
            midValue = self.mountain.get(mid)
            
            if midValue == targt:
                return mid
            elif midValue < targt:
                left += 1
            else:
                right -= 1
                
        return -1

    def binSearchNeg(self, left, right, targt):
        while left <= right:
            mid = (left + right)//2
            midValue = self.mountain.get(mid)
            
            if midValue == targt:
                return mid
            elif midValue > targt:
                left += 1
            else:
                right -= 1
                
        return -1
                
        
arr = [
    [[0,1,2,4,2,1], 3],
    [[0,5,3,1], 1],
    [[1,2,3,4,5,3,1], 3],
]
foo, bar = arr[-1]

mountain = MountainArray(foo)
sol = Solution()
res = sol.findInMountainArray(bar, mountain)
print(res)

