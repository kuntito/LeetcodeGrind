# https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        sublist, self.master = [], []

        nums.sort()
        self.nums = nums
        self.explore(0, sublist)

        return self.master
    
    def explore(self, idx, sublist):
        if idx == len(self.nums):
            self.master.append(sublist.copy())
            return

        item = self.nums[idx]
        sublist.append(item)
        self.explore(idx + 1, sublist)
        sublist.pop()



        while idx < len(self.nums) and self.nums[idx] == item:
            idx += 1
        self.explore(idx, sublist)
        
arr = [
    [0],
    [1,2,2],
    [4,4,4,1,4],
]
foo = arr[-1]
sol = Solution()
res = sol.subsetsWithDup(foo)

for row in res:
    print(row)