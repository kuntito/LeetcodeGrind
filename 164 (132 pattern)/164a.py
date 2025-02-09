# https://leetcode.com/problems/132-pattern/description/

# TODO optimize the rightVal search
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        pass
        if len(nums) < 3:
            return False
        
        # create an array that stores the lowest number seen at each index
        # create a hash map that stores the frequency of the numbers
        # maintain the lowest seen so far
        # for each index where (nums[idx] > lowest + 1)
        # search rightwards, search the range(lowest+1, nums[idx])
        # for any number that's in the hashmap
        # the hashmap should only contain elements [idx + 1 =>]
        
        counter = {}
        
        # starting from the first k valid number
        for n in nums[2:]:
            counter[n] = counter.get(n, 0) + 1
            
        lowest = nums[0]
        dim = len(nums)
        for idx in range(1, dim):
            midVal = nums[idx]
            for rightVal in range(lowest + 1, midVal):
                if rightVal in counter:
                    # print(lowest, midVal, rightVal)
                    return True
                
            lowest = min(lowest, midVal)

            if idx >= 2:
                counter[midVal] -= 1
                if counter[midVal] == 0:
                    del counter[midVal]
                
        return False
    
arr = [
    [-2,1,2,-2,1,2],
    [1,2,3,4],
    [3,1,4,2],
    [-1,3,2,0],
]
foo = arr[-1]
sol = Solution()
res = sol.find132pattern(foo)
print(res)