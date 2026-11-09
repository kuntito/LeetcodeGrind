i wrote the solution before writing the code.

i saw it and saw a sliding dictionary window.

i have a two strings.

checkString, and targetString.

the string really is a line of characters.

so, perhaps it's easier to say,
i have two groups of characters.

i want to find the points where one group exists in the other.
i'm told which group is which.

i'm tryingt to make this too abstract.
i have a string.

but i can't make progress if i don't define it.

you have a group of characters.
you told to identify this group
in another group of characters.

the group is the same.
if the items are the same and occur together.

so reordering the group members is still the same group.

i saw this a sliding dictionary window problem.
the dictionary tracks the group it's seen.

every person added..

not doing this.
the question is solved.

till next time.

the approach though.
an elastic dictionary.

i know the group members.
so i run through the new group.
if i see a group member, i note it in the elastic dictionary.

once i have a valid group, i note it.
if i see an unknown member, i dismiss the group i've been tracking.

this unknown guy breaks the streak.

once i have a valid group,
and see another group member.

i'd have to offset members
till the group is valid again.

# maybe start here
so, run through the new group
tracking a streak.

if the streak hits the target.
note it.

if something breaks the streak
restart the streak.

the streak can only be as long as the target
so, any new members have to trim the streak
till they fit.

since each streak has a max count per member.

i think i nailed it though.