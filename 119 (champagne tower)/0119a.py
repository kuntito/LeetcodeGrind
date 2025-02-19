# https://leetcode.com/problems/champagne-tower/description/

# https://neetcode.io/solutions/champagne-tower
# 04:00
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pass
        # for each row, fill the cups
        
        count = 0
        old_row = [poured]
        
        while count < query_row:
            new_row = []
            
            dim = len(old_row)
            for i in range(dim + 1):
                curr = old_row[i] if i < dim else 0
                prev = old_row[i-1] if i - 1 < dim else 0
                
                currChunk = self.get_leftover_chunk(curr)
                prevChunk = self.get_leftover_chunk(prev)
                
                
                
            
            count += 1


    def get_leftover_chunk(self, value):
        if value >= 1:
            value -= 1
            
        return value / 2