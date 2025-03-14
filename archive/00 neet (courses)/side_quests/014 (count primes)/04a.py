# https://leetcode.com/problems/count-primes/
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        non_primes = set()
        for i in range(min(2, n)):
            non_primes.add(i)

        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if i in non_primes: continue

            self.get_count_of_multiples(i, n, non_primes)

        return n - len(non_primes)


    def get_count_of_multiples(self, unit, max_num, non_primes: set):
        count = 0
        start = unit * unit
        for num in range(start, max_num, unit):
            non_primes.add(num)
            count += 1

        return count
    

arr = [
    5_000_000,
    10,
]
foo = arr[-1]
sol = Solution()
res = sol.countPrimes(foo)
print(res)

# for n in range(2, 10, 2):
#     print(n)
