# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        pass
        # create an array, `comparisons`
        # to store the relationships between each element of `arr`
        # `comparisons` should compare arr[i] with arr[i+1] and store
        # the comparison operator `>` or `<`
        
        risons = []
        dim = len(arr)
        for idx in range(dim - 1):
            curNum = arr[idx]
            nextNum = arr[idx + 1]
            
            if curNum > nextNum:
                risons.append("a")
            elif curNum < nextNum:
                risons.append("b")
            else:
                risons.append("=")
        
        # the next step is to find a longest string of alternating
        # `<` and `>`
        
        # since `rsns` can only contain two values
        # use a sliding window such that whenever the current idx is the same as previous, you update it
        
        # print(risons)
        
        uno, dos = 0, 0
        longestWindow = 0
        while dos < len(risons):
            pass
            if risons[dos] == "=":
                uno, dos = dos + 1, dos + 1
                continue
        
            if dos > 0 and risons[dos] == risons[dos - 1]:
                uno = dos
                
            dist = (dos - uno) + 1
            longestWindow = max(longestWindow, dist)
            dos += 1
        
        # return the result + 1
        return longestWindow + 1
        
arr = [
    [9,4,2,10,7,8,8,1,9],
    [4,8,12,16],
    [100],
]
foo = arr[-1]
sol = Solution()
res = sol.maxTurbulenceSize(foo)
print(res)