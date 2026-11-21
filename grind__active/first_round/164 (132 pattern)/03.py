class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        curMin = nums[0]
        
        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()
                
            if stack and n > stack[-1][1] and n < stack[-1][0]:
                return True
            
            if not stack:
                stack.append([n, curMin])
            curMin = min(curMin, n)
            
        return False
            
            
    
arr = [
    [3,1,4,2],
    [1, 2, 3, 4],
    [3,4,3,1,2],
]
sol = Solution()
foo = arr[-1]
res = sol.find132pattern(foo)
print(res)