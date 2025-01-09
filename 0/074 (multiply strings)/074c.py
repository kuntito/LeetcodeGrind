# https://leetcode.com/problems/multiply-strings/description/

# https://neetcode.io/solutions/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pass
        # if either number is zero, return zero
        if "0" in [num1, num2]:
            return "0"

        # `maxSlots` is an array representing the max number of digits
        # you could get after multiplying `num1` and `num2`
        maxSlots = [0] * (len(num1) + len(num2))
        
        
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                idx = i1 + i2
                maxSlots[idx] += digit
                
                quo, rem = divmod(maxSlots[idx], 10)
                
                maxSlots[i1 + i2 + 1] += quo
                maxSlots[i1 + i2] = rem
                

        maxSlots, beg = maxSlots[::-1], 0
        while beg < len(maxSlots) and maxSlots[beg] == 0:
            beg += 1
        maxSlots = map(str, maxSlots[beg:])
        return "".join(maxSlots)



arr = [
    ["5", "5"],
    ["123", "456"],
    # ["12", "5"],
    ["999", "999"],
    ["29", "22"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.multiply(foo, bar)
print(res)

