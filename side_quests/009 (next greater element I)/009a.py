# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num_map = {}
        for idx, n in enumerate(nums2):
            num_map[n] = idx

        res = []
        for n in nums1:
            idx = num_map[n]
            res.append(
                self.find_next(idx + 1, n, nums2)
            )
        return res
    

    def find_next(self, start_idx, target, nums2):
        for idx in range(start_idx, len(nums2)):
            if nums2[idx] > target:
                return nums2[idx]
            
        return -1


arr = [
    [[2, 4], [1, 2, 3, 4]],
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[4, 1, 2], [1, 3, 4, 2]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.nextGreaterElement(foo, bar)

print(res)