# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        pass
        # create a temp, `arr`
        # this appends each `n` in `nums`
        # if `nums[idx-1] + 1 != nums[idx]` 
        # concatenate the array content to string
        # append to res
        # clear the array
        
        res = []
        arr = []
        for idx, n in enumerate(nums):
            if idx > 0 and (nums[idx-1] + 1 != n):
                res.append(self.get_string(arr))
                arr.clear()
            
            arr.append(n)
            
        res.append(self.get_string(arr))
        
        return res
    
    def get_string(self, arr):
        return f"{arr[0]}->{arr[-1]}" if len(arr) > 1 else str(arr[0])
    
arr = [
    [0,1,2,4,5,7],
    [0,2,3,4,6,8,9],
]
foo = arr[-1]
sol = Solution()
res = sol.summaryRanges(foo)
print(res)