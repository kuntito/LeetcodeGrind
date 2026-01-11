# https://leetcode.com/problems/design-tic-tac-toe/

# what's the challenge? we are to implement a TicTacToe class
# the constructor takes an integer argument determining the board dimensions
# rows and columns

# and we are to implement a function `move`, it takes three integer arguments
# row, col and player
# row and col represent a position on the board
# and `player` represents the current player who made the move

# the `player` is either `1` or `2`
# every time a move is made, the `move` function checks if a winner has emerged
# and returns the player id of the winner i.e. 1 or 2
# if no winner, return 0

# a winner emerges, if a player has `n` consecutive vertical, horizontal or diagonal moves anywhere on the board

# once a winning condition is reached, no more moves are allowed
# not sure if this is extraneous info or the testcases would try to move after a winner emerges, since it doesn't say, i'd keep a global state for when a winner emerges and return 0 for any moves made after that.


class TicTacToe:
    def __init__(self, n: int):
        # first thing is create the board
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.isWinnerEmerged = False

    def move(self, row: int, col: int, player: int) -> int:
        if self.isWinnerEmerged:
            return 0
        # all moves are guaranteed to be valid and `row` and `col` are valid indices, that said, we can simply place the player's on the board

        self.board[row][col] = player

        # now we check for winner
        # the idea here would be to explore in all directions
        # technically there's eight directions, up, down, left, right, up left, down right, up right, down left

        # we can pair the directions up (up, down), (left, right), (upLeft, downRight) and (upRight, downLeft)

        # what would happen is for each pair, we'd explore both directions as long as the value there is equal to player
        # we'd have declared a variable streak, initialized to `1`
        # and increments whenever we find another similar consecutive player cell
        # the exploration stops in either direction if we run out of cells or encounter a cell that's not the current player
        res = self.exploreWinner(row, col, player)
        if res > 0:
            self.isWinnerEmerged = True
            
        return res

    def exploreWinner(self, row, col, player):
        # we can pair the directions up (up, down), (left, right), (upLeft, downRight) and (upRight, downLeft)
        upDown = ((-1, 0), (1, 0))
        leftRight = ((0, -1), (0, 1))
        upLeftDownRight = ((-1, -1), (1, 1))
        upRightDownLeft = ((-1, 1), (1, -1))

        pairs = (upDown, leftRight, upLeftDownRight, upRightDownLeft)
        maxRows, maxCols = len(self.board), len(self.board[0])

        # those is the four pairs
        for dirOne, dirTwo in pairs:
            streak = 1
            ri, ci = row + dirOne[0], col + dirOne[1]
            while (
                ri >= 0
                and ri < maxRows
                and ci >= 0
                and ci < maxCols
                and self.board[ri][ci] == player
            ):
                streak += 1
                ri += dirOne[0]
                ci += dirOne[1]
                if streak == self.n:
                    return player

            ri, ci = row + dirTwo[0], col + dirTwo[1]
            while (
                ri >= 0
                and ri < maxRows
                and ci >= 0
                and ci < maxCols
                and self.board[ri][ci] == player
            ):
                streak += 1
                ri += dirTwo[0]
                ci += dirTwo[1]
                if streak == self.n:
                    return player

        return 0


sol = TicTacToe(3)
print(sol.move(0, 0, 1))
print(sol.move(0, 2, 2))
print(sol.move(2, 2, 1))
print(sol.move(1, 1, 2))
print(sol.move(2, 0, 1))
print(sol.move(1, 0, 2))
print(sol.move(2, 1, 1))


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
