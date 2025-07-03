# https://leetcode.com/problems/basic-calculator/

# i want to implement a function that returns an integer.
# the function is called calculate and takes a single argument, 
# a string, `s`.

# `s` represents a valid arithmetic expression.
# i.e.
# "1 + 2" 
# -2+(3x5)

# my job is to solve this expression and return the result

# how do iapproach this joint?
# the way i see it, the smallest arithmetic expression has three parts.
# left operand, operator and right operand

# using PEMDAS, i'd identify all first set of expressions, solve them
# and replace them in the string with their result

# i.e. s = "2+3*5"
# the first expression is "3*5"
# which results to "15"

# now, i'd replace "3*5" with "15" in `s`
# which results in 2+15
# and this is another arithmetic expression.

# i'd recursively apply the same method till i obtain a single digit
# based on the constraints, we don't need the `E` in PEMDAS
# which means we'd work with PMDAS

# first, we need to find the smallest parentheses
# and solve for the expression within it

# once solved, we explore for all the multiplications
# what if you had 2*3*5

# the first multiplication expression would be 2*3
# if i replaced this with `6`
# the expression becomes 6*5
# then i'd handle this, it becomes `30`

# i get the gist but how do i structure it in code?
# off the dome, i'm thinking doubly linked list.

# i'd divide the string into tokens
# each token represents a linked list node
# and the value of each node can either be a number
# or an operator
# how bout parentheses?

# i guess, those could be tokens too
# say you've tokenized the string, what next?

# address the first operations
# scanning through the string, you want to find the first set of parentheses
# if there are none, you want to find the first set of multiply operators
# if there are none, the first set of additions
# if there are none, the first of subtractions
# if there are none, you're probably at the end.

# there a way to keep track of which operators?
# i mean once i scan through the operators, i want to know the operator to address first
# the arithmetic operators are the easiest
# i'd have a variable and a list of nodes
# i'd have a hashmap, with "+", "-" and "*"
# where the values are a list

# every operator node get's appended to the list
# this way i can address every multiplication first before dealing with others
# since i use a double linked list i can simply replace the expression with it's result
# in O(1) time and since, i've store the operators as linked list nodes
# i can get the left and right side in O(1) time
# the problem here, would be parentheses?

# how do i address that?
# for one, i want to address the deepest parentheses first.
# that's the first parenthesis to close.
# i can keep track of all the opens
# the moment i close one, i know i'm at the ending.

# that way i can address that expression first
# but how would this fit in to the linked list node narrative

# i get it, it'd be a recursive approach.
# a function that attempts to tokenize a string,
# the function does it's thing and tracks any open parentheses it finds
# the moment it finds a closing parentheses

# it takes all the characters in between
# and solves for that expression
# this is some messy reasoning.

# how do i approach this?
# say brute force, the only problem with my tokenizing approach is parentheses
# perhaps i'd address all the parentheses first.

class Solution:
    def calculate(self, s: str) -> int:
        pass
    
        # the idea here is to eliminate parentheses
        # i'd track the indices of all the opens
        # when i find a close, i'd have a range of characters
        # without parentheses, i'd solve the expression(s)
        # then what?
        # this is the tricky bit, what if i converted all the characters to a string first?
        # or technically the tokens thing could still work
        # rather than storing indices, i'd store the nodes
        # this way, knowing the opening parenthesis node and the closing, i can solve for what's in between
        # and replace with the result in O(1) time
        
        # this way i can address all the parentheses in one swoop
        # once done i'd run through the list again
        # do the hashmap thing for each arithmetic operator and voila, problem solved

        # first, i need a linked list node class
        # then i need an array to track all the opening nodes
        
        opens = []
        # now, i blaze through `s`
        # ignoring any spaces, since spaces are not part of the equation
        # however, how do i address negative numbers
        # i'm guaranteed there'd be no consecutive operators
        
        # therefore, `-` can only appear in front of another number or an open parenthesis.
        
        # how do i differentiate the two 3s
        # `-3 + 2` from `1-3+2`
        
        # think it's what comes before the minus sign
        # if there's nothing before the minus sign
        # then the minus sign is part of the number
        # else, the minus sign is an operator
        
        # think i can proceed
        space = ' '
        minus = '-'
        plus = '+'

        dim = len(s)
        while idx < dim:
            ch = s[idx]
            
            if ch == minus and idx == 0:
                # this is the unary operator
                # at this point i want to take all the digits after
            
            idx += 1
        
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
    def connectNeighbours(self):
        left = self.left if self else None
        right = self.right if self else None
        
        if left:
            left.next = right
        
        if right:
            right.prev = left
        
class LinkedList:
    def __init__(self) -> None:
        self.head = Node("head")
        self.tail = Node("tail")
        
        self.head.right = self.tail
        self.tail.left = self.head
        
    def addNode(self, node):
        self.tail.next = node
        node.prev = self.tail
        
        self.tail = node
    