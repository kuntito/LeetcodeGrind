from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dim = len(nums)

        imposters = 0

        prev = nums[0]

        for idx in range(dim):
            cur = nums[idx]

            if prev <= cur:
                prev = cur
            else:
                imposters += 1

                beforePrev = nums[idx - 2] if idx -2 >= 0 else None
                if beforePrev is None:
                    prev = cur
                elif beforePrev <= cur:
                    prev = cur

        return imposters <= 1
    
    
arr = [
    [4, 2, 3],
    [3, 4, 2, 3],
    [-1,4,2,3],
]
foo = arr[-1]
sol = Solution()

res = sol.checkPossibility(foo)
print(res)
