# https://leetcode.com/problems/open-the-lock/description/

# TODO https://neetcode.io/solutions/open-the-lock
# write your version, view the decision tree
# what's really going on?
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        pass
        # each lock position can either turn left or turn right
        # use a bfs search to try all combinations
        # initially it's [0, 0, 0, 0]
        # the first dial can be turned to `1` or `9`
        # do the same for each dial and store the new orientation
        
        # make a set of the deadends, if you encounter a dead end,
        # do not include the new orientation
        
        # `arr` is a 2d array that contains all the valid combinations seen so far
        
        arr = [
            [0, 0, 0, 0]
        ]
        
        deadends = set(deadends)
        # you'd have to convert the combinations to string to check for deadends
        while arr:
            tmp = []
            for comb in arr:
                for c in self.get_new_combinations(comb):
                    # TODO i think you should add visited positions to deadends
                    # so you don't visit the same position more than once
                    if c in deadends:
                        continue

            
        return -1

    def get_new_combinations(self, comb):
        pass
        res = []
        for idx, dig in enumerate(comb):
            clone = comb[::]
            for newPos in self.get_digits(dig):
                clone[idx] = newPos
                res.append("".join(str(d) for d in clone))
                
        return res
    
    def get_digits(self, dial):
        # since each dial can go from 0 - 9, (10 distinct values)
        # we can either turn the dial forward
        # or backward
        
        # for simplicity sake
        # do dial + 1 and dial + 9
        # and mod the results by 10
        # this would simulate turning forward and backward
        
        posOne = (dial + 1) % 10
        posTwo = (dial + 9) % 10
        
        return posOne, posTwo
    
sol = Solution()
res = sol.get_new_combinations([0, 0])

print(res)