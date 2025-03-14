# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        seen = set()

        for idx, n in enumerate(nums):
            if n in seen: continue

            for ts in self.get_two_sums(idx + 1, -n, nums):
                res.append(
                    ts + [n]
                )

            seen.add(n)
        return res


    def get_two_sums(self, start_idx, target, nums):
        res = []

        seen = set()
        valid_compliments = set()
        for idx in range(start_idx, len(nums)):
            n = nums[idx]
            compliment = target - n
            if compliment in valid_compliments:
                continue

            if compliment in seen:
                res.append(
                    [n, compliment]
                )
                valid_compliments.add(compliment)
            seen.add(n)
            

        return res


arr = [
    [0, 0, 0, 0],
    [-1,0,1,2,-1,-4],
]
foo = arr[-1]
sol = Solution()
res = sol.threeSum(foo)
print(res)