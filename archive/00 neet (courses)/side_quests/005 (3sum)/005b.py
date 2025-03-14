class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        seen = set()
        res = []

        for idx, n in enumerate(nums):
            if n in seen: continue
            seen.add(n)

            two_sums = self.get_two_sums(idx+1, -n, nums)
            for ts in two_sums:
                res.append([n] + ts)

        return res
    
    def get_two_sums(self, start_idx, target, nums):
        res = []
        seen = set()
        numset = set()
        for n in nums[start_idx:]:
            if n in seen: continue

            compliment = target - n
            if compliment in numset:
                res.append([n, compliment])
                seen.add(compliment)
                seen.add(n)

            numset.add(n)
        return res


nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0, 0]
# nums = [-1, 0, 1, 0, 0, 0, 0]
# nums = [-4, -1, -1, 0, 1, 2]
sol = Solution()

res = sol.threeSum(nums)
print(res)