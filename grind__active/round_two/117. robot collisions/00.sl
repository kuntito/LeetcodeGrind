# https://leetcode.com/problems/robot-collisions/

i'm given three things and want to return a list of integers.

what are those integers?
what are the three things?

how does the magic happen?

it might be simpler to understand without talking about the three things right now.

what's happening is, i have robots littered on a line.

each robot is moving in one direction, either left or right.

based on the robots movements, they might collide with another robot.

when a collision occurs, i'm to consider the health of the robots involved.


***

there are robots on a line.

the robots are moving.

either moving left or moving right.

if two robots are facing each other, a collision would happen.

when they collide, something interesting happens.

each robot has a health, it's represented by an integer.
when two robots collide, 
    the robot with the lesser health is removed from the line.
    the second robot has it's health decreased by `1`

    what happens if the health hits `0`, it's not stated.

    another scenario is if the robots have equal healths.
    if this happens, both robots are removed from the line.

after every collision, the remaining robot, if it exists, keeps moving in the same direction it was before the collision.

my job is to return the health of any remaning robots after all collisions have happened.

and i'm to do so in the same order as the robots were presented to me.

the robot positions on the line are represented by an array, `positions`
each position is unique.

the robot healths are represented by an array, `healths`

and the direction each robot is moving, is represented by `directions`

all three arrays are the same size and their respective indices refers to a single robot.

robot 0 is at position[0], has health[0] and is moving in directions[0]

`directions` contains the strings, 'R' or 'L', indicating right and left.

how do i approach this?
for one, i'd say collate each robot's properties into one.

Robot(
    position,
    health,
    direction
)

now, i need to find any collisions.
the first collision would be between
the furthest robot moving right and the next robot moving left after it.

once that collision happens, i sort it out.
and move on.

moving on is the same step, the furthest robot moving right, and the next robot moving left after it.

in essence, i want to address each robot moving right in reverse.
from the furthest one downwards.

and i need to know the next robot moving left after it.

i need to maintain an ascending order of left moving robots.
this lends itself nicely to a min heap of robot positions.

robot positions of left moving robots.

let's not get hasty.

the first thing you want is to track right moving robots.
you can put this in an array.

you can then treat each right moving robot in reverse.
for the first one, the question is, what's the first robot after me that's moving left.

now, how do you find this?
you could simply continue the iteration.

once you find that robot, one of three things could happen.

the right robot wins, the left robot is removed.
    the iteration for the next left moving robot continues
the left robot wins, the right robot is removed.
    in this case, i go backwards to the next right robot
    then restart the iteration.

    it would have to collide with the left robot that just won.

the third case, both robots are removed.
    in which case, i still go backwards to the next right robot
    then restart the iteration.

    this time, i'm looking again for the next left moving robot.

R R L R

and what happens if you never find a left moving robot?

***

i feel like i'm making this more difficult than it needs to be.
the directions is where it's at.

it's a series of Rs or Ls.
whenever i have an RL

i have a decision to make, once i make the decision, i'm left with an R or an L or nothing.

if i have an R, i keep moving
if i have an L, i check the previous element for an R

if i find an R, i have another decision to make.
i keep doing this till
    * i get an R
    * or i run out of previous directions.
in which case i keep moving.

and at the end, i'd have my result.

***
one mistake i made is thinking a collision only happens with `RL`

when in fact, `LR` is also a collision.

the first collision, is the first direction that meets an opposing direction.
and as long as the directions oppose, collisions keep happening, till all directions are the same, or the there's nothing to collide with.


***
still wrong.

yeah, this would need a rewrite.
the first assumption was correct, the first RL combination is what i should seek.

the problem was, i didn't consider the starting positions.
my initial algo only works, if robots were sorted in ascending order according to positions.

what happend with the LR case, was a robot started at 13 and was moving left
the second robot started at 2 and was moving right, so a collision would happend.

i didn't investigate and blindly wrote another algo to solve the question based on opposing directions.

the shape of the right answer would be sort the arrays based on position.
then implement the RL collision algo.

the concern right now, is storing the original order of the positions.
to be fair, i could modify positions and pair each position with it's index.

sort positions..
it'd have to be a three way sort.

one alternative is combine all three iterables into one tuple.

(position, health, direction)

you can add one more element for original index.

(position, health, direction, ogIdx)

now sort based on position.
then implement your RL algo on this.

then you can retrieve the original indices.