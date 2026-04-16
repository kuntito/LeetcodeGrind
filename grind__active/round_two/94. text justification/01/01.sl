# https://leetcode.com/problems/text-justification/description/

i'm given two things, a list and a number.

the list is a list of words.

what i want is to make those words into a block of text,
where each line has a maximum amount of characters.

that's where the number comes in. it's called `maxWidth`

to make the block of text, i'd have to generate each line.
to do this, i'd take the leading words from the list and place on the line.

every word should be separated by a space character. i'd keep adding words to the line until i can't add any more to the line without exceeding the max characters.
