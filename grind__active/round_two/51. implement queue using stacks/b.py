# https://leetcode.com/problems/implement-queue-using-stacks/

# after debating claude, it turns out the two stack approach
# is more optimal than my recursion..
# i was impressed with me, cause i did it in one go
# but there's simpler methods..
# LeetCode is really humbling..

# okay.. let's name these stacks firstStack and secondStack

# initially, i add 1, 2, and 3 to firstStack
# when i pop, i empty it's content into secondStack and return 1 

# now, secondStack is [2, 1]
# if i add 4​ and 5
# you're saying 4 and 5 goes into firstStack​

# now, i want to pop..
# i'd still pop from secondStack since, i'm always popping from the front of the queue..

# the reverse in secondStack is what mimics the queue.
# and this would be O(1) until it's empty.

# and when it's empty, i should do what i did at first, empty all but one from firstStack into.. secondStack​.. in reality, i don't need to empty all but one..

# i can simply empty all, and pop the secondStack

# re-made the mistake, i didn't return after popping from the stack..

class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.reverseStack = []

    def push(self, x: int) -> None:
        self.firstStack.append(x)

    def pop(self) -> int:
        if not self.reverseStack:
            while self.firstStack:
                self.reverseStack.append(
                    self.firstStack.pop()
                )
        
        return self.reverseStack.pop()

    def peek(self) -> int:
        if self.reverseStack:
            return self.reverseStack[-1]
        
        return self.firstStack[0]

    def empty(self) -> bool:
        return not (self.firstStack or self.reverseStack)
