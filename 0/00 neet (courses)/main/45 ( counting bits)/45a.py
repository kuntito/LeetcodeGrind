# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, n: int) -> list[int]:
        arr = []

        for num in range(n+1):
            arr.append(self.get_bit_count(num))

        return arr
    
    def get_bit_count(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
    
foo = [
    2,
    5,
]
bar = foo[-1]

sol = Solution()
res = sol.countBits(5)

print(res)