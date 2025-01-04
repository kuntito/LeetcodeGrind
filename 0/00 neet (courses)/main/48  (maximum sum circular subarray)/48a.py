# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        self.nums = nums
        self.max_sum = self.nums[0]

        has_neg = self.get_best_sum()

        if has_neg:
            idx = 0
            while idx < len(nums):
                if nums[idx] > 0:
                    res = self.get_circular_best_sum(idx)
                    if res and res < len(nums):
                        idx = res
                        continue

                idx += 1

        return self.max_sum
    

    def get_best_sum(self):
        temp = 0
        has_neg = False
        for n in self.nums:
            if not has_neg and n < 0:
                has_neg = True

            temp = max(temp, 0) + n
            self.max_sum = max(self.max_sum, temp)
        return has_neg


    
    def get_circular_best_sum(self, index: int):
        x = len(self.nums)

        temp = 0
        self.max_sum = max(self.max_sum, self.nums[index % x])
        for _ in range(x):
            n = self.nums[index % x]
            if temp < 0:
                return index
            temp = max(temp, 0) + n
            self.max_sum = max(self.max_sum, temp)
            index += 1

        
    

arr = [
    [1, -2, 3, -2],
    [-9,14,24,-14,12,18,-18,-10,-10,-23,-2,-23,11,12,18,-9,9,-29,12,4,-8,15,11,-12,-16,-9,19,-12,22,16],
    [-2, 4, -5, 4, -5, 9, 4],
    [0, 5, 8, -9, 9, -7, 3, -2],
    [-5,-2,5,6,-2,-7,0,2,8],
    [-3, -2, -3],
    [5, -3, 5],
    [5,6,1,4,8,-8,7,-5,3],
    [5,-19,10,-15,22,-2,-11,28,-29,10,1,2,22,-23,-9,-30,-6,-9,1,8,24,2,21,29,10,-25,18,30,1,9],
]
foo = arr[-1]

sol = Solution()
res = sol.maxSubarraySumCircular(foo)

print(res)