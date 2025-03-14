# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        nums.sort()
        idx = 0
        while idx < len(nums):
            n = nums[idx]
            temp = []
            consec_nums = []
            while idx < len(nums) and nums[idx] == n:
                consec_nums.append(n)
                idx += 1
            
            for sub in res:
                for i in range(len(sub) + 1):
                    sub_copy = sub[::]
                    sub_copy[i:i] = consec_nums
                    temp.append(sub_copy)
                    self.spread_duplicates(consec_nums, i, sub, temp)

            res = temp
        return res
            

    def spread_duplicates(self, consec_nums, stay_idx, sub, temp):
        for slice_index in range(1, len(consec_nums)):
            stay = consec_nums[slice_index:]
            move = consec_nums[:slice_index] 

            for move_idx in range(stay_idx + len(stay) + 1, len(sub) + len(stay) + 1):
                sub_copy = sub[::]
                sub_copy[stay_idx:stay_idx] = stay
                self.spread_duplicates(
                    move,
                    move_idx,
                    sub_copy,
                    temp
                )
                sub_copy[move_idx:move_idx] = move
                temp.append(sub_copy)

                


arr = [
    [1,2],
    [1,1,3,3,3,2,1],
    [2,2, 1, 1, 1],
    [2,2, 1,],
    [2,2, 1, 1],
    [3,3,0,3],
]
foo = arr[-1]
sol = Solution()
res = sol.permuteUnique(foo)

for row in res:
    print(row)
