# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        pass
        # sliding window of size `k`
        # update the average as you slide through dem dms
        # keep track of how many averages is >= threshold
        dim = len(arr)
        
        currTotal = sum(arr[:k])
        res = 1 if (currTotal/k) >= threshold else 0
    
        for idx in range(k, dim):
            prev = arr[idx-k]
            curr = arr[idx]
            
            currTotal += curr
            currTotal -= prev
            
            if (currTotal / k) >= threshold:
                res += 1
                
        return res

arr = [
    [[2,2,2,2,5,5,5,8], 3, 4],
    [[11,13,17,23,29,31,7,5,2,3], 3, 5],
]
foo, bar, zar = arr[-1]
sol = Solution()
res = sol.numOfSubarrays(foo, bar, zar)
print(res)