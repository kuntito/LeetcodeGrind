# https://leetcode.com/problems/longest-increasing-subsequence/description/

# TODO https://neetcode.io/solutions/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        pass
        # create an array, `arr`
        # iterate through `nums`, place each number, `n` in array
        # use binary search to determine where `n` should be placed in the array
        # return the length of the array
        
        arr = []
        for n in nums:
            idx = self.get_index(n, arr)
            if idx == len(arr):
                arr.append(n)
            else:
                arr[idx] = n        
        
        return len(arr)
    
    
    def get_index(self, num, arr):
        if not arr:
            return 0
        
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            if num > arr[mid]:
                left = mid + 1
            elif num < arr[mid]:
                right = mid - 1
            else:
                return mid

        # if the left passes the right, it means that's the next position
        # if right goes behind left, it means left's position is where the item would have been found if it existed
        return left

    
    
arr = [
    [7,7,7,7,7,7,7],
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [1,3,6,7,9,4,10,5,6],
]
foo = arr[-1]
sol = Solution()
res = sol.lengthOfLIS(foo)
print(res)
