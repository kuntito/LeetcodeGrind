i want to return a number.

after receiving three inputs.

i have a pool of `n` workers.
i want to hire `k` of them.

i want to hire them for the least amount.
while i following the hiring rules.

there are two rules:
one,
    every worker must be paid their minimum wage.
    each worker has their going rate.
two,
    every workers wage must be proportional to their quality
    within the team.

    workers have a numerical attribute called quality.
    if a worker has twice the quality of another worker.
    they must be paid twice as much as the other worker.

i'm told each workers minimum wage and each workers quality.

**
in essence, i want to select the cheapest team.

cheap is a value of their minimum wage, and their relative quality.

i want to select a team with the lowest wage
and lowest relative quality.

can i express this as a single value?
you could, but you'd have to explore every combination
of `k` hires.

let's start with that.

