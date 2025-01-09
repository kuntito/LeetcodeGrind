# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = '0'
        if num1 == zero or num2 == zero:
            return zero
        
        arr = []
        last_idx = len(num1) - 1
        for idx in range(last_idx, -1, -1):
            n = num1[idx]

            places = last_idx- idx
            arr.append(
                self.run_through(n, num2) + ['0' for i in range(places)]
            )

        return str(sum(int(''.join(item)) for item in arr))


    def run_through(self, n, num2):
        carry = 0
        num2 = list(num2)
        for idx in range(len(num2) - 1, -1, -1):
            foo = int(n) * int(num2[idx])
            foo += carry

            carry, rem = divmod(foo, 10)
            num2[idx] = f'{rem}'

        return [f'{carry}'] + num2 if carry else num2



arr = [
    ["29", "22"],
    ["123", "456"],
    ["999", "999"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.multiply(foo, bar)

print(res)


