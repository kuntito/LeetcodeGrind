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
        zero_edge_case = False
        for idx in range(start_idx, len(nums)):
            n = nums[idx]

            compliment = target - n

            if compliment in seen:
                if n == 0 and compliment == 0:
                    zero_edge_case = True
                else:
                    res.append(
                        [n, compliment]
                    )
            seen.add(n)
            
        if zero_edge_case and target == 0:
            res.append([0, 0])

        return res


arr = [
    [-1,0,1,2,-1,-4],
    [-1,0,1,0],
    [0, 0, 0, 0],
]
foo = arr[-1]
sol = Solution()
res = sol.threeSum(foo)
print(res)