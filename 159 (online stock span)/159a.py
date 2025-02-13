# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        pass
        self.monotoneStack = []
        self.curIdx = 0

    def next(self, price: int) -> int:
        pass
        while self.monotoneStack and price > self.monotoneStack[-1][0]:
            self.monotoneStack.pop()
            
        prevIdx = self.monotoneStack[-1][1] if self.monotoneStack else None
        self.monotoneStack.append((price, self.curIdx))
        
        res = 1 if prevIdx is None else self.curIdx - prevIdx
        self.curIdx += 1
        return res
            
        
        



# Your StockSpanner object will be instantiated and called as such:
sol = StockSpanner()
print(sol.next(100))
print(sol.next(80))
print(sol.next(60))
print(sol.next(70))
print(sol.next(60))