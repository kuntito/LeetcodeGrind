# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1: return nums
        
        return self.explore(nums)
    
    def explore(self, arr):
        if len(arr) == 1: return arr
        mid_point = len(arr)//2

        left_half = arr[:mid_point]
        right_half = arr[mid_point:]

        left_res = self.explore(left_half)
        right_res = self.explore(right_half)

        idx = len(arr) - 1
        while left_res and right_res:
            right_val = right_res[-1]
            left_val = left_res[-1]

            if right_val > left_val:
                arr[idx] = right_res.pop()
            else:
                arr[idx] = left_res.pop()
            idx -= 1

        while left_res:
            arr[idx] = left_res.pop()
            idx -= 1
        while right_res:
            arr[idx] = right_res.pop()
            idx -= 1

        return arr
    

nums = [3, 4, 3, 3, 2, 1]
foo = Solution()
res = foo.sortArray(nums)

print(res)