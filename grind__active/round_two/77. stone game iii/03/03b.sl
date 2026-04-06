two people are playing a game.

their names are Alice and Bob.

the game is this:

there's a queue of numbers.
the queue is a mix of positive and negative numbers.

the players take turns picking from the queue.
and every number they pick, adds to their score.

a positive number, increases their score.
a negative number, decreases their score.

there are two conditions to picking from this queue:
    the part of the queue they can pick from
    how many numbers they can pick

they can only pick from the start of the queue.

and when they pick, they can pick at most three numbers.

they can pick one number
pick the first two, OR,
the first three.

but they must pick.

the game ends when there no more numbers to pick.
and whoever has the highest score wins.

if they have the same score, it's a tie.

my job, is to write the function that finds out the result.
if Alice plays first and both players always make the best move available.

TODO
  One gap — you never say whose turn goes first when the game starts, or that they alternate. You mention "they take turns" but it's easy for 
  a reader to miss that Alice goes first and Bob follows.

  Worth one line after "the players take turns picking from the queue." Something like — Alice goes first, then Bob, then Alice again, back   
  and forth until the queue is empty.