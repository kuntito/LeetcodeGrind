https://leetcode.com/problems/word-search-ii/description/

i'm given two things.

a 2d grid of letters, the abc's

and a list of words called `words`

the 2d grid is called `board`

my job, i want to find the words in `words` that exist on the `board`.

and how would that go? what does it mean to exist on the board?

well, for a word to exist on `board`, it means the characters that make up the word exist on the board such that each character is connected to the next vertically or horizontally.

also, without repitition of cells. if the word is `meek`, both e's would have to be in different cells.

**
and how would this work in code?
well, what am i trying to do?

i want to find out if the words in `words` exist on the board.
surely, you're not checking all the words at once.

you'd do one after the other.
so, how would it go?

i'd pick the first word from `words` and ask, is this on the board?
then do the same for every other word till i run out of words?

i could.

what would that look like? for each word, i'd run through every cell on the board.

what am i looking for? cells containing the first character of my target word.

and what happens when you hit each cell?
i explore the cardinal directions, up, down, left, right, if those cells have the next character in my target word.

i'd also track the cells i've visited so i don't double visit any cell.
i keep going till i run out of cells or run out of characters.
if i run out of characters, good. the word exists.

if i run out of cells, bad. the word does not exist.
at least not from where i started.

okay, seems decent enough.
scan the board for cells that contain targetWord[0]

for each one, start a recursive exploration in four directions.
track what you find.

the initial exploration for the board cells could be cached.
a dictionary of characters => list of cells

say the letter a is at topLeft and second topLeft

a => [(0, 0), (0, 1)]

this way, as i check every word in words, if i find a word with `a`
i immediately know where to start.

