# https://leetcode.com/problems/house-robber/

from typing import List

# TODO 
# lifted this off a previous submission
# trying to figure out why it works..

# the algorithm's written in a way that the value at current index
# always tells you the best you can rob starting from there..

# but how does it know that?
# the iteration starts from behind..


# say, i'm at the last index..
# what's the most i can rob..

# well, just the value at the last index..
# but since, it's a loop, everything we do in one loop, we do in the other..
# less, we add conditionals..

# let's leave those tactics and deep what actually happened here..

class Solution:
    def rob(self, nums: List[int]) -> int:
        dim = len(nums)
        nums += [0, 0]

        for idx in range(dim - 1, -1, -1):
            nums[idx] = max(
                nums[idx + 1],
                nums[idx] + nums[idx + 2]
            )
        
        return nums[0]
    
arr = [
    [8,4,3,3,10],
    [6,6,4,8,4,3,3,10],
]
foo = arr[-1]
sol = Solution()
res = sol.rob(foo)

print(res)