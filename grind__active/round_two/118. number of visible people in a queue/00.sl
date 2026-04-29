# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

i'm given an array of integers.

each integer represents the height of a person.

my task is to find out how many people each person can see to their right.

***

i'm given an array of integers, `heights`.

each element represents the height of a person.

my task, is find out, for each person, when they look right, how many people are visible to them?

each person can see everyone on their right, as long as they're not being obstructed by someone taller.

and how would this go?

each person needs to know who they can see rightwards.

the first instinct is for each person, iterate forwards and count how many people can be seen.

i imagine that would fail due to TLE, but let me try first.

what would the check for visible persons look like?

well each person, can see their immediate neighbor and anyone taller than them.

it's a case of count every neighbor that's taller than the last.

my algo failed miserably.
perhaps, i didn't understand the condition.

what actually dictates that you can see someone.

the failed test case is:
[10,6,8,5,11,9]

and for the second position with height `6`
i reported that it can see two people.

according to me, the person with height `6` can see the people with height `8` and height `11`

but the example says they can only see one person.

let's review the conditions for seeing a person.

it says the ith person can see the jth person if whoever's smaller between the ith person and the jth person can see everybody in between them.

what does this mean, let's make things clearer.
rather than ith and jth, let's use the left person and the right person.

the left person can see the right person, if the shorter between them is taller than everybody between them.

let's address this one at a time.
if the left person is shorter, they need to be taller than everyone in between.

