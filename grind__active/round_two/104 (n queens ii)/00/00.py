class Solution:
    def totalNQueens(self, n: int) -> int:
        self.verticals = set()
        self.horizontals = set()
        self.forwardDiagonals = set()
        self.backwardDiagonals = set()
    
        self.count = 0
        self.dimensions = n
            
        self.placeQueen(rowIdx=0)
        
        return self.count
        
    def placeQueen(self, rowIdx: int):
        if rowIdx == self.dimensions:
            self.count += 1
            return
        
        for colIdx in range(self.dimensions):
            if self.is_vacant(rowIdx, colIdx):
                self.horizontals.add(rowIdx)
                self.verticals.add(colIdx)
                
                fdid = rowIdx + colIdx
                self.forwardDiagonals.add(fdid)
                
                bdid = rowIdx - colIdx
                self.backwardDiagonals.add(bdid)
                
                self.placeQueen(rowIdx + 1)
                
                self.horizontals.remove(rowIdx)
                self.verticals.remove(colIdx)
                self.forwardDiagonals.remove(fdid)
                self.backwardDiagonals.remove(bdid)
                
    def is_vacant(self, rowIdx, colIdx):
        foo = (
            rowIdx in self.horizontals,
            colIdx in self.verticals,
            (rowIdx + colIdx) in self.forwardDiagonals,
            (rowIdx - colIdx) in self.backwardDiagonals,
        )
        
        return not any(foo)