# https://leetcode.com/problems/subarrays-with-k-different-integers/

from typing import List


class Solution:
    def subarraysWithKDistinct(
        self,
        nums: List[int],
        k: int
    ) -> int:
        pass
    
        # it's best to use a hash map for uniques
        # since, i'd be removing elements.
        # 
        # so when duplicates exist, removing an element
        # simply means decrementing it's counter in the hash map.
        uniques = {}
        
        startIdx = 0
        valid_subarr_count = 0
        for n in nums:
            uniques[n] = uniques.get(n, 0) + 1

            while len(uniques) > k:
                curStartNum = nums[startIdx]
                uniques[curStartNum] -= 1
                
                if uniques[curStartNum] == 0:
                    del uniques[curStartNum]
                
                startIdx += 1
            
            if len(uniques) == k:
                valid_subarr_count += 1
                valid_subarr_count += self.explore_recursive_shrink(
                    startIdx,
                    nums,
                    uniques,
                    k
                )
                
        return valid_subarr_count
            
                
    def explore_recursive_shrink(self, startIdx, nums, uniques, k):
        # what do i want to do?
        # remove the element at start index
        # if len of uniques is still equal to `k`
        # you'd have to increment count
        # however, i'm not doing a global increment
        # rather, i'm returning the increment and leaving the parent call
        # to increment count
        
        incr = 0
        
        n = nums[startIdx]
        uniques[n] -= 1
        if uniques[n] == 0:
            del uniques[n]
            
        if len(uniques) == k:
            incr += 1
        
            incr += self.explore_recursive_shrink(
                startIdx + 1,
                nums,
                uniques,
                k
            )
        
        # but keep in mind after the recursion, i want to re-add the removed number.
        uniques[n] = uniques.get(n, 0) + 1
        
        return incr
        
        
arr = [
    [[1, 2, 3], 2],
    [[1, 2, 1, 2, 3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.subarraysWithKDistinct(foo, bar)
print(res)