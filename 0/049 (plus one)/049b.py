# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 0
        last_idx = len(digits) - 1
        for idx in range(last_idx, -1, -1):
            n = digits[idx]

            if idx == last_idx:
                n += 1
            n += carry
            carry = 1 if n == 10 else 0            
            digits[idx] = n % 10
    
        return [1] + digits if carry else digits                




arr = [
    [9, 9],
    [1, 2, 3],
    [4, 3, 2, 1],
]
foo = arr[-1]

sol = Solution()
res = sol.plusOne(foo)
print(res)

