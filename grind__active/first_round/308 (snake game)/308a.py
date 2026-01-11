# https://leetcode.com/problems/design-snake-game/description/

from collections import deque
from typing import List


# we want to build a snake game
# we're given a class `SnakeGame` and want to implement two methods

# the constructor that takes three arguments, two integers representing the width and height of the game screen and a 2d integer array that represents the food for the snake.

# we're told the snake starts at position (0, 0) with a length of `1`

# food[r][c] represents a position on the screen where food appears for the snake, when food appears, the length of the snake increases and so does the score on the game.

# the snake length and game score both increase by `1`

# let me say what i understand by the question.
# we're given integers, width and height representing the dimensions of the board for the snake game

# the snake starts at position (0, 0) with a length of `1`

# the array food, contains coordinates, each food[i] is essentially [r, c]
# some row and column on the board

# when the `move` method is called, the snake head proceeds one unit in the specified direction. if that new position is the same as food[0]
# then the snake grows longer by one unit and the score of the game increases by `1`

# if the new position is not food[0], nothing happens
# everytime, `move` is called, we also return the current game score

# if the game is over, we return `-1`

# i know i'd have to create a 2d grid representing the board, and track the current location of the snake
# perhaps it's easier to place the snake on the board
# i'd represent the snake with "#"
# everytime the snake grows, i'd increment the hashtag

# but in which direction
# [#, food]
# [-,   - ]

# consider the following, if we moved right, the snake has to grow
# the head remains the same but it snake grows in the opposite direction of which it moved
# technically, we need to know the tail of the snake too

# [ #, # ],
# [ -, - ]

# what if it's not possible to grow the snake in the opposite direction of the food
# consider the board
# [ -, f, # ]
# [ -, -, # ]

# when we turn left, we eat food
# i think i get it now, we don't need to extend anything
# the location of the food becomes the new head of the snake.

# the rest of it, remains exactly where it is
# i've figured out how the lengthening works

# next thing is how does the snake turn
# [-, #, #]
# [-, -, #]

# how would i communicate moving left in this case?
# if it's a straight line, it's easy to move the snake
# but when it bends

# well, i know where i need to be, i just need the tail block
# to go where the penultimate block is
# simple follow the guy infront

# do i store the snake on the board, or simply a chain of positions?
# at any point, at most two positions change
# a double ended queue is brilliant

# for a movement, i just need to add the new position to the start of the queue
# and pop the last element from the deque

# we should keep a set of the snake positions so we can know when the snake runs into itself
# i don't think i need to create the board

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        
        self.snakeQueue = deque()
        self.snakeSet = set()
        
        origin = (0, 0)
        self.snakeQueue.append(origin)
        self.snakeSet.add(origin)
        # for O(1) access to the topmost food
        food.reverse()
        self.food = food
        
        self.score = 0

    def move(self, direction: str) -> int:
        snakeHead = self.snakeQueue[0]
        
        r, c = snakeHead
        if direction == 'U':
            r -= 1
        elif direction == 'D':
            r += 1
        elif direction == 'L':
            c -= 1
        else:
            c += 1
            
        # if the new position is out of bounds
        if r < 0 or r == self.height or c < 0 or c == self.width:
            return -1
        
        newPos = (r, c)
        
        # if the new position is in snakeSet i.e. the snake runs into itself
        # this is tricky, if the snake moves to where it's tail is, technically
        # technically (r, c) is in self.snakeSet but the snake wouldn't run into itself since the tail would also move
        
        # so we should pop the last element
        # yes, but what if we eat food
        
        # so there's two scenarios, one where we eat
        # and where we don't
        food = self.food[-1] if self.food else None
        if food and r == food[0] and c == food[1]:
            # now we have food, what's the situation
            # we simply increase the score
            # and remove the food
            self.score += 1
            self.food.pop()
        else:
            # we don't have food, so we pop the last element from the queue
            lastPos = self.snakeQueue.pop()
            self.snakeSet.remove(lastPos)
            
            if newPos in self.snakeSet:
                return -1
            
        self.snakeQueue.appendleft(newPos)
        self.snakeSet.add(newPos)
            
        return self.score
    
    
sol = SnakeGame(3, 2, [[1, 2], [0, 1]])
print(sol.move('R'))
print(sol.move('D'))
print(sol.move('R'))
print(sol.move('U'))
print(sol.move('L'))
print(sol.move('U'))
