# https://leetcode.com/problems/integer-to-roman/description/

from collections import deque


class Solution:
    def intToRoman(self, num: int) -> str:
        self.int_to_roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        pass
        # might make sense to iterate in reverse
        # for each position, determine what unit the number is
        # i.e. thousands, hundreds, tens, units?

        # for num in reverseNum
        # for each passing num, increase the exponent of zero
        # num * (10 ** exp)
        # this way we know what position each number is

        # also, if a number is zero, ignore it and move on to the next number
        # i.e. 50

        # iterating in reverse would be 0 -> 5
        # but we'd skip zero and move on to `5` which would be `5 * 10**1`

        # for each number modified by it's exponent, we convert to roman numeral

        res = deque()
        exp = 0

        # while num:
        #     num, dig = divmod(num, 10)
        #     if dig > 0:
        #         dig * 10 ** exp
        #         digToRoman = self.getRoman(dig)
        #         res.appendleft(digToRoman)
        #     exp += 1

        num_str = str(num)
        for n in num_str[::-1]:
            romanN = self.getRoman(n, 10**exp)
            # print(romanN)
            res.appendleft(romanN)
            exp += 1

        return "".join(res)

    def getRoman(self, num_str, unit):
        if num_str == '0':
            return ""
        # if you have 30, i know the units is 10
        # if 30 // 10 < 4:
        # then get roman[10] * 3
        # where `3` == 30//10

        # if you have 40, i know the units is 10
        # it starts with a `4` so i get roman[40 + 10]
        # L
        # and i precede it with the value for 10, X
        # anything that starts with four, add it's unit
        # get the roman equivalent of the new value
        # then precede it's unit
        first_dig = num_str[0]
        if first_dig in ("4", "9"):
            pass
            num = int(num_str)
            num *= unit

            nextNum = num + unit
            # print(nextNum)
            
            romanNext = self.int_to_roman[nextNum]
            romanUnit = self.int_to_roman[unit]
            return romanUnit + romanNext
        
        if int(first_dig) < 4:
            return self.int_to_roman[unit] * int(first_dig)
        
        mids = unit * 5
        secondPart = str((int(num_str) * unit) - mids)
        return self.int_to_roman[mids] + self.getRoman(secondPart, unit)

        # what about 60?
        # well, it's previous value is `50`
        # get's it's roman value `50 = L`
        # subtract 50 from 60 to get 10
        # call self.getRoman on `10`, get `X`
        # append the `X` to `L` to form `LX`


arr = [
    3749,
    53,
    1994,
]
foo = arr[-1]
sol = Solution()
res = sol.intToRoman(foo)
print(res)