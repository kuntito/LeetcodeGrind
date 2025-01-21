# TODO https://neetcode.io/solutions/next-greater-element-i
# deep solution
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass
        
        # for O(1) access to elements in `nums2`
        counter = { n: idx for idx, n in enumerate(nums2) }
        
        greater = {}
        
        mots = []
        for n in nums2:
            pass
            while mots and n > mots[-1]:
                pass
                rem = mots.pop()
                greater[rem] = n
            
            if n in counter:
                mots.append(n)
                
        res = [greater[n] if n in greater else -1 for n in nums1]
        return res

    
arr = [
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[1,3,5,2,4], [6,5,4,3,2,1,7]],
    [[2, 4], [1, 2, 3, 4]],
    [[4, 1, 2], [1, 3, 4, 2]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.nextGreaterElement(foo, bar)

print(res)