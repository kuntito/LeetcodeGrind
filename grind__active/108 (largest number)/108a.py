# https://leetcode.com/problems/largest-number/description/

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        pass
    
        # create an array of 10 slots, each slot is an empty list
        slots = [[] for _ in range(10)]
        
        # iterate through nums, convert each number to a string
        for n in nums:
            num_string = str(n)            
            # the first digit represents the slot index
            # int(num[0])
            idx = int(num_string[0])
        
            # place in it's slot
            slots[idx].append(num_string)
            
        
        res = []
        # iterate through all slots from behind
        for idx in range(9, -1, -1):
            container = slots[idx]
            container.sort(key=lambda x: (len(x), -int(x)))

            res.extend(container)
        # sort the list by length of each string and the string it's self
        # so 9 -> 91 -> 92
        
        return "".join(res)
        
        
arr = [
    [10, 2],
    [3,30,34,5,9],
]
foo = arr[-1]
sol = Solution()
res = sol.largestNumber(foo)
print(res)