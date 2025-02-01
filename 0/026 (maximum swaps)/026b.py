# https://leetcode.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        pass
        num_arr = [int(dig) for dig in str(num)]
        
        # create an array, `arr`
        # such that each index, `arr[i]` contains
        # the largest number after `i` and it's index
        largestSoFar = self.get_largest(num_arr)
        # print(largestSoFar)
        
        for idx, num in enumerate(num_arr):
            memo_item = largestSoFar[idx]
            if memo_item:
                largeNum, largeNumIdx = memo_item
                if largeNum > num:
                    num_arr[idx], num_arr[largeNumIdx] = num_arr[largeNumIdx], num_arr[idx]
                    break
                
        return self.convert_to_int(num_arr)
    
    
    def convert_to_int(self, arr):
        dim = len(arr)
                
        res = 0
        for idx, n in enumerate(arr):
            unit = dim - (idx + 1)
            n = n * (10 ** unit)

            res += n
            
        return res

        
    def get_largest(self, arr):
        pass
        # iterate backwards keeping track of the largest number you've seen
        
        dim = len(arr)
        res = [None for _ in range(dim)]
        largestSoFar = (arr[-1], dim - 1)
        
        for idx in range(dim-2, -1, -1):
            num = arr[idx]
            largeNum, largeNumIdx = largestSoFar
            
            if largeNum > num:
                res[idx] = largestSoFar
                
            if num > largeNum:
                largestSoFar = (num, idx)
                
        return res
                  

arr = [
    9973,
    2736,
]
foo = arr[-1]
sol = Solution()
res = sol.maximumSwap(foo)
# res = sol.convert_to_int([3, 1, 2])
print(res)