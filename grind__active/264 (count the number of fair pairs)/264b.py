# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        pass
        # for each number, you want to know how many numbers it can combine with
        # to be within in range
        
        # itself is included in the range of numbers
        
        # makes sense to get a unique set of numbers
        # so we avoid repeated work
        # hence use a hash map to summarize the `nums`
        
        # run through each element in the hashmap
        # does this mean for each element, we'd check every other element?
        
        # am i over complicating things,
        # let me attempt the bruteforce
        # grab every pair and compare
        
        # TODO
        # bruteforce takes too long, TLE
        nums.sort()
        dim = len(nums)
        
        cache = {}
        
        res = 0
        for i in range(dim):
            n1 = nums[i]
            if n1 in cache:
                res += cache[n1]
                continue
            
            count = 0
            for j in range(i + 1, dim):
                n2 = nums[j]
                total = n1 + n2
                if lower <= total <= upper:
                    count += 1
                    
            cache[n1] = count
            res += count
                    
            
        return res
        

        
arr = [
    [[0,1,7,4,4,5], 3, 6],
    [[1,7,9,2,5], 11, 11],
    [[0, 0, 0, 0, 0, 0], 0, 0],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.countFairPairs(foo, bar, baz)
print(res)