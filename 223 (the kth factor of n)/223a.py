# https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        
        for i in range(1, n//2 + 1):
            if n % i == 0:
                count += 1
            if count == k:
                return i
            
        # the loop only iterates to the middle of `n`
        # this condition handles the scenario where the kth factor is `n`
        return -1 if count + 1 < k else n
    
arr = [
    [7, 2],
    [4, 4],
    [12, 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.kthFactor(foo, bar)
print(res)
    