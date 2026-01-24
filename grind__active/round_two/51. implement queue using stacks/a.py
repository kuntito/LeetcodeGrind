# https://leetcode.com/problems/implement-queue-using-stacks/

# now, how would this work..
# both stack and queue are a list of items..
# both add items to the end of the list..

# difference is, stacks remove items from the end
# while, queues remove items from the front..

# and they want me to implement a queue with a stack, rather stacks..
# i know i'd have to have a stack..
# since both data structures add items the same way..
# a stack would suffice with adding...

# however, removing is where it gets dicey
# i can't remove from the front of a stack unless
# i remove all the elements after it..

# perhaps, it's what i'd do..
# when i remove from stack
# i'd remove every element except the first..

# and re-add the removed elements..
# but you'd need to store them somewhere first..
# i think that's where the stackS part of the question is..

# if i have two stacks i can remove every element and add to the second
# stack.. i think you've jumped the gun on this one..
# if you remove elements from the end of the stack
# and add it to another stack..

# you'd be reversing the elements..
# think:
# [1, 2, 3]
# we'd pop `3` and `2`..
# we put this in another stack..
# we'd have [3, 2]
# which would reverse the order..

# i think, i can use recursion to my advantage..
# on each recursive call, i'd pop the last element from the stack..

# first call, pop `3`
# second call, pop `2`
# third call, pop `1`, this'd be the base case, so i'd return the value

# however, going back up, i'd append `2`
# go one up, append `3`
# and i'd have added the elements back in the right order..

# i used the recursive stack to my advantage.

# made an error, i didn't return the result of the recursive pop
# i merely called it but should have stored it's result
# and returned that.

class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 1:
            return self.stack.pop()
        
        elem = self.stack.pop()
        
        poppedElem = self.pop()
        
        self.stack.append(elem)
        
        return poppedElem
    

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack
    
queue = MyQueue()
queue.push(1)
queue.push(2)

print(queue.stack)

print(queue.peek())

print(queue.pop())

print(queue.empty())