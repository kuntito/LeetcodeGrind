# https://leetcode.com/problems/binary-subarrays-with-sum/description/

# TODO is this same as counting unique subarrays?
# combinations?
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        pass
        # recursively check every subarray
        # memoize
        
        total, count = self.explore(0, len(nums)-1, nums, goal, {})
        return count
    
    # this returns the total sum at this point and the count
    def explore(self, left, right, arr, goal, memo):
        mode = (left, right)
        if mode in memo:
            return memo[mode][0], 0
        
        count = 0
        if left == right:
            res = None
            if arr[left] == goal:
                res = arr[left]
            memo[mode] = res, 1
            return res, 1
            
    
        leftSum, leftCount = self.explore(left + 1, right, arr, goal, memo)
        rightSum, rightCount = self.explore(left, right - 1, arr, goal, memo)
        
        count = leftCount + rightCount
        total = leftSum + rightSum
        if total == goal:
            count += 1
            
        memo[mode] = total, count
        return total, count
    
arr = [
    [[0, 0, 0], 0],
    [[0, 0, 0, 0, 0], 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numSubarraysWithSum(foo, bar)
print(res)