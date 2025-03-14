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

        uno, dos = start_idx, len(nums) - 1

        while uno < dos:
            a = nums[uno]
            b = nums[dos]
            agg = a + b
            if agg == target:
                res.append([a, b])
                while uno < len(nums) and nums[uno] == a:
                    uno += 1
                while dos >= start_idx and nums[dos] == b:
                    dos -= 1
                
            elif agg > target:
                dos -= 1
            else:
                uno += 1

        return res


arr = [
    [-1,0,1,2,-1,-4],
    [0, 0, 0, 0],
]
foo = arr[-1]
sol = Solution()
res = sol.threeSum(foo)
print(res)