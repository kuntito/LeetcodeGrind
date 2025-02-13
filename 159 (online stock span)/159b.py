# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        pass
        # keep a monotonically decreasing stack
        # that contains (elem, idx)
        
        self.idx = 0
        self.stack = []
        self.maxEver = None

    def next(self, price: int) -> int:
        pass
        # return the dist between current idx and the previous idx in `stack`
        if self.maxEver is None:
            self.maxEver = price
        else:
            self.maxEver = max(
                price,
                self.maxEver
            )
            
        if self.maxEver != price:
            res = self.getGreatest(price)
        else:
            self.stack.append(
                (price, self.idx)
            )
            res = self.idx + 1
        
        self.idx += 1
        return res

    def getGreatest(self, price):
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
            
        prevIdx = self.stack[-1][1] + 1 if self.stack else self.idx
            
        self.stack.append(
            (price, self.idx)
        )
        
        res = (self.idx - prevIdx) + 1
        return res
        



# Your StockSpanner object will be instantiated and called as such:
sol = StockSpanner()
# print(sol.next(100))
# print(sol.next(80))
# print(sol.next(60))
# print(sol.next(70))
# print(sol.next(60))
# print(sol.next(75))
# print(sol.next(85))
print(sol.next(1))
print(sol.next(79))
print(sol.next(34))
print(sol.next(21))
print(sol.next(34))
# print(sol.next(16))
# print(sol.next(59))
# print(sol.next(63))
# print(sol.next(72))
# print(sol.next(5))