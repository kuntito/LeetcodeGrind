from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dim = len(nums)
        for idx in range(dim):
            shortGuy = nums[idx]
            for idxTwo in range(idx + 1, dim):
                maybeTallestGuy = nums[idxTwo]
                if maybeTallestGuy > shortGuy:
                    tallestGuy = maybeTallestGuy
                    for idxThree in range(idxTwo + 1, dim):
                        maybeTallerGuy = nums[idxThree]
                        if tallestGuy > maybeTallerGuy > shortGuy:
                            return True
                        
        return False

            