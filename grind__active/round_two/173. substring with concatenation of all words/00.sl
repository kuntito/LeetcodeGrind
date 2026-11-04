okay, i have a list of strings.

and want to find out if these strings occur as a group
within a given string.

so, my list could be ["ab", "cd"]
and the given string could be "cdabab"

does my list occur as a group within the given string.
well, the group would be "ab", "cd" in any order.

and the given string does contain "cdab"

so yes.

we have one.
do we have another?
no.

so, the ask is to take the list as a group.
and find the groups occurences within the given string.

i'm to return the starting indices of these strings.
i know the list items all have the same length,
so i know the group i'm looking for.

okay so, what do you suggest.
explore every index of the given string.

at each index, you know how many characters you're looking at.
then break up the characters into list item chunks.

then ask if every chunk is in the list.
if yes, you have a valid group.

that's one index.
repeat.
