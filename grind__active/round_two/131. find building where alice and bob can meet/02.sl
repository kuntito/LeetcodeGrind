i didn't define it properly in `01.sl`

two people.

one on the left, one on the right.
they want to have a meeting.

to do this, they'd have to be in the same building.
if they aren't, they'd have to move.

however, there's rules to moving.
each person can only move right,
and each person can only meet in a building,
taller than where they left.

given a list of starting positions.
i'm supposed to find the first building
where a meeting can occur.

and if a meeting can't occur, i'd return -1.

bruteforce first.

at each turn, you want to check,
if same building, don't move.

if not, where are you moving to.
well, a building taller than the taller between them.
and the same building has to be after the further one.

well, only the left person has to move.
the right person might need to move, for building height reasons.