# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        pass
        # two pointers, `left` and `right`
        # two variables, `leftValue` and `rightValue`
        
        # if the left value and right value are different
        # move the pointer with the lesser value forward
        # and update it's value based on the value at it's new position
        
        # i.e. 1, 2, 3
        # in this case, left value is `1` and right value is `3`
        # if you move the left pointer forward, update the value to `1 + 2`
        # now left value is `3`
        # the values are equal, so you can move the pointers closer
        # the iteration ends, when the pointers meet or cross each other
        
        # you don't actually have to add the values in the array
        # just simulate the addition
        
        # use a variable `count` to track whenever the left value != right value
        
        dim = len(nums)
        left, right = 0, dim - 1
        
        count = 0
        while left < right:
            leftValue = nums[left]
            rightValue = nums[right]
            
            while leftValue != rightValue and left < right:
                count += 1
                if leftValue < rightValue:
                    left += 1
                    leftValue += nums[left]
                else:
                    right -= 1
                    rightValue += nums[right]
            
            
            left += 1
            right -= 1
            
        return count
            
arr = [
    [4,3,2,1,2,3,1],
    [1,2,3,4],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumOperations(foo)
print(res)