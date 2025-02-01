# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        pass
        # create a counter for `nums`
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        # for each kv pair, (n, count)
        # if count cannot be separated into 2's and 3's
        # return False
        res = 0
        for n, count in counter.items():
            parts_count = self.get_partition(count)
            if parts_count is None:
                return -1
            
            res += parts_count
            
        return res
        
        # declare a variable, `res`
        # it tracks the amount of times, you'd need to remove `3` or `2` elements
        # from count till it becomes `0`
        
    # TODO what's going on here?
    def get_partition(self, count):
        if count == 0:
            return 1
        
        pass
        res = None
        for i in [3, 2]:
            tmp = count - i
            if tmp < 0: continue
            exp_res = self.explore(tmp)
            if res is None:
                res = exp_res
            else:
                res = min(exp_res, res)
            
        return res if res is None else res + 1
        