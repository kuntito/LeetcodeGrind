# https://leetcode.com/problems/min-stack/description/

# i think what went down in `b.py` is
# navdeep kept two stacks, one for the elements as they enter
# another to track the minimum when each element is added..

# which is what we need?
# when we pop an element, it could be the min element we just popped.
# in which case, we want to update our min element.

# the solution to use stacks is elegant.
# at each entry point, it's trivial to calculate the min element
# so, as each element is added, we take a snapshot of the min element at that point.

# and store it in a separate araay.
# to be fair, the solution can be rewritten with a single array.

# i'd just need a variable to track the minimum element so far.
# i can initialize this to `float("inf")`

# one error, when i pop the last item from the array
# i should reset min element to `float("inf")`

# another error, i should update `self.minElem` whenever i pop items..
# why this didn't occur to me at first was because, i always referred to the last item
# in the array as the min element.

# however, i introduced two sources of truth, `self.minElem` and `arr[-1][1]`
# i should only use one, on every pop, either
# i update `self.minElem` to the new `arr[-1][1]` or `float("inf")` if array is empty
# or when adding new elements
# `self.minElem` should always be compared with the last entry in `arr`
# not compared with the new element itself, i.e. `if val < self.minElem`

# i think the second approach is cleaner.
# wrong, this doesn't solve the problem.. 

# consider -20 being the current minimum element
# and the element being on top the stack..

# [(10, -10), (-20, -20)]
# self.minElem = -20, from when you added the element,

# when you pop it from the stack..
# you'd get 
# [(10, -10)]
# but self.minElem still points to -20


# this way, if you add a new element, `10`
# it's corresponding min element should be `-10`
# not `-20`

# so the two alternatives should be update `self.minElem`
# on every pop...

# or update it on every entry..
# i.e. self.minElem = arr[-1][1] if arr else float("inf")
# then do the check, if val < self.Elem...


class MinStack:
    def __init__(self):
        self.arr = []
        self.minElem = float("inf")

    def push(self, val: int) -> None:
        self.minElem = self.arr[-1][1] if self.arr else float("inf")
        if val < self.minElem:
            self.minElem = val
            
        self.arr.append((val, self.minElem))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
    
sol = MinStack()
sol.push(-10)
sol.push(14)
# sol.getMin()
# sol.getMin()
sol.push(-20)
# sol.getMin()
# sol.getMin()
# sol.top()
# sol.getMin()
sol.pop()
sol.push(10)
sol.push(-7)
sol.getMin()
sol.push(-7)
sol.pop()
# sol.top()
sol.getMin()
sol.pop()