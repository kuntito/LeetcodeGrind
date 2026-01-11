# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pass
        # create a counter
        
        # run through the unique element in nums
        # in increasing order
        # for each num, check if num + k exists in counter
        
        # if yes, increment `kCount` by the frequency of `(num + k) * frequency of num`
        
        counter = Counter(nums)
        
        order = sorted(list(counter))
        
        k_count = 0
        for num in order:
            partner = num + k
            if partner in counter:
                k_count += (counter[num] * counter[partner])
                
        return k_count
    
arr = [
    [[3, 2, 1, 5, 4], 2],
    [[1,2,2,1], 1],
    [[1,3], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countKDifference(foo, bar)
print(res)