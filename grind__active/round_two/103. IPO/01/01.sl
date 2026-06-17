i want to return a number.

after receiving four inputs.

the number represents capital.

i want to pick the number of projects
that give me the most capital.

however,
i can't pick more than `k` projects.

i start with `w` capital.
to start, every project requires some capital.
i take from `w`, i start the project.
when done, every project yields profit

this profit, added to what i have left
becomes my new capital.

*

now, to solve.

how do i know what projects to pick?

well, you'd want to pick your most profitable
at every point.

and when you run out of money or reach project limit,
you stop.

is this the case?
well, yeah. i think.

let's find out.

at each point, 
how do you know your most profitable project?

it's the project with highest profit
among the projects you can afford.

two heaps.

one contains the projects you can afford
sorted by profit.

a max heap.

the other contains the projects you can't afford.
sorted by starting capital.

a min heap.

you manage the transfer from min heap to max heap
as the capital grows.

you hit project limit
or run out of projects, you stop.

it worked.

learning:
    pay attention.

    the profits array were 'pure profits'
    i didn't need to deduct capital then add profit.
    i could just add.

TODO
    see if there's a more efficient way to solve it.