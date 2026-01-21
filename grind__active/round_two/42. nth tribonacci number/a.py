# https://leetcode.com/problems/n-th-tribonacci-number/description/

# i want to find the nth tribonacci number
# what's a tribonacci number?

# the number in a tribonacci sequence
# what's that, it's a sequence of numbers where each number is the sum
# of the last three number in the sequence..

# naturally the sequence has it's first three number predefined..
# i.e.
# 0, 1, 1
# so the fourth tribonnaci number is 0 + 1 + 1
# in our case, `2`

# so, how would this work..
# question says `n` can be at lowest, `0`

# so if `n` is `0`, my guess is tribonacci number is `0`
# i'd hard code the base cases..

# if n <= 1 return 0
# if n <= 3 return 1

# now the trib itself, i'd use a for loop to manually update the last three numbers
# how would that work

# i'd set:
# first, second, third =>
# 0, 1, 1

# then run a for loop `n - 3` times
# for each iteration..
# i'd sum `first + second + third` as the current nth tribonacci number

# then update the pointers..
# third = current number
# second = third
# first = second

# until we exhaust the loop
# at which point, it's calm, innit..

# two errors, one tribonacci starts from `0`
# yes, 0, 1, 1..
# no, not that.. following this logic, the third tribonacci number is `1`
# but the examples given, show it isn't

# the third tribonacci number is `3`
# the sequence is 0, 1, 1, 2

# trib(0) = 0
# trib(1) = 1
# trib(1) = 1
# trib(2) = 2

# ergo, we shouldn't do `range(n-3)`
# it should be `range(n-2)`

# that said, my order of updating the last three numbers was wrong.
# i'd written:
# third = current number
# second = third
# first = second

# but with this, once i do.. `second = third`
# i no longer have access to `second`

# so when i do `first = second`
# i'm actually doing `first = third`

# even still, when i do `third == current_trib`
# i lose access the original third..

# so how should this go..
# i know, current_trib would be third, so i can leave that as-is
# for first and second..
# i know second wants to become third..
# but first has to become second first..

# so:
# first = second
# second = third
# third = current_trib

# error, i had to update the base case checks
# since the trib sequence starts counting at zero.. not one
# i'd previously written:

# if n <= 1: return 0
# if n <= 3: return 1

# which isn't True, since, the sequence is..
# 0, 1, 1, 2..
# fib0 = 0, fib1 =1, fib2 = 1
# fib3 = fib0 + fib1 + fib2 = 0 + 1 + 1 = 2

# the correct base case checks are:
# if n == 0: return 0
# if n <= 2: return 1
 

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        first, second, third = 0, 1, 1
        
        for _ in range(n - 2):
            current_trib = sum([first, second, third])
            first = second
            second = third
            third = current_trib
            
            
        return current_trib        
    
arr = [
    4,
]
foo = arr[-1]
sol = Solution()
res = sol.tribonacci(foo)
print(res)