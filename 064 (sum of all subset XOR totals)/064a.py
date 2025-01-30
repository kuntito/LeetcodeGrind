# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

# TODO https://neetcode.io/solutions/sum-of-all-subset-xor-totals
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        pass
        # run a recursive function `explore(currIdx, arr, nums)`
        # for each call of `explore`
        # there are two branches
        # in both branches, currIdx is incremented by `1`
        # in the first branch `arr` stays the same
        # in the second branch `arr` appends `nums[currIdx]`
        # when `currIdx == len(nums)`
        # XOR all the elements in `arr` and return it
        
        return self.explore(0, [], nums)

    def explore(self, idx, arr, nums):
        if idx == len(nums):
            return self.xor_all(arr)
        
        res = 0
        
        arr.append(nums[idx])
        res += self.explore(idx+1, arr, nums)
        arr.pop()
        
        res += self.explore(idx+1, arr, nums)
        return res
        
        
    def xor_all(self, arr):
        if not arr:
            return 0
        
        res = arr[0]
        for n in arr[1:]:
            res ^= n
            
        return res
        
arr = [
    [5, 1, 6],
    [3,4,5,6,7,8],
    [1,3],
]
foo = arr[-1]
sol = Solution()
res = sol.subsetXORSum(foo)
print(res)