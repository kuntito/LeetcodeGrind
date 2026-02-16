# https://leetcode.com/problems/maximum-frequency-stack/

# what's the situation..
# i want to design a stack.

# a stack that always pop the most frequent element
# that's not exactly a stack is it.

# yeah, it's a frequency stack.
# i'd misread the question title.
# my bad.

# i want to design a frequency stack.
# it stores integers.

# and has two operations, `push` and `pop`
# the `push` method adds an integer to the stack.
# the question says, adds an integer to the top of the stack.
# but the concept of top doesn't really matter here.

# since, it's not a regular stack.
# perhaps the name stack is misleading.

# the `pop` method removes and returns the most frequent element in the stack.
# if there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# okay.. i see. perhaps, the order does matter.

# in essence, i want to store elements by frequency and recency.
# at any point, the `pop` method is asking..
# what's the most frequent and most recent integer added to the stack.
# once i return this element, i'd have to update the frequencies of the other elements.

# the `push` operation, would have to consider recency and frequency while adding elements.
# a hashmap can help store the frequency of each element.

# and we can use a variable, `self.maxFreqElem` to track the most frequent element
# but you also need recency.

# you can have an internal counter to give each new element a number
# and that number would increase with every new element.

# okay.. say you've stored these elements in the hashmap
# how would you get the most frequent and most recent element.

# well, our variable handles that..
# the challenge would be updating the variable..

# when you take out the most frequent and most recent element
# you'd need a new one.

# how do you determine a new one..
# search the hash map again?

# what if i did store each element in a regular stack
# this naturally handles the recency.

# yes, but frequency?
# what if i 

class FreqStack:

    def __init__(self):
        pass        

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass
