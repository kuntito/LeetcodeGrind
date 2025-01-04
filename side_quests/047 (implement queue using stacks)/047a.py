# https://leetcode.com/problems/implement-queue-using-stacks/description/

# TODO https://neetcode.io/solutions/implement-queue-using-stacks
# TODO implement amortized O(1) solution
class MyQueue:
    def __init__(self):
        pass
        # create two stacks, `one` and `two`
        self.one = []
        self.two = []

    def push(self, x: int) -> None:
        pass        
        # push elements to `one`
        self.one.append(x)

    def pop(self) -> int:
        pass        
        # move `one`'s elements into `two` except the last one
        while len(self.one) > 1:
            self.two.append(self.one.pop())

        # save it as `res`
        res = self.one.pop()
        # empty `two` into `one`
        while self.two:
            self.one.append(self.two.pop())
        
        print(res)
        return res

    def peek(self) -> int:
        return self.one[0]

    def empty(self) -> bool:
        return len(self.one) == 0


sol = MyQueue()
sol.push(1)
sol.push(2)
sol.push(3)
sol.push(4)
sol.pop()
sol.push(5)
sol.pop()
sol.pop()
sol.pop()
sol.pop()