# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums, k):
        max_val = -10**4
        nums_map = {}
        for n in nums:
            max_val = max(n, max_val)
            if n not in nums_map:
                nums_map[n] = 0
            nums_map[n] += 1
    
        i = 0
        for n in range(max_val, -10**4, -1):
            if n in nums_map:
                i += nums_map[n]

            if i >= k: return n


nums = [3,2,1,5,6,4]
k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4

foo = Solution()
res = foo.findKthLargest(nums, k)

print(res)

        