# https://leetcode.com/problems/sliding-window-median/description/
import heapq
class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        self.arr = []

        for n in nums[:k]:
            self.arr.append(n)
        
        self.arr.sort()
        res = [self.get_median()]

        curr_idx = k
        while curr_idx < len(nums):
            self.add_remove(
                curr_idx - k, 
                curr_idx,
                nums,
            )
            curr_idx += 1
            res.append(self.get_median())

        return res
    

    def add_remove(self, remove_idx, curr_idx, nums):
        old_val = nums[remove_idx]
        idx = self.bin_search(old_val)
        self.arr[idx] = nums[curr_idx]
        self.arr.sort()

    def bin_search(self, val):
        left, right = 0, len(self.arr)

        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] == val:
                return mid
            elif val > self.arr[mid]:
                left = mid + 1
            else:
                right = mid

    
    def get_median(self):
        mid = len(self.arr) // 2
        res = self.arr[mid]

        if len(self.arr) % 2 == 0:
            res += self.arr[mid - 1]
            res /= 2

        return res
        

    

arr =[
    [[1,3,-1,-3,5,3,6,7], 3],
    [[2147483647,1,2,3,4,5,6,7,2147483647], 2],
    [[3,1,4,2], 3],
    [[1,2], 1],
    [[1,2,3,4,2,3,1,4,2], 3],
]

foo, bar = arr[-1]
sol = Solution()
res = sol.medianSlidingWindow(foo, bar)
print(res)