# https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        pass
        dim = len(nums)
        target_freq = (dim // 3) + 1

        # sort the array
        # keep a `streak` of each element
        # if the `streak` == `target_freq`
        # append that element to `res`
        res = []
        
        nums.sort()
        prev = None
        
        streak = 0
        idx = 0
        while idx < dim:
            curr = nums[idx]
            if prev is None:
                prev = curr
                
            if curr == prev:
                streak += 1
            else:
                streak = 1
                prev = curr
            
            if streak == target_freq:
                res.append(curr)
                while idx + 1 < dim and nums[idx + 1] == curr:
                    idx += 1    
                streak = 0
                prev = None
            
            idx += 1
    
        return res


arr = [
    [3,2,3],
    [1],
    [1,2],
    [4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]
foo = arr[-1]
sol = Solution()

res = sol.majorityElement(foo)
print(res)