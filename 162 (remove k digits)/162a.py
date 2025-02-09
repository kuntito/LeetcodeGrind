# https://leetcode.com/problems/remove-k-digits/description/

import heapq
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        pass
        # convert `num` to an array of numbers
        # if you take out `k` numbers from the array,
        # you'd have `l` numbers left, let's call that `win_size`
        
        # create a minHeap that stores the numbers and indices
        # append the first `win_size` numbers
        # take out the smallest number
        # append it to res
        # remove all elements in the heap that have indexes before the smallest number
        # update k -= 1
        # update `win_size = len(what's left of num_arr - k - 1)`
        
        num_arr = [int(n) for n in str(num)]
        
        
        res = []
        minHeap = []
        
        dim = len(num_arr)
        idx = 0
        smallestIdx = 0
        while k >= 0:        
            while idx < dim and dim - idx >= k:
                heapq.heappush(minHeap, (num_arr[idx], idx))
                idx += 1
        
            while minHeap and minHeap[0][1] < smallestIdx:
                heapq.heappop(minHeap)

            smallest, smallestIdx = heapq.heappop(minHeap)
            res.append(smallest)
            print(res)
            k -= 1
        
        return res
    
arr = [
    ["1432219", 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.removeKdigits(foo, bar)
print(res)
                        