# https://leetcode.com/problems/excel-sheet-column-title/

# re-implementing the solution from `f.py`
# using a queue

# works..

from collections import deque

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.num_to_alpha = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
        }
                
        queue = deque()
        
        self.explore(columnNumber, queue)
        
        return ''.join(queue)
    
    def explore(self, number, queue: deque):
        if number == 0:
            return
        
        multipes26, rem = divmod(number, 26)
        
        if rem == 0:
            queue.appendleft('Z')
            multipes26 -= 1
        else:
            queue.appendleft(
                self.num_to_alpha[rem]
            )
            
        self.explore(multipes26, queue)