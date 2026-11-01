from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        self.longest = 0
        self.nums = nums
        
        arr = []
        startIdx = 0
        
        self.explore(arr, startIdx)
        
        return self.longest

    def explore(self, arr, idx):
            dim = len(self.nums)
            if idx == dim:
                if len(arr) > self.longest:
                    self.longest = len(arr)
                return
            
            curNum = self.nums[idx]
            if not arr or arr[-1] >= curNum:
                arr.append(curNum)
                self.explore(arr, idx + 1)
                arr.pop()
            else:
                self.explore(arr, idx + 1)

                cloneArr = arr[::]                
                while cloneArr and cloneArr[-1] < curNum:
                    cloneArr.pop()
                    
                cloneArr.append(curNum)
                self.explore(cloneArr, idx + 1)
                


arr = [
    [16,6,3],
    [6,5,3,4,2,1]
]
foo = arr[-1]
sol = Solution()
res = sol.longestSubsequence(foo)
print(res)