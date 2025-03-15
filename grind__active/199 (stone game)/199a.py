# https://leetcode.com/problems/stone-game/description/

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        pass
    
        # two variables, `alice` and `bob`
        # use a variable, `i` to determine whose turn it is
        # each player should always take the largest
        # bookend number
        # if the bookend numbers are equal and different i.e. different indices
        # explore both options
        # preferably pick the one where alice wins
        left, right = 0, len(piles) - 1
        res = self.explore(left, right, piles, 0)
        return True if res > 0 else False

    def explore(self, leftIdx, rightIdx, piles, counter):
        alice, bob = 0, 0
        
        while leftIdx <= rightIdx:
            leftMost, rightMost = piles[leftIdx], piles[rightIdx]
            chosen = None
            if leftMost > rightMost or leftIdx == rightIdx:
                chosen = leftMost
                leftIdx += 1
            elif rightMost > leftMost:
                pass
                chosen = rightMost
                rightIdx -= 1
            else:
                if counter % 2 == 0:
                    alice += piles[leftIdx]
                else:
                    bob += piles[rightIdx]
                resOne = self.explore(leftIdx + 1, rightIdx, piles, counter + 1)
                resTwo = self.explore(leftIdx, rightIdx-1, piles, counter + 1)
                
                currRes = alice - bob
                return max(
                    currRes + resOne,
                    currRes + resTwo
                )
                
            if counter % 2 == 0:
                alice += chosen
            else:
                bob += chosen
            
            counter += 1
                
        return alice - bob
    
arr = [
    [5,3,4,5],
    [3,7,2,3],
    [3,2,10,4],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGame(foo)
print(res)