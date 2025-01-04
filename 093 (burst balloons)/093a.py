# https://leetcode.com/problems/burst-balloons/description/

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        pass
        # you want to priortize the smallest balloon with the largest neighbour product
        
        dim = len(nums)
        
        smallest = nums[0]
        neighbours = nums[1] if 1 < dim else 1
        
        frontman = [smallest, neighbours]
        
        for idx in range(1, dim):
            val = nums[idx]
            left = nums[idx-1]
            right = nums[idx + 1] if idx + 1 < dim else 1
            