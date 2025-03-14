# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

# TODO https://neetcode.io/solutions/partition-to-k-equal-sum-subsets
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        pass
        # backtracking problem where we try all the possible combinations
        # you keep adding numbers until the subarray sum becomes greater than `target`
        # or the remainder
        
        # `target` is `total of nums / k`
        # if it `target` is odd, return False
        
        total = sum(nums)        
        target, rem = divmod(total, k)
        if rem:
            return False
        
        # TODO i think the code could work without sorting
        # but sorting might speed up the process
        
        # because if we add a number to the subarray and it exceeds `target`
        # we know not to search further
        # also, if any single number is greater than `target`
        # return False
        nums.sort(reverse=True)
        
        # create a bucket of size `k`
        bucket = [0 for _ in range(k)]
        
        return self.explore(0, target, bucket, nums)
        
    def explore(self, idx, target, bucket, nums):
        dim = len(nums)
        
        if idx == dim:
            return True
        
        n = nums[idx]
        dimTwo = len(bucket)
        for j in range(dimTwo):
            if bucket[j] + n <= target:
                bucket[j] += n
                if self.explore(idx + 1, target, bucket, nums):
                    return True
                bucket[j] -= n
        return False

        
arr = [
    [[5, 4, 3, 3, 2, 2, 1], 4],
    [[1,2,3,4], 3],
]

foo, bar = arr[-1]
sol = Solution()
res = sol.canPartitionKSubsets(foo, bar)
print(res)
