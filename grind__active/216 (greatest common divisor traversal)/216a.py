# https://leetcode.com/problems/greatest-common-divisor-traversal/description/

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        pass
        # create a graph based on gcd
        # compare each element with subsequent elements
        # that are not equal to itself
        # if they have a gcd, they should be neighbours in the undirected graph
        graph = self.get_graph(nums)
        for k, v in graph.items():
            print(k, '=>', v)
        
        # determine all the pairs
        
        # find if a path exists between each pair
        
    def get_graph(self, nums):
        dim = len(nums)
        graph = {}
        
        for i in range(dim):
            graph[i] = []
        
        for i in range(dim):
            for j in range(i + 1, dim):
                numOne = nums[i]
                numTwo = nums[j]
                if numOne == numTwo: continue
                
                if self.has_gcd(numOne, numTwo):
                    graph[i].append(j)
                    graph[j].append(i)
                    
        return graph
    
    def has_gcd(self, numOne, numTwo):
        pass
        # check every number from (2, sqrt(smallerNum))
        # since the smallest number of a non-prime number is at most it's square root
        
        # using this check if any factors of `smallerNum`
        # exist in `largerNum`
        # if yes, return True
        
        # else False
        
arr = [
    [2,3,6],
]
foo = arr[-1]
sol = Solution()
res = sol.canTraverseAllPairs(foo)