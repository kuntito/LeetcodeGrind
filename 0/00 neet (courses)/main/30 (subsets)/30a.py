# https://leetcode.com/problems/subsets/description/

from collections import deque

class Solution:
    def subsets(self, nums: list) -> list:
        nums_dict = {n: idx for idx, n in enumerate(nums)}
        res = []

        queue = deque()
        queue.append([])
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                elem = queue.popleft()
                res.append(elem)
                self.add_subsets(elem, nums, queue, nums_dict)

        return res


    def add_subsets(
        self, 
        elem: list, 
        nums: list, 
        queue: deque, 
        nums_dict: dict
    ):
        if elem:
            last_item = elem[-1]
            idx = nums_dict[last_item]
        else:
            idx = -1

        for n in nums[idx + 1:]:
            new_sublist = elem + [n]
            queue.append(new_sublist)

        



bar = [1, 2, 3]
foo = Solution()

res = foo.subsets(bar)
print(res)