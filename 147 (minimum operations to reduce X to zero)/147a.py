# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        pass
        # recursively, check leftMost and rightMost
        slice_len = self.explore(nums, x)
        if slice_len == -1:
            return -1
        
        return len(nums) - slice_len

    # this function returns the size of the slice of the arr left
    # after target is found
    def explore(self, arr, target):
        if target == 0:
            return len(arr)
        if target < 0 or not arr:
            return -1
        
        leftMost = arr[0]
        rightMost = arr[-1]
        
        if len(arr) == 1:
            return 0 if leftMost == target else -1

        # if left is bigger, do left then right
        if leftMost > rightMost:
            res = self.explore(arr[1:], target - leftMost)
            if res >= 0: return res
            return self.explore(arr[:-1], target - rightMost)


        # if right is bigger or equal, do right then left
        res = self.explore(arr[:-1], target - rightMost)
        if res >= 0: return res
        return self.explore(arr[1:], target - leftMost)
            
        
        
arr = [
    [[6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119], 31841],
    [[3,2,20,1,1,3], 10],
    [[5,6,7,8,9], 4],
    [[1,1,4,2,3], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minOperations(foo, bar)
print(res)