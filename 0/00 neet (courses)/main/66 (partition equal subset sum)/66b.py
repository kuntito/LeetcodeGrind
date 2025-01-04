# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        seen_sums = set()
        seen_sums.add(0)
        target = sum(nums) // 2

        for n in nums:
            temp = seen_sums.copy()
            for elem in seen_sums:
                foo = elem + n
                if foo > target: continue
                if foo == target: return True
                temp.add(foo)
            seen_sums = temp

        return False


arr = [
    [5, 10, 5],
    [1, 5, 11, 5],
]
foo = arr[-1]
sol = Solution()
res = sol.canPartition(foo)
print(res)