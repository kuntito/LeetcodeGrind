# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# TODO https://neetcode.io/solutions/find-all-numbers-disappeared-in-an-array
# TODO rewrite this for clarity, then view neets solution
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # move elements to appropriate indices
        # [4,3,2,7,8,2,3,1]

        # starting with the first element, `4`
        # it should be at index (3), but element `7` is at index `3`
        # move element `7` to index (6)
        # but element `3` is at index (6), move element `3` to index (2)
        # but element `2` is at index (2), move element `2` to index (1)
        # but element `3` is at inedx (1), move element `3` to index (2)

        # the loop stops here because the element at index (2) is already 3

        dim = len(nums)
        # leave a `None` whenever you move elements
        for idx in range(dim):
            n = nums[idx]
            actualIdx = n - 1
            if actualIdx == idx:
                continue
            nums[idx] = None
            self.place_appropriately(n, actualIdx, nums)

        return [i+1 for i in range(dim) if nums[i] is None ]


    def place_appropriately(self, n, idx, nums):
        # if `nums[idx]` is None or `nums[idx] == n`: return
        tenant = nums[idx]
        if tenant and tenant != n:
            nums[idx] = None

            tenantIdx = tenant - 1
            self.place_appropriately(tenant, tenantIdx, nums)

        nums[idx] = n


    
arr = [
    [1],
    [1, 1],
    [3,3,1],
    [4,3,2,7,8,2,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findDisappearedNumbers(foo)
print(res)
