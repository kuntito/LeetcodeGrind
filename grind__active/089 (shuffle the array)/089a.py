# https://leetcode.com/problems/shuffle-the-array/description/

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        pass
        # two pointers, one at the start and the other at the mid point
        # create an array and append the elements at each pointer into it
        arr = []
        
        idxOne = 0
        idxTwo = len(nums)//2
        
        while idxTwo < len(nums):
            arr.append(nums[idxOne])
            arr.append(nums[idxTwo])
            
            idxOne += 1
            idxTwo += 1
            
        return arr
            
arr = [
    [[2,5,1,3,4,7], 3],
    [[1,2,3,4,4,3,2,1], 4],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shuffle(foo, bar)
print(res)