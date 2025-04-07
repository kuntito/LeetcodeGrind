# https://leetcode.com/problems/furthest-building-you-can-reach/description/


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        pass
        # create an array of climbs
        # a climb is the number of bricks it takes to reach the next building
        # i.e. [2, 1, 3]
        # there's only one climb in the array. from `1` to `3`
        # and it's value is `2`
        
        # i believe an array of climbs might bring clarity to the question
        # save the index of each climb
        climbs = self.getClimbs(heights)
        print([x[0] for x in climbs])
        # print(climbs)
        
        # the question becomes, what's the most efficient way to distribute bricks and ladders
        # since `ladders` are more useful, since they can be used for inordinately high climbs
        # we should save them for later?
        # TODO, the assumption is wrong, bricks first is not always the optimal approach
        # see `[[1,5,1,2,3,4,10000], 4, 1]`
        # bricks first approach returns `3`
        # when the answer is `5`
        
        # use only bricks, when you run out, use ladders
        furthest = 0
        for bricksNeeded, idx in climbs:
            if bricks >= bricksNeeded:
                bricks -= bricksNeeded
            elif ladders:
                ladders -= 1
            else:
                break
            furthest = idx
                
        # TODO increment `furthest` while the next index is <= it's value
        dim = len(heights)
        while furthest + 1 < dim and heights[furthest] >= heights[furthest + 1]:
            furthest += 1
        return furthest
                
        
    def getClimbs(self, arr):
        climbs = []
        
        dim = len(arr)
        for idx in range(1, dim):
            prev, curr = arr[idx - 1], arr[idx]
            if curr > prev:
                cl = curr - prev
                climbs.append((cl, idx))
                
        return climbs


        
arr = [
    [[4,12,2,7,3,18,20,3,19], 10, 2],
    [[4,2,7,6,9,14,12], 5, 1],
    [[14,3,19,3], 17, 0],
    [[1,5,1,2,3,4,10000], 4, 1]
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.furthestBuilding(foo, bar, baz)
print(res)