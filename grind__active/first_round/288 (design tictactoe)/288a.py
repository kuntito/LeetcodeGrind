# https://leetcode.com/problems/design-tic-tac-toe/description/?envType=problem-list-v2&envId=2y96di6m

# to implement this tictactoe game, we'd need a grid to represent the board
# an nxn grid
# 
# the `move` method allows us to place a player's avatar on the board
# hence, each player needs a value to represent it
# we'd use 'x' and 'o'

# and every time we place a player's avatar on the board, we want to know if they've won

# so we'd need an optimal way of checking if a player has won
# a player has won if they have `n` consecutive avatars in 
# any direction

# the tricky bit is implementing the check for a winner
# ideally, we would explore all directions from the - 

# how many unique directions is there
# four
# the vertical, the horizontal, the forward slanting diagonal
# the backward slanting diagonal
# if we can find -

# say i have an avatar at O, how do i know if it is a winner, i explore vertically upwards looking for `n-1` consecutive same avatars
# whatever i find from there, i save it and check vertically downwards for what i need, if i find it, i know i have a winner on that line else we ball
class TicTacToe:

    def __init__(self, n: int):
        pass
        # first, the grid
        self.streak = n
        self.board = [[None for _ in range(n)] for _ in range(n)]
                

    def move(self, row: int, col: int, player: int) -> int:
        pass
        # the players are indicated by `1` or `2`, no need for 'x' and 'o', i seem to still be jumping the gun
        # what do i need? place the player on the grid
        
        self.board[row][col] = player
        
        # then check for winner
        if self.checkWinner(row, col, player):
            return player
        
        return 0
    
    def checkWinner(self, ri, ci, player):
        pass
        # we need `n` consecutive player avatars
        
        
        # vertical,
        if self.checkVertical(ri, ci, player):
            return player
        # 
        # horizontal,
        # 
        if self.checkHorizontal(ri, ci, player):
            return player
        # forward diagonal, backward diagonal

    def checkVertical(self, startRi, startCi, player):
        currStreak = 1

        # check upwards
        ri = startRi - 1
        # the loop only continues once the avatar is valid
        while ri >= 0 and self.board[ri][startCi] == player:
            currStreak += 1
            if currStreak == self.streak:
                return True
            ri -= 1
        
        # check downwards
        dim = len(self.board)
        ri = startRi + 1
        # the loop only continues once the avatar is valid
        while ri < dim and self.board[ri][startCi] == player:
            currStreak += 1
            if currStreak == self.streak:
                return True
            ri += 1
        
    def checkHorizontal(self, startRi, startCi, player):
        currStreak = 1
        
        # we're going left then right
        ci = startCi - 1
        while ci >= 0 and self.board[startRi][ci] == player:
            pass
        
        ci = startCi + 1




tac = TicTacToe(3)
print(tac.move(0, 0, 1))
print(tac.move(1, 0, 1))
print(tac.move(2, 0, 1))