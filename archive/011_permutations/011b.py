class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        sub_problem_res = self.permute(nums[1:])
        res = []

        n = nums[0]
        for sub in sub_problem_res:
            for idx in range(len(sub) + 1):
                foo = sub.copy()
                foo.insert(idx, n)
                res.append(foo)
        
        return res
