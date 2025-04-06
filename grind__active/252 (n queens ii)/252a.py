# https://leetcode.com/problems/n-queens-ii/description/

# TODO https://neetcode.io/solutions/n-queens-ii
class Solution:
    def totalNQueens(self, n: int) -> int:
        pass
        # based on how queens be
        # there can only be one queen on each row
        # meaning each of the `n` queens have their own row  
        
        # that said, we place explore what happens on every column on the queens row
        # when you place a queen, mark all the lines it can reach
        # verticals, horizontals, forward diagonals and backward diagonals
        # move to the next row and place a queen on a vacant cell
        # if possible move to the next row
        # do this until all queens are placed
        
        # it's giving.. recursion and backtracking
        # if a particular cell cannot be placed

        # try another cell
        # declare a global variable to track the solutions found
        # the algorithm guarantees the solutions would be distinct
        # since each cell route is explored only once
        
        # the kicker is mapping out the queens range
        # the verticals and horizontals are easy
        # it's the diagonals that cause a situation
        
        # neetcode revealed to me that each diagonal can be described
        # by combining the rows and columns
        # backward slanting diagonals can be represented by subtracting
        # the columns from the rows
        
        # 00 01 02 03  
        # 10 11 12 13  
        # 20 21 22 23  
        # 30 31 32 33
        
        # i.e. 00, 11, 22, 33 can be represented by `0`
        # another bsd, 10, 21, 32 can be represented by `1`
        
        
        # the forward slanting diagonals can be represented by adding the rows and columns
        # i.e. 01, 10 is `1`
        # 20, 11, 02 is `2` and so on and so forth
        
        # declare sets for each, verticals, horizontals, fsds, bsds
        # for each queen placed, determine it's range
        # and place in appropriate cells
        
        # when done exploring a position, remove the added ids from the sets
        # and, voila

        self.dim = n
        self.count = 0
        cols, rows, fsds, bsds = set(), set(), set(), set()
        self.explore(n, cols, rows, fsds, bsds)
        
        return self.count
    
    def explore(self, queensLeft, cols, rows, fsds, bsds):
        # `queensLeft - 1` also represents the current row
        # the iteration starts from the bottom up
        if queensLeft == 0:
            self.count += 1
            return
        
        
        for ci in range(self.dim):
            if ci in cols:
                continue
            
            ri = queensLeft - 1
            fsi = ri + ci
            bsi = ri - ci
            
            if any((                
                ri in rows,
                fsi in fsds,
                bsi in bsds
            )):
                continue
            
            rows.add(ri)
            cols.add(ci)
            fsds.add(fsi)
            bsds.add(bsi)
            
            self.explore(queensLeft-1, cols, rows, fsds, bsds)
            
            rows.remove(ri)
            cols.remove(ci)
            fsds.remove(fsi)
            bsds.remove(bsi)
            
arr = [
    4,
    1,
    9,
]
foo = arr[-1]
sol = Solution()
res = sol.totalNQueens(foo)
print(res)
