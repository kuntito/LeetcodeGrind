# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1
    
nums = [-1,0,3,5,9,12]
foo = Solution()
res = foo.search(nums, 9)

print(res)