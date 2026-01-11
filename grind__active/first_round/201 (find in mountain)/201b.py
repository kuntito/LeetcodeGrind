# https://leetcode.com/problems/find-in-mountain-array/description/

# TODO https://neetcode.io/solutions/find-in-mountain-array
class MountainArray:
    def __init__(self, arr):
         self.arr = arr
    
    def get(self, index: int) -> int:
        if index < 0: return None
        return self.arr[index]
    
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def __init__(self):
        self.peakIdx = None
        self.peakValue = None
    
    def findInMountainArray(self, target: int, mountainArr: MountainArray) -> int:
        # find the peak
        if self.peakIdx == None:
            self.peakIdx, self.peakValue = self.getPeakDetails(mountainArr)
        
        # check if peak value is `target`
        if target == self.peakValue:
            return self.peakIdx
        
        # else if check peak left for `target`
        res = self.checkLeft(target, self.peakIdx, mountain)
        if res != -1:
            return res
        
        # then check peak right for `target`
        return self.checkRight(target, self.peakIdx, mountain)
        
        # might need to optimize based on every search
        
    def checkLeft(self, target, peakIdx, mountain):
        left, right = 0, peakIdx-1
        
        while left <= right:
            mid = (left + right) // 2
            
            val = mountain.get(mid)
            if val == target:
                return mid
            
            if target < val:
                right = mid - 1
            else:
                left = mid + 1
        return -1
                
    def checkRight(self, target, peakIdx, mountain):
        left, right = peakIdx + 1, mountain.length() - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain.get(mid)
            
            if val == target:
                return mid
            
            if target < val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
    def getPeakDetails(self, arr: MountainArray):
        pass
        # i think a binary search might work
        # we'd check the mid point if it's the peak
        # if not, it could either be ascending or descending
        # with respect to it's neighbours
        
        # if ascending, we move leftwards
        # if descending, we move rightwards
        
        left, right = 0, arr.length() - 1
        
        while left <= right:
            idx = (left + right) // 2
            midVal = arr.get(idx)
            
            prevVal = arr.get(idx - 1) if idx - 1 >= 0 else -1
            nexVal = arr.get(idx + 1) if idx + 1 < arr.length() else float("inf")
            isPeak = prevVal < midVal > nexVal
            
            if isPeak:
                return idx, midVal
            elif prevVal < midVal:
                # is ascending
                left = idx + 1
            else:
                right = idx - 1
                
arr = [
    [[1,2,3,4,5,3,1], 3],
    [[0,1,2,4,2,1], 3],
    [[0,5,3,1], 1],
    [[3,5,3,2,0], 0]
]
foo, bar = arr[-1]

mountain = MountainArray(foo)
sol = Solution()
res = sol.findInMountainArray(bar, mountain)
print(res)