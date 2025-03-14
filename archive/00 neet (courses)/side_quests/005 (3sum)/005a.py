# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list) -> list:
        seen = set()
        res = []
        for idx, n in enumerate(nums):
            if n in seen: continue
            seen.add(n)
            two_sums = self.get_two_sum(idx, -n, nums)
            if two_sums:
                for ts in two_sums:
                    sublist = [n] + ts
                    subset = frozenset(sublist)
                    if subset in seen:
                        continue
                    else:
                        res.append(sublist)
                        seen.add(subset)
        return res

    def get_two_sum(self, omit_idx: int, target: int, nums: list):
        res = []
        num_set = set()
        seen = set()

        for idx, n in enumerate(nums):
            if n in seen or idx  == omit_idx: continue

            compliment = target - n
            if compliment in num_set:
                res.append([n, compliment])
                seen.add(n)
                seen.add(compliment)

            num_set.add(n)
        return res

nums = [-1,0,1,2,-1,-4]
# nums = [-1, 0, 1, 0, 0, 0, 0]
# nums = [-4, -1, -1, 0, 1, 2]
sol = Solution()

res = sol.threeSum(nums)
print(res)