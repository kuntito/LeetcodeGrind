# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # since the values are bounded by len(nums), (0, n-1)
        # it means each number can be mapped to a unique index
        # for each number, mark the index it should be at
        # by negating the value at that index
        # i.e. [1, 4, 4, 2]
        # the value at index `0` is `1`
        # it's corresponding index is `0`
        
        # so negate `nums[0]`
        
        # by this metric every marked index exists in the `nums`
        # and the unmarked ones are the missing ones
        
        # also, consider index `2` where it's value `4`
        # belongs at `index 3`
        # meaning we'd negate `nums[3]`
        
        # but when we reach `nums[3]`, the value would be -2
        # so we'd need to take it's absolute value to determine it's corresponding index

        for n in nums:
            n = abs(n)
            corrIdx = n - 1
            
            if nums[corrIdx] > 0:
                nums[corrIdx] = -1 * nums[corrIdx]
            
        res = []
        for idx, n in enumerate(nums):
            if n > 0:
                res.append(idx + 1)
                
        return res
        
arr = [
    [3, 2, 1],
    [4,3,2,7,8,2,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findDisappearedNumbers(foo)
print(res)
