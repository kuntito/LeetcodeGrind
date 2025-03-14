# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [None for i in range(3)]

        for n in nums:
            if bucket[n] is None:
                bucket[n] = 0
            bucket[n] += 1

        print(bucket)

        idx = 0
        for item, freq in enumerate(bucket):
            if freq is None: continue
            for _ in range(freq):
                nums[idx] = item
                idx += 1

        return nums

    def sortColorsII(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]    
    
    
        start = 0
        end = len(nums) - 1

        idx = 0
        while idx <= end:
            num = nums[idx]
            if num == 0:
                swap(idx, start)
                start += 1
            elif num == 2:
                swap(idx, end)
                end -= 1
                idx -= 1

            idx += 1


        return nums


nums = [2,2,0]
foo = Solution()
res = foo.sortColorsII(nums)

print(res)