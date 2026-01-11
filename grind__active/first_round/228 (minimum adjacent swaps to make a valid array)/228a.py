# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/

# find the smallest number
# find the biggest number
# determine the first occurence of the smallest number, `firstIdx`
# determine the last occurence of the largest number, `lastIdx`

# it would take `firstIdx` swaps to get the smallest number to index `0`

# normally, it would take (dim - lastIdx + 1) for the biggest number to reach the end
# however, if the smallest number crossed it i.e. swapped with it, it means part of that journey
# has already been made so `dim - lastIdx + 1 + 1`
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        pass
        small, big = self.get_small_and_big(nums)
        firstIdx, lastIdx = self.getFirstAndLast(nums, small, big)
        
        
        is_cross = firstIdx > lastIdx
        
        smSwaps = firstIdx
        
        lastIdx += 1 if is_cross else 0
        bgSwaps = len(nums) - (lastIdx + 1)
        
        return smSwaps + bgSwaps
                
    def getFirstAndLast(self, nums, small, big):
        firstIdx = None
        lastIdx = None
        
        for idx, n in enumerate(nums):
            if n == small and firstIdx is None:
                firstIdx = idx
                
            if n == big:
                lastIdx = idx

        return firstIdx, lastIdx    
            
    def get_small_and_big(self, nums):
        small, big = float("inf"), float("-inf")
        
        for n in nums:
            small = min(n, small)
            big = max(n, big)
            
        return small, big

arr = [
    [9],
    [3,4,5,5,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumSwaps(foo)
print(res)