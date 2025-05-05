# https://leetcode.com/problems/3sum-closest/description/

# TODO i think it works but takes too long
# i'm thinking something along the lines of binary search
# or can we optimize this function as is
# which part is taking time??
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        pass
        # what does it mean to be close to the target
        # it's giving sliding window
        
        # forget sliding window, let's build our way up
        # what does it mean to find two numbers that are closest to a target?
        
        # say we sort the array
        # and pick the first and last elements
        
        
        # i don't know about this
        # how about we invert the problem
        # find three numbers in `nums` that add up to target
        # if it can't be found
        
        # find three numbers in `nums` that add up to `target - 1`
        # find three numbers in `nums` that add up to `target + 1`
        
        # and repeat until we hit the a result
        
        # so how would you find two numbers that sum up to target
        # well this is a three sum problem
        
        # for each number, determine it's complement
        # for each complement, explore the array for two numbers that make it up
        nums.sort()
        
        decr = 0
        while True:
            one = self.hasThreeSum(target + decr, nums)
            if one:
                return target + decr
            
            two = self.hasThreeSum(target - decr, nums)
            if two:
                return target - decr
            decr += 1
        
    def hasThreeSum(self, target, nums):
        for idx, n in enumerate(nums):
            complement = target - n
            if self.hasTwoSum(complement, nums[idx + 1:]):
                return True
        
        return False
    
    def hasTwoSum(self, target, arr):
        # the array is sorted
        left, right = 0, len(arr)-1
        
        while left < right:
            leftNum, rightNum = arr[left], arr[right]
            
            total = leftNum + rightNum
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return True
            
        return False    
            
arr = [
    [[-1,2,1,-4], 1],
    [[0,0,0], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.threeSumClosest(foo, bar)
print(res)