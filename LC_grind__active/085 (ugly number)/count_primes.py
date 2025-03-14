import math

class Solution:
    def countPrimes(self, n: int) -> int:
        # this keeps track of all the non prime numbers
        non_primes = set()
        
        # if `n < 2`, append `0` and `1` to `non_primes`
        for i in range(min(2, n)):
            non_primes.add(i)

        # the idea is every number you encounter during this iteration should be a prime number
        # once you find a prime number, add all it's multiples to `non_primes`
        # say, i encounter `2`, i add all it's multiples up to `n` (2, 4, 6, ) in `non_primes`
        # such that when i encounter them in the iteration, i skip them
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if i in non_primes: continue

            self.add_multiples(i, n, non_primes)

        return n - len(non_primes)


    def add_multiples(self, unit, max_num, non_primes: set):
        start = unit * unit
        for num in range(start, max_num, unit):
            non_primes.add(num)

    
sol = Solution()
sol.countPrimes(10)