# https://leetcode.com/problems/candy/description/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        pass
        # how about a dependency graph
        # where each child knows who has a higher rating than them
        # then a loop to update the rating of each child to `1`, minimum requirement
        # but whenever a child's rating is increased, it's parents are also increased by `1`
        
        dim = len(ratings)
        arr = [0 for _ in ratings]
        
        dependencies = {}
        for idx in range(dim):
            dependencies[idx] = []
            
        for idx in range(dim):
            prevRating = None if idx == 0 else ratings[idx - 1]
            nextRating = None if idx + 1 == dim else ratings[idx + 1]
            
            currRating = ratings[idx]
            if isinstance(prevRating, int) and prevRating > currRating:
                dependencies[idx].append(idx - 1)
            if isinstance(nextRating, int) and nextRating > currRating:
                dependencies[idx].append(idx + 1)
                
                
        print(dependencies)
        for idx in range(dim):
            if arr[idx] == 0:
                arr[idx] += 1
            self.update_parents(idx, dependencies, arr)
                
        print(arr)
        return sum(arr)


    def update_parents(self, idx, dependencies, arr):
        for parIdx in dependencies[idx]:
            arr[parIdx] = max(
                arr[idx] + 1,
                arr[parIdx]
            )
            self.update_parents(parIdx, dependencies, arr)

    
arr = [
    [1, 0, 2],
    [1, 2, 2],
    [1,2,87,87,87,2,1]
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)