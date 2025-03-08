# https://leetcode.com/problems/candy/description/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        pass
        # figure out which indexes need more candy than their neighbour
        # create an array of size `n` to store these
                
        # there are two types of indices
        # one where it's greater than it's left and right
        # another where it's only greater than left OR greater than right
        
        # there are two types of values
        # type 1 values are only greater than their left or greater than their right
        # type 2 values are greater than both their left value and their right value
                
        # for the type 1 values, increment by `1`
        # for the type 2 values, note the index
                
        dim = len(ratings)
        
        # minimum candy for each child
        arr = [0 for _ in range(dim)]
        
        both_sides = []
        for idx in range(dim):
            prevRating = None if idx == 0 else ratings[idx - 1]
            nextRating = None if idx + 1 == dim else ratings[idx + 1]
            
            currRating = ratings[idx]
            
            sides = 0
            # if prevRating is a number and that number is less than currRating
            # it means this value should have more candy than it's neighbour
            if isinstance(prevRating, int) and currRating > prevRating:
                sides += 1

            # if nextRating is a number and that number is less than currRating
            # it means this child should have more candy than it's neighbour
            if isinstance(nextRating, int) and currRating > nextRating:
                sides += 1
                
            if sides == 1:
                arr[idx] += 1
            elif sides == 2:
                both_sides.append(idx)
                
        # for each index in `both_sides`
        # make it `arr[idx] = 1 + max(leftSide, rightSide)`
        
        for idx in both_sides:
            leftCandy = arr[idx - 1]
            rightCandy = arr[idx + 1]
            
            arr[idx] = max(leftCandy, rightCandy) + 1
            
        # i'm adding dim since every index has at least one candy
        # `dim` is the length of the entire array
        return sum(arr) + dim
    
    
arr = [
    [1, 0, 2],
    [1, 2, 2],
    [1,2,87,87,87,2,1]
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)