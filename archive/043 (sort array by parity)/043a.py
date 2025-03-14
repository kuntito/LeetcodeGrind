# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        dim = len(nums)

        # place `oddIdx` at the first odd number
        oddIdx = 0
        while oddIdx < dim and nums[oddIdx] % 2 == 0:
            oddIdx += 1
        if oddIdx == dim:
            return nums
        
        evenIdx = oddIdx + 1
        # `evenIdx` starts after the first odd number
        # and moves till it finds the first even number
        # once found, swap values and move `oddIdx` forward by 1
        # keeping moving `evenIdx` till another even number occurs,
        # repeat till `evenIdx` reaches the end
        while evenIdx < dim:
            n = nums[evenIdx]

            if n % 2 == 0:
                nums[oddIdx], nums[evenIdx] = nums[evenIdx], nums[oddIdx]
                oddIdx += 1

            evenIdx += 1

        return nums
    
arr = [
    [3,1,2,4],
    [0],
    [2, 4, 8],
    [1, 3, 5]
]
foo = arr[-1]
sol = Solution()
res = sol.sortArrayByParity(foo)
print(res)