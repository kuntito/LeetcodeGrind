# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        pass
        # create a hashmap of all the elements of nums
        counter = {}
        
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        res = []
        while counter:
            tmp = []
            to_remove = []
            
            for key in counter:
                tmp.append(key)
                counter[key] -= 1
                
                if counter[key] == 0:
                    to_remove.append(key)
                    
            while to_remove:
                del counter[to_remove.pop()]
                
            res.append(tmp)
            
        return res
    
arr = [
    [1,3,4,1,2,3,1],
    [1,2,3,4],
]
foo = arr[-1]
sol = Solution()
res = sol.findMatrix(foo)
print(res)
                