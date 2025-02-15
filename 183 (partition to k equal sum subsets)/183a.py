# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

# TODO https://neetcode.io/solutions/partition-to-k-equal-sum-subsets
# look at solution
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        pass
        # at the very least, equalSum >= max(nums)
        nums.sort()
        print(nums)
        
        # total = sum(nums)
        # at the very most, equalSum <= total/k
        # if total % 2: return False
        
        # if you take the largest out
        # is there enough elements to form `k-1` subsets
        # if yes, two pointers
        # compare
        
arr = [
    [[4,3,2,3,5,2,1], 4],
]

foo, bar = arr[-1]
sol = Solution()
res = sol.canPartitionKSubsets(foo, bar)
