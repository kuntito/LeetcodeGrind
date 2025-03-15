# https://leetcode.com/problems/contiguous-array/description/

# TODO consider all possibilities if neither shift improves imbalance?
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        pass
        # create a counter for all zeros and ones
        # then create two pointers, left and right
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        # you can either increment left or decrement right
        # the decision is based on whichever one decreases the imbalance
        dim = len(nums)
        left = 0
        right = dim - 1
        
        if 0 not in counter:
            return 0
        
        if 1 not in counter:
            return 0
        
        while counter[0] != counter[1]:
            pass
            currImbalance = abs(counter[0] - counter[1])
            
            leftNum = nums[left]
            rightNum = nums[right]
            
            # if you take out the left what happens to the imbalance
            leftImbalance = abs(
                (counter[leftNum] - 1) -
                counter[rightNum]
            )
            
            # if you take out the right what happens to the imbalance
            rightImbalance = abs(
                counter[leftNum] +
                (counter[rightNum] - 1)
            )
            
            if leftImbalance < currImbalance:
                left += 1
                counter[leftNum] -= 1
            else:
                right -= 1
                counter[rightNum] -= 1
                
        return (right - left) + 1

arr = [
    [0, 1],
    [0,1,0],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [1,1,1,1,1,1,1,1],
    [0,1,1,0,1,1,1,0],
]
foo = arr[-1]
sol = Solution()
res = sol.findMaxLength(foo)

print(res)
