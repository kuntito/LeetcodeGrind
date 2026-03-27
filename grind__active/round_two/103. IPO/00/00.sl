i'm given several projects.

for each project, i know two things.
how much it costs to start it.
how much i'd make when done.

these are called `capital` and `profit`.

i'm told to pick a given number of projects that'd give me the most profit.

i'm also told how much i start with.

all said and done, what's the first step.

well, i can only pick a project i can afford.
so, step one is pick the project you can afford.

what if there are multiple ones?
well, i'd want to pick the one that allows me gain the most profit in the long-run.

and what would in the long-run mean?
it means, if i pick one project, 
every further project it allows to pick
ends up being the most profit i can make within my constraints.

and how do you know this from the jump?
you don't.

so i'd have to explore each one.
***

what would the code look like?

i'd need a variable to hold how much i have, `myCapital`

i'd need to track how many projects picked.
i can use the max projects i can pick, turn it to `projectsLeft`
then decrement. when i hit `0`, i know i've picked all the projects i can pick.

i'd need to track available projects.
the projects are presented as two arrays.

`profits` and `capital`
their indices refer to the same project.

the project 0, has profit[0] and capital[0]
but what do i care about when picking projects.

just the cost really. the capital.
i only care about the capital after i've picked the project.

i want to pick each project in order of affordability.
i'm thinking a `minHeap` of items, (capital, idx)

this way, the tip f the minHeap lets me know the cheapest project in my vicinity.

and once i pick the project, i update my profits.
i'd need a variable for profits, `profitMade`.

i'd update my capital, then pick another project.

it's giving backtracking.
for each project i can afford, i'd explore further projects.
each project chosen is a different path.

i'd explore one till then end.
come back. the come back is the backtracking bit.

for each step, i'm doing the same thing.
can i afford the cheapest project, if yes.

start another recursive call.
each recursive call would have

(capitalLeft, minHeap, projectsLeft)

the exploration ends if i have zero projects left.
or i can no longer afford any projects.

at that point, i'd update `profitsMade`
then backtrack.

when i come back, i want to pick the next project i can afford.
it's important i don't add the project i just explored to the heap
so i don't pick it again.

so, i'd need some place to keep explored projects at each step, `exploredProjects`
it's only when the tip of the minHeap has an unaffordable project,
that's when i can re-add the contents of `exploredProjects` back into the minHeap.