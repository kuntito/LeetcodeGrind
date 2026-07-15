three inputs, one output.

parallel courses iii.

there are courses.
some courses need to be completed before others.

i know how long it takes to complete every course.

i want to find how quick i can complete all the courses.

a course can be taken once it's prerequisites are met.
several courses can be taken at once.

to solve, i'd say take courses as soon as they're available.

what makes a course available?
it's prerequisites completed, if it has any.

for every course,
i want to know it's prerequisites.

to even begin, there must be a course without prerequisites
one or more of those.

that's the starting point.

well. feels like implementation detail.
whichever way, the course you take,
must have no pending prerequisites and so,
every course eventually gets to the same state
as the starting course(s)

the question is how you represent.
well, the hashmap tells us, a course and it's number of prerequisites.

and so, you always want to take the courses that are ready.
once, you complete all those, keep track of the time it took
for the longest one.

ah, i see.
the tricky bit is, if several courses start at once.
finishing one course, means you can start another.

i'm spiralling.
***
pick any course
complete it's prerequisites, before completing it.
track the time it took to complete.

say you have four courses.

a, b, c, d

c needs a to be completed
d needs b, a to be completed

i'm having trouble understanding how to implement the minimum months.

what would minimum months look like on a high level.

this,
take a course as soon as it's available.

how do you know when a course is available?
when it's prerequisites are done.

so, i need a place to check completed courses.
okay, and how do i track the time?

the duration of a course, i'm defining as,
the time it takes to complete that course plus
the duration of it's longest prerequisite.

the definition is recursive.
so each course, needs to know it's duration.
and essentially, the course with the longest duration
is your result.

so, to solve,
create a structure of `course -> prerequisites`
for each course take all prerequisites first.
this is a post order traversal.
till you hit the base course.
at which point, you return duration upwards.

each recursive fn knows it's duration.
caching this, would be helpful.

at the end, you'd have all the courses and durations.
the longest one is what you return.

also, `duration` is a concept i invented.
the `length of a course + the duration of it's longest prerequisite`.
it's recursive in nature.
