there's two groups.

the members are lined up.
left to right.

each member can do one of two things.

remove any opponent from the queue.
or, announce victory.

however, victory can only be announced
if the people left in the queue are all from the same group.

so, really, they can only do one thing.
ban, until, only their group members are present in the queue.

so, everybody's simply banning the next.

so, what's the optimal strategy

at each person, you ask,
does the queue only contain my members.

if yes, announce a winner.
if no, ban somebody.

and if there's nobody to ban.
well, it means, the queue only has your group members.

mutally exclusive as the saying goes.

is there an advantage to banning any one in specific?
i don't wanna think about it.

i'd write this, see what happens.

how do you want to structure the people?
a linked list fits nicely.

and a hashmap for each group.
each node is a person.

and you can check if the queue only contains your members.
if their hashmap is empty.

else. remove anyone from their hashmap.
you can't easily do that with a hashmap.

how about two min heaps.
the indices lead for each party.

heck, you don't need the original queue.
the heap is the queue.

you can deduce who's next in from the heap.
whoever has the lesser index.

for each person, check if the other group is empty.
if yes, declare winner.

else, remove someone from the next group.

i don't really need a heap do i.
two lists would be fine.

long as i can get the smallest index first.
you could arrange the indices in descending order
so you can pop.

i got the idea but TLE.

wanna do it again. i ended up using a deque
two deques per group really.

one set, is the one i'm iterating through.
the other holds what i've iterated through.

i'm considering using a two deques not four.
one holds, what i'm iterating
another holds what i've iterated.

i'd keep a globalCount of both groups.
once i hit zero for one.

i'd have my answer.
then while iterating, if i hit one group
and both groups still have members.

i take not, that when next i see a member of the opposing
group, i remove them.
