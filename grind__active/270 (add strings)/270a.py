# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # iterate backwards
        
        num1 = list(num1)
        num2 = list(num2)

        longest = len(num1) if len(num1) > len(num2) else len(num2)
        res = [0 for _ in range(longest + 1)]

        carry = 0
        idx = len(res) - 1
        while num1 and num2:
            dig1, dig2 = num1.pop(), num2.pop()

            dig1, dig2 = int(dig1), int(dig2)

            total = dig1 + dig2 + carry
            carry, val = divmod(total, 10)

            res[idx] = val
            idx -= 1

        while num1:
            dig = num1.pop()
            total = int(dig) + carry
            carry, val = divmod(total, 10)

            res[idx] = val
            idx -= 1

        while num2:
            dig = num2.pop()
            total = int(dig) + carry
            carry, val = divmod(total, 10)

            res[idx] = val
            idx -= 1

        if carry:
            res[idx] = carry

        return "".join(str(d) for d in (res[1:] if res[0] == 0 else res))
    
arr = [
    ["11", "123"],
    ["0", "0"],
    ["456", "77"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.addStrings(foo, bar)
print(res)

