# https://leetcode.com/problems/number-of-atoms/description/

i'm given a string and want to turn it into another string.

the input string represents a chemical formula.

what's a chemical formula?
the question assumes i already know what it is.

it attempts to explain, 
but does so, as though i already know what it is.

and so, i can simply explain a chemical formula my own way.
the carry on with the question.

a chemical formula is a string.
it's typically used by scientists to represent chemicals.

structurally, it contains letters and numbers.
but the letters mean things

***

i'm given a string and want to return a string.

***

i'm given a string and want to return a string.

***

i'm given a string.

i want to do something with the string.

when i'm done, i would get another string.

i want to return that string.

okay, but what am i doing with the first string.

i'm told that string is a chemical formula.

what does that mean?

in abstract terms, it's a string that contains groups of letters and numbers indicating how many of each group exist.

i say group of letters, but a single letter is also considered a group.

the giveaway for each group is the first letter is uppercase.
and every character that follows is lowercase.

for context, the following are chemical formulas

*H20
*Na2CO3

***

i'm given a string.

i want to explore the string.

when i'm done, i want to return another string.

the another string, is a result of my exploration of the first string.

okay, so what am i doing during the exploration?

i want to count the elements within the string.
then take the counts of each elements and represent them as another string.

okay, but what's an element?


***

i'm given a string, `formula`.

i want to carry out some instructions.

and in the process, generate another string.

the generated string is what i'd return.

but what are these instructions.

before addressing that, you need to know what `formula` represents.

the question says it's a chemical formula but it can be explained without that.

what you have, is a group of letters.
several groups within the string.

then you have numbers and parentheses to describe how many of said groups exist.

***
the string contains short names,

the names can vary, one or more characters.
although, they are typically 1-2 character names.



each name begins with Uppercase.

that's how you identify a name.
if it has more than one character, every next character is lower case.



some examples are:
A
Db
Ceg


all three are valid names.

names can have numbers next to them.
the numbers represent how many copies of the name exists within the string.

for instance, 

A2
Db2
Ceg

also, if a name doesn't have a number next to it, it's assumed there's only one copy.

my job is to figure out how many copies i have of each name
the return the result as a string.

a string formatted like this, 
all the names are sorted in alphabetical order
and after each name, i have it's count

so for the example above, my final response would be:
A2Db2Ceg


you can also add parenteses... TODO finish the explanation
