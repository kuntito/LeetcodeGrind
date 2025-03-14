# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations):
        record = []
        for op in operations:
            if self.is_digit(op):
                record.append(int(op))
            elif op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
        return sum(record)


    def is_digit(self, value):
        is_integer = False
        try:
            int(value)
            is_integer = True
        except ValueError:
            pass
        return is_integer
    

foo = Solution()
bar = ["5","2","C","D","+"]

res = foo.calPoints(bar)
print(res)