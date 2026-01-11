# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

# TODO, zero might be an edge case
# expanding forwards should work for every other number
from collections import Counter
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        pass
        # for each number, you want to know how many numbers it can combine with
        # to be within in range
        
        # itself is included in the range of numbers
        
        # makes sense to get a unique set of numbers
        # so we avoid repeated work
        # hence use a hash map to summarize the `nums`
        
        # run through each element in the hashmap
        # does this mean for each element, we'd check every other element?
        
        counter = Counter(nums)
        lst = sorted(list(counter))
        dim = len(lst)
        
        res = 0
        graph = {}
        for i in range(dim):
            numOne = lst[i]
            if numOne in graph: continue
            
            graph[numOne] = []
            # if numOne has multiples TODO
            if lower <= numOne * 2 <= upper:
                n = counter[numOne] - 1
                res += (n * (n + 1))// 2
            
            for j in range(i + 1, dim):
                numTwo = lst[j]
                
                total = numOne + numTwo
                if lower <= total <= upper:
                    graph[numOne].append(numTwo)
        
        
        for numOne, lst in graph.items():
            for numTwo in lst:
                countOne, countTwo = counter[numOne], counter[numTwo]
                res += (countOne * countTwo)


        return res        

        
arr = [
    [[0, 0, 0, 0, 0, 0], 0, 0],
    [[1,7,9,2,5], 11, 11],
    [[0,1,7,4,4,5], 3, 6],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.countFairPairs(foo, bar, baz)
print(res)