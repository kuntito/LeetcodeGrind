# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

# https://neetcode.io/solutions/partition-to-k-equal-sum-subsets
# TODO why do we need to prune?
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        # it's a recursive backtracking problem
        # where we try all combinations to fill each subarray
        # we'd track the following `explore(idx, nums, kLeft, seen, target, curSum)`
        # `idx` is the current index we're exploring
        # `kLeft` is the numeber of remaining sub arrays
        # `seen` is a set representing the indices already seen in a subarray
        # `target` is the sum of each subarray
        
        # for any of this to be possible,
        # the sum of `nums` should divisible by `k` without remainder
        
        target, rem =  divmod(sum(nums), k)
        if rem:
            return False

        # nums.sort(reverse=True)
        
        self.nums = nums
        self.seen = [False for _ in nums]
        self.target = target
        return self.explore(0, k, 0)
    
    def explore(self, start_idx, kLeft, curSum):
        if kLeft == 0:
            return True
        if curSum == self.target:
            return self.explore(0, kLeft-1, 0)
        
        dim = len(self.nums)
        for idx in range(start_idx, dim):
            n = self.nums[idx]
            if self.seen[idx] or curSum + n > self.target:
                continue
            
            self.seen[idx] = True
            if self.explore(idx + 1, kLeft, curSum + n):
                return True
            self.seen[idx] = False

            if curSum == 0: # Pruning
                return False
            
        return False
            
        
        
arr = [
    [[1,2,3,4], 3],
    [[5, 4, 3, 3, 2, 2, 1], 4],
]

foo, bar = arr[-1]
sol = Solution()
res = sol.canPartitionKSubsets(foo, bar)
print(res)
