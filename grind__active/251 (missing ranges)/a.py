# https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        pass
        # get the range of `nums` that fits in `lower` and `upper`
        
        
        # # move start to the first element that's >= `lower`
        # start = 0
        # while start < dim and nums[start] < lower:
        #     start += 1
            
        # # end might not need a range
        # # `end = upper` 

        
        # redefine nums to start with `lower-1`
        arr = [lower-1]
        for n in nums:
            if n < lower:
                continue
            arr.append(n)
            if n > upper:
                break
            
        arr.append(upper+1)
        
        res = []
        dim = len(arr)
        for idx in range(1, dim):
            # you have an interval, when there's a gap between numbers
            # if prev+1 != curr
            # interval
            
            prev = arr[idx - 1]
            curr = arr[idx]
            if prev + 1 != curr:
                res.append(
                    [prev+1, curr-1]
                )
        
        return res
            
arr = [
    [[0,1,3,50,75], 0, 99],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.findMissingRanges(foo, bar, baz)
print(res)