# https://leetcode.com/problems/two-sum/description/

from collections import defaultdict, deque
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
        # to find two numbers that add up to the target
        # we might have to explore every number
        
        # the idea here is to iterate through `nums`
        # for every number, `n`
        # determine it's `complement = target - n`
        # we want to check if the `complement` exists in the array
        
        # why can't you run a counter on `nums`
        # iterate through `nums` again
        # this time, for each number, decrement it's counter
        # if the value hits `0`, remove that element from the counter
        
        # determine the `complement` of that number
        # if it exists in the array, return the indices

        # this won't work because you need the indices
        
        # a regular hash map wouldn't work since you need the indices of each value
        # what if we appended indices, rather than track the count
        
        # and rather than decrement the count, we popped left
        # the hashmap would store (value => deque(indices))
        # if the deque every becomes empty
        # remove from the hashmap
        
        # calculate the complement
        # if it exists in the hashmap, grab the index from the queue
        counter = defaultdict(deque)
        
        for idx, n in enumerate(nums):
            counter[n].append(idx)
            
        for n in nums:
            idx = self.removeIndex(counter, n)
            
            complement = target - n
            if complement in counter:
                idxTwo = self.removeIndex(counter, complement)
                
                return [idx, idxTwo]
    
    def removeIndex(self, counter, value):
        idx = counter[value].popleft()
        if not counter[value]:
            del counter[value]
            
        return idx
    
arr = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3, 3], 6]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.twoSum(foo, bar)
print(res)