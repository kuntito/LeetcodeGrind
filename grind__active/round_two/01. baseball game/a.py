# https://leetcode.com/problems/baseball-game/description/

# it's a baseball game, we create an array, `record`
# we're given a list of strings called `operations`

# each operation, `operation[i]` is the ith operation i must apply to the record.
# not sure what ith operation means but okay..

# each operation is one of four things..
# an integer, is this an integer type int or a string version?, it's a string version

# back to operations, each operation is one of four things:
# an integer represented as a string i.e. "-5"
# a "+"
# a "D"
# a "C"

# if the op is an integer, add the integer to `record`

# if the op is a "+", add to `record`, the sum of the last two integers in `record`
#    i.e. `record.append(
#       record[-1] + record[-2]   
#    )`, we're guaranteed, there'd always be two previous integers whenever the operation is "+", unless of course, i've done sumn' wrong.

# if the op is "D", add to `record`, a score that's double of the previous
# i.e. `record.append(record[-1] * 2)`, again, we're guaranteed there'd be a previous score unless of course, i've done sumn' wrong.

# if the op is "C", remove the last score from `record` i.e. `record.pop()`
# we're guaranteed, a number would exist, unless, of course, i've done sumn' wrong.

# after all said and done, return `sum(record)`
# this suggests i'd have to convert the string representations to actual integers
# i actually should since, i'd be doing some calculations through out

# NB, str.isdigit() only considers 0-9 as digits.
# hence `"-2".isdigit()` would return False
# the better check is str.lstrip("-").isdigit
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        
        is_digit = lambda x: x.lstrip("-").isdigit()
        
        for op in operations:
            if is_digit(op):
                record.append(int(op))
            elif op == "+":
                record.append(
                    record[-1] + record[-2]
                )
            elif op == "D":
                record.append(
                    record[-1] * 2
                )
            elif op == "C":
                record.pop()
                
        return sum(record)
    
arr = [
    ["5","-2","4","C","D","9","+","+"],
]
foo = arr[-1]
sol = Solution()
res = sol.calPoints(foo)

print(res)