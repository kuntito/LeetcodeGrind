# https://leetcode.com/problems/candy-crush/description/

class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        pass
        # a recursive application of two steps until the board is stable
        # step 1: identify the consecutive cells
        # step 2: convert them to zero's
        # step 3: fill in the holes
        
        # 0 0 0
        # 1 0 1
        # 1 0 1
        
        self.explore(board)
        return board
    
    def explore(self, board):
        consec_cells = self.get_consec_cells(board)
        if not consec_cells:
            return
        
        self.convert_to_zeros(consec_cells, board)
        self.fill_holes(board)
        
    def get_consec_cells(self, board):
        rows, cols = len(board), len(board[0])
        visited = set()
        
        consec_cells = []
        for ri in range(rows):
            for ci in range(cols):
                if (ri, ci) in visited:
                    continue
                cell_res = self.exploreSimilar(ri, ci, board, visited)
                if len(cell_res) < 3:
                    continue
                # TODO mark as visited
                consec_cells.append(cell_res)
                
        return consec_cells
    
    def exploreSimilar(self, ri, ci, tgt, board, visited):
        # you want to explore cardinal directions for every cell with the same value as
        # the starting ri, ci
        
        # pass the target value
        # for each visited (ri, ci) with said value, append it to `visited`
        # and continue the exploration
        
        # the exploration naturally stops when you've seen all cells
        # or no cells match target value
        
        # then we return visited cells
        
        rows, cols = len(board), len(board[0])
        if (ri, ci) in visited:
            return
        if ri < 0 or ri == rows or ci < 0 or ci == cols:
            return
        if board[ri][ci] != tgt:
            return
        
        visited.append((ri, ci))
        
        self.explore()
                
                
    
    def convert_to_zeros(self, consec_cells, board):
        pass
    
    def fill_holes(board):
        pass
