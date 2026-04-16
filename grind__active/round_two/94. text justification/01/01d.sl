# https://leetcode.com/problems/text-justification/description/

i'm given a list of words.

i want to group the words based on a condition.

each group has the same number of characters.
let's call this `maxWidth`

however, the last group may have less characters.

the way it'd work is this:

to populate a group, i'd add the leading words from the list.
i'd add a word, then another word.

`this is where the complexity lives.. by telling myself, i'm adding a space 'tween each word, i create a problem where i then have to add more space once i see i can't add any more words to the group

the idea, at it's simplest, is you keep adding words.
the words would be separated by space.

as you add the words, you're keeping track of how much space you'd need.

and so, you can tell when you approach the max width
at which point, you can now add more space and conclude the group`