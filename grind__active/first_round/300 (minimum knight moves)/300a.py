# https://leetcode.com/problems/minimum-knight-moves/description/

# TODO, the problem here is a max recursion exceeded, of the eight paths, some paths would never lead to the the destination, how do we avoid going there?

# i think a bfs solves this problem, since we explore all layers at once
# we never have to go too deep to realize the error of our ways

# how do i know what paths would not lead to the destination?
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        pass
        # what is this asking? we are given a boundless chessboard
        # it's as big as it gets, we have a knight at position (0, 0)
        # a knight can move in eight directions
        
        # and we want to find the minimum number of steps it would take for the knight to reach position (x, y) so we return an integer
        
        # how would you solve this?
        
        # i think the naive approach would be to try out all eight directions, tracking how long it takes to get to (x, y) and return the shortest one
        
        # the overhead logic is simple enough, the tricky bit is implementing the movement of the knight.
        
        # a knight moves in a L shape but when you observe closely, the knight moves up, down, left or right then turns
        # but makes a total of three moves in the process
        
        # so we can move the knight-
        # there's some sense here but i think the focus should be solving the problem first before optimizing the movement of the knight
        
        # let's harcode the eight positions, then recursively use that as a starting position, every position we explore counts as one step
        
        # we would eventually hit (x,y)
        # then return the least number of steps it took to get there
        # while exploring, there's a good chance, we'd hit some positions more than once, so it makes sense to memoize them
        
        # i think we can start here
        # first, the first recursive call
        origin = (0, 0)
        destination = (x, y)
        memo = {}
        return self.explore(origin, destination, memo) - 1
    
    def explore(self, pos, destination, memo):
        # if the current position has been memoized, return the memoized value
        if pos in memo:
            return memo[pos]
        
        # the base case for finding the destination
        if pos == destination:
            # what do we return?
            return 1
        
        # we can't go out of bounds so no need to check
        # what we need is to write out the eight directions
        # and a variable to track the least steps
        
        # let's initialize that to max infinity
        leastSteps = float("inf")
        
        # then determine the eight directions
        r, c = pos
        nextDestinations = [
            (r - 1, c - 2),
            (r - 2, c - 1),
            (r - 1, c + 2),
            (r - 2, c  +1),
            (r + 1, c - 2),
            (r + 2, c - 1),
            (r + 1, c + 2),
            (r + 2, c + 1),
        ]
        
        for nextDes in nextDestinations:
            leastSteps = min(
                leastSteps,
                self.explore(nextDes, destination, memo)
            )
            
        memo[pos] = leastSteps + 1
        return memo[pos]
        

arr = [
    [2, 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minKnightMoves(foo, bar)
print(res)