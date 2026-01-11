# https://leetcode.com/problems/greatest-common-divisor-traversal/description/


from collections import defaultdict

#  TODO TLE, you're onto something
# how can you optimize for a large array
# is the bruteforce the best way
# also, handle 1s i.e [1, 1] and [1]?
# a singleton with `1` is fine, a non-empty set with `1` is not
# technically, `len(nums) < 2` should return True
class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        pass
        # you can move between indices, if their values have a gcd > 1
        # determine every pair of indices, nC2 ish
        
        # it's looking like a graph problem
        # when you determine all possible pairs (a, b)
        # you want to find out, if you can go from a -> b
        
        # we'd have to construct a graph
        # the graph would be such that every value `nums[i]`
        # has neighbours with gcd > 1
        
        # step one is building the graph
        # consider [2, 3, 6]
        # how do i know all of `2`s neighbours
        
        # it's looking like an n2 type thing
        # i'd go through every number after `2` and check for a gcd
        
        # i think we should only care about unique numbers
        # consider: [2, 2]
        
        
        # rather than the nsquared approach for the graph
        # use prime numbers for the graph
        # the gcd looks like a red herring
        
        # what we want to know is if two numbers have a common factor
        # i.e. 6, 12
        # the gcd would be 6 but the LCM is `2`
        # if an LCM exists, we can extend the logic that a gcd exists
        
        # using prime numbers we can run through all prime numbers
        # determine the prime number range
        # 2 -> max(nums)
        # use that erastothenes thingy
        
        maxNum = max(nums)
        primes = self.primes_up_to(maxNum)
        
        # once we have the primes
        # create a set from `nums`, `numset`
        # while numset:
        # for each prime number 
        # run through the set and grab it's multiples
        # and remove any
        numset = set(nums)
        if 1 in numset and len(nums) > 1:
            return False
        primeMultiples = defaultdict(list)
        
        for p in primes:
            for num in numset:
                if num % p == 0:
                    primeMultiples[p].append(num)


        # for k,v in primeMultiples.items():
        #     print(f'{k} => {v}')

        graph = self.create_graph(primeMultiples)
        
        # for k,v in graph.items():
        #     print(f'{k} => {v}')
        # return
        # store the prime number and multiples in a hashmap
        # that hashmap contains all the connections
        
        
        # i.e. for [2, 3, 6]
        
        # {
        # 2 -> [2, 6],
        # 3 -> [3, 6]
        # }
        
        # this way, i know 2 can go to 6
        # and 6 can go to three
        
        # once we have the graph, we want to know if all the components are connected
        # remove explored numbers from numset
        self.explore(nums[0], graph, numset)
        
        # if 1 in numset:
        #     numset.remove(1)
        
        return not numset
    
    def explore(self, num, graph, numset):
        # if num not in numset:
        #     return
        numset.remove(num)
        
        for nei in graph[num]:
            if nei in numset:
                self.explore(nei, graph, numset)
        
    def create_graph(self, multiples):
        graph = defaultdict(list)
        
        for arr in multiples.values():
            dim = len(arr)
            for idx in range(dim):
                uno = arr[idx]
                for j in range(idx + 1, dim):
                    dos = arr[j]
                    graph[uno].append(dos)
                    graph[dos].append(uno)
                    
        return graph
        
    def primes_up_to(self, n):
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]
        
arr = [
    [2,3,6],
    [4,3,12,8],
    [3,9,5],
    [42,40,45,42,50,33,30,45,33,45,30,36,44,1,21,10,40,42,42],
]
foo = arr[-1]
sol = Solution()
res = sol.canTraverseAllPairs(foo)
print(res)

