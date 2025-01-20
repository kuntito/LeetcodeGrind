# https://leetcode.com/problems/next-greater-element-i/description/

# TODO https://neetcode.io/solutions/next-greater-element-i
# look at solution
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass
        # you want to iterate through `nums1`
        # for each value, find it's index in `nums2`, `j`
        # if it exists, check if there's a number greater than nums2[j]
        
        # for O(1) access to elements in `nums2`
        counter = { n: idx for idx, n in enumerate(nums2) }
        
        # for O(1) access to numbers greater than `nums2[j]`
        greater_than = self.get_greater_than(nums2)
        
        # print(greater_than)
                
        res = []
        for idx, n in enumerate(nums1):
            pass
            item = -1
            if n in counter:
                idxCounter = counter[n]
                item = greater_than[idxCounter]
            
            res.append(item)
    
        return res
    
    def get_greater_than(self, arr):
        pass
        dim = len(arr)
        greater_than = [-1 for _ in range(dim)]
        # the idea is for each val in arr
        # `greater_than` contains the nearest value to it's right that's greater
        # than it
        
        # to establish this, iterate from behind
        # keep a monotonically decreasing stack
        monotone = []
        # for each `val` in `arr`
        # iterate through the stack from behind
        # greater_than[idx] = the first value that's greater than `val`
        # if not, return -1
        for idx in range(dim - 1, -1, -1):
            val = arr[idx]
            
            while monotone and val > monotone[-1]:
                monotone.pop()
                
            monotone.append(val)
            
            for j in range(len(monotone)-1, -1, -1):
                potential_great = monotone[j]
                if potential_great > val:
                    greater_than[idx] = potential_great
                    break
                
        return greater_than
                    
            
            


arr = [
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[4, 1, 2], [1, 3, 4, 2]],
    [[2, 4], [1, 2, 3, 4]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.nextGreaterElement(foo, bar)

print(res)