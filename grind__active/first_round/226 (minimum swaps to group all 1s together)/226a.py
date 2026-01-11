# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def minSwaps(self, data: list[int]) -> int:
        pass
    
        # find out the total number of 1s
        
        # find the window of size `total` with the most number of `1s`
        # return total - windowSize
        
        totalOnes = sum(1 for n in data if n)
        
        
        left = 0
        
        idx = 0
        count = 0
        while idx < totalOnes:
            n = data[idx]
            if n == 1:
                count += 1
            idx += 1
            
        maxCount = count
        
        for right in range(idx, len(data)):
            old = data[left]
            if old:
                count -=1
            
            neww = data[right]
            if neww:
                count += 1
                
            maxCount = max(count, maxCount)
            
            left += 1
            
        return totalOnes - maxCount
        
arr = [
    [1,0,1,0,1],
    [1,0,1,0,1,0,0,1,1,0,1],
    [0,0,0,1,0],
]
foo = arr[-1]
sol = Solution()
res = sol.minSwaps(foo)
print(res)