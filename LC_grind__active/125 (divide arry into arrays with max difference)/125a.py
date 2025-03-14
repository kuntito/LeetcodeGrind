# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        pass
        # sort the array
        nums.sort()
        print(nums)
        res = []
        # determine the three slices
        dim = len(nums)
        step = dim // 3
        for i in range(0, dim, dim//3):
            slice = nums[i: i + step]
            
            # for each slice, if slice[0] + k > slice[-1]
            if slice[0] + k > slice[-1]:
                # return an empty array
                return []
    
            # else append the slice to res 
            res.append(slice)
        return res
        
        
arr = [
    [[1,3,4,8,7,9,3,5,1], 2],
    [[2,4,2,2,5,2], 2],
    [[4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.divideArray(foo, bar)
print(res)