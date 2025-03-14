# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        targetClone = [None, None, None]
    
        for item in triplets:
            uno, dos, tres = item
            if uno > target[0] or dos > target[1] or tres > target[2]:
                continue

            if uno == target[0]:
                targetClone[0] = uno

            if dos == target[1]:
                targetClone[1] = dos
    
            if tres == target[2]:
                targetClone[2] = tres



        return all(clone == actual for clone, actual in zip(targetClone, target))
    
arr = [
    [[[2,5,3],[1,8,4],[1,7,5]], [2,7,5]],
    [[[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]],
    [[[3,5,1],[10,5,7]], [3,5,7]],
    [[[2,5,3],[2,7,8],[1,3,5]], [2,7,5]],
    [[[1,3,1]], [1, 3, 1]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.mergeTriplets(foo, bar)
print(res)