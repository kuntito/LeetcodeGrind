
#https://leetcode.com/problems/contains-duplicate/submissions/1329314802/

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        nums_map = {}

        for n in nums:
            if n not in nums_map:
                nums_map[n] = 0
            
            nums_map[n] += 1
            if nums_map[n] == 2:
                return True

        return False