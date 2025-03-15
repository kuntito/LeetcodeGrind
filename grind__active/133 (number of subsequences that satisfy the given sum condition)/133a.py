# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

# TODO this implementation checks for sub arrays not sub sequences
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        pass
    
        # TODO imma assume `nums` is sorted
                
        self.res = []
        self.explore(0, len(nums)-1, nums, target, {})
        
        return self.res
        
    def explore(self, left, right, arr, target, memo):
        if left > right:
            return
        
        mode = (left, right)
        if mode in memo:
            return memo[mode]
        
        total = arr[left] + arr[right]
        if total <= target:
            slice = arr[left:right+1]
            self.res.append(slice)
            memo[mode] = slice
        
        self.explore(left, right-1, arr, target, memo)
        self.explore(left+1, right, arr, target, memo)

arr = [
    [[3,3,6,8], 10],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numSubseq(foo, bar)

print(res)
        