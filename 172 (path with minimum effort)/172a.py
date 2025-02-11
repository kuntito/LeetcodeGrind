# https://leetcode.com/problems/path-with-minimum-effort/description/

# TODO maxrecursion depth
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        pass
        # for each (ri, ci), explore the path to (rows-1, cols-1)
        # memoize the shortest ones
    
        
        return self.explore((0, 0), heights, {}, set())
        
    def explore(self, org, arr, memo, seen):
        if org in memo:
            return memo[org]
        
        seen.add(org)
        
        rows, cols = len(arr), len(arr[0])
        if org == (rows-1, cols-1):
            return 0
        
        neighbours = self.get_neis(org, arr, seen)
        minLen = None
        for nei in neighbours:
            source_nei_dist = self.get_dist(org, nei, arr)
            neiRes = self.explore(nei, arr, memo, seen) + source_nei_dist
            if minLen is None:
                minLen = neiRes
            else:
                minLen = min(
                    minLen,
                    neiRes
                )
                
        memo[org] = minLen
        return memo[org]
    
    def get_dist(self, posOne, posTwo, arr):
        numOne = arr[posOne[0]][posOne[1]]
        numTwo = arr[posTwo[0]][posTwo[1]]
        
        return abs(numOne - numTwo)
    
        
        
    def get_neis(self, org, arr, seen):
        rows, cols = len(arr), len(arr[0])
        ri, ci = org
        neis = [
            (ri - 1, ci),
            (ri + 1, ci),
            (ri, ci - 1),
            (ri, ci + 1),
        ]
        
        return [(r, c) for r, c in neis if r >= 0 and r < rows and c >=0 and c < cols if (r, c) not in seen]
    
arr = [
    [[1,2,2],[3,8,2],[5,3,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumEffortPath(foo)
print(res)