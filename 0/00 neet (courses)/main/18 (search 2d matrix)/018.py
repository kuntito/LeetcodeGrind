# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return True

        return False


    def searchMatrix(self, matrix, target: int):
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid  = (top + bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif self.search(matrix[mid], target):
                return True
            else:
                bottom = mid - 1

        return False
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

foo = Solution()
res = foo.searchMatrix(matrix, target)

print(res)