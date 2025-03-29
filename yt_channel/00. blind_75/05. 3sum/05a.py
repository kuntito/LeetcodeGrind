# https://leetcode.com/problems/3sum/

from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass
        # the problem asks for an array of triplets
        # a triplet is an array of three numbers that sum up to zero
        # essentially, we'd be returning a 2d array
        
        # the caveat is that each number in the triplet should be unique indices
        # and all triplets should be unique
        
        # say i have a triplet with indices [0, 1, 2]
        # i can't have anothe triplet with indices [2, 0, 1]
        # since they are essentially the same indices just reordered
        
        # based on i've done this before
        # the idea would be to iterate through `nums`
        # for each number, explore the rest of the array for two numbers that negate that number
        
        # for instance, if `nums = [2, -1, 3, -1]`
        # the first number is `2`
        # this means, we need two numbers in the rest of the array `nums[1:]`
        # such that both numbers sum up to `-2` and have unique indices
        
        # FIXME i know we have to sort the array
        # but i'm not sure why
        # i'd do it without sorting, and figure out why it doesn't work
        
        threeSums = []
        for idx, n in enumerate(nums):
            complement = -n
            # now we need all the two sums
            twoSums = self.getTwoSums(complement, nums[idx + 1:])
            for ts in twoSums:
                threeSums.append(
                    [n, *ts]
                ) # TODO why does it return the duplicates?
                
        return threeSums
    
    # TODO how does two sum ii two pointer approach work?
    def getTwoSums(self, target, arr):
        pass
        # we need all pairs of numbers in `arr`
        # that add up to target
        # store them all in `twoSums`

        # my idea is to make a counter from `arr`
        # then iterate through each unique element in `arr`
        # determine it's complement
        # if it's complement exists, we'd have to find the different ways, we can select a pair from their frequencies
        
        # FIXME, this would need some explaining but it's simply multiplying their frequencies
        
        # remove each number and complement from the counter
        # even if you don't find the complement, still remove the number
        # since it means, no other number would combine with it to form `target`
        twoSums = []
        
        counter = Counter(arr)            
        
        for n in arr:
            # for each `n`, decrement it's count from the counter
            # for instance, [0, 0, 0] and target = 0
            # would have a complement of `0`
            # this would mean the total combinations is:
            # counter[0] * counter[0] = 3 x 3 which would result in `9`
            
            # so we should decrement each `n`
            counter[n] -= 1
            
            complement = target - n
            if complement in counter:
                totalCombinations = counter[complement]
                for _ in range(totalCombinations):
                    twoSums.append([n, complement])
                
            if counter[n] == 0:
                del counter[n]
            
        return twoSums

arr = [
    [-1,0,1,2,-1,-4],
]
foo = arr[-1]
sol = Solution()
res = sol.threeSum(foo)
print(res)