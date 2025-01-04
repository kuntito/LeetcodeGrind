class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        nums_map = {}

        for n in nums:
            if n in nums_map:
                return True
            else:
                nums_map[n] = 0

        return False