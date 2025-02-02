# https://leetcode.com/problems/k-th-symbol-in-grammar/description/

# TODO https://neetcode.io/solutions/k-th-symbol-in-grammar
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        pass
        hashmap = {
            0:[0, 1],
            1:[1, 0],
        }
        
        arr = [0]
        for i in range(1, n):
            tmp = []
            for ch in arr:
                tmp.extend(
                    hashmap[ch]
                )
                
            arr = tmp
            print(arr)
            
        return arr[k-1]
        
arr = [
    [1, 1],
    [2, 1],
    [2, 2],
    [5, 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.kthGrammar(foo, bar)
print(res)