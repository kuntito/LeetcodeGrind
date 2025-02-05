# https://leetcode.com/problems/find-k-closest-elements/

import heapq
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        pass
        # use binary search to find x's index, `idx`
        # if x does not exist search all indices `[idx: ]`
        # and `[:idx-1]` and store k values on both sides in a heap
        
        # if `x` does exist, search `[idx+1: ]` and [:idx-1]
        
        idx = self.get_index(arr, x)
        dim = len(arr)        

        left, right = idx - 1, idx
        count = 0
        res = []
        while len(res) < k and left >= 0 and right < dim:
            pass
            leftNum = arr[left]
            rightNum = arr[right]
            
            leftAbs = abs(x - leftNum)
            rightAbs = abs(x - rightNum)
            
            if leftAbs <= rightAbs:
                res.append(leftNum)
                left -= 1
            else:
                res.append(rightNum)
                right += 1
                
        while left >= 0 and len(res) < k:
            res.append(arr[left])
            left -= 1
            
        while right < dim and len(res) < k:
            res.append(arr[right])
            right += 1
                
                
        return sorted(res)
                

        
    def get_index(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
    
arr = [
    [[1,1,1,10,10,10], 1, 9],
    [[1,1,2,3,4,5], 4, -1],
    [[1, 2, 3, 4, 5], 4, 3],
    [[0,0,1,2,3,3,4,7,7,8], 3, 5]
]
foo, bar, zar = arr[-1]
sol = Solution()
res = sol.findClosestElements(foo, bar, zar)
print(res)