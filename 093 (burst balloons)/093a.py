# https://leetcode.com/problems/burst-balloons/description/

import heapq

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        pass
        # a loop, on each iteration, find the smallest balloon with the largest
        # neighbours
            
            
    def get_product(self, idx, arr):
        left = arr[idx - 1] if idx - 1 >= 0 else 1
        right = arr[idx + 1] if idx + 1 < len(arr) else 1
        
        return left * arr[idx] * right
    
arr = [
    [3, 1, 5, 8],
]
foo = arr[-1]
sol = Solution()
res = sol.maxCoins(foo)
print(res)