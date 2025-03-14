# https://leetcode.com/problems/remove-element/description/

class Solution:
    def find_next_val(self, pos, val, arr):
        while (pos < len(arr) and arr[pos] != val):
            pos += 1

        return pos


    def swap(self, idxOne, idxTwo, arr):
        temp = arr[idxOne]
        arr[idxOne] = arr[idxTwo]
        arr[idxTwo] = temp


    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0: return 0

        uno = self.find_next_val(0, val, nums)
        for dos in range(uno + 1, len(nums)):
            if nums[dos] != val:
                self.swap(uno, dos, nums)
                uno = self.find_next_val(uno, val, nums)
        
        return uno
        

foo = Solution()

nums = [3, 2, 2, 3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

nums = [2]
val = 3

res = foo.removeElement(nums, val)
print(res)

