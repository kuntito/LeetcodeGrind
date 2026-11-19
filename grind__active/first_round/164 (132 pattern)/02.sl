i'm given a list of numbers.

no, i have a queue of people.

i wanna know if within the queue.
there's a short guy followed by two taller guys.
where the first guy is taller.

so, how would you go about this?
well, you'd start at the short guy.
he can see the guy taller than him.
but not the other one behind the guy taller than him.

so, it can be an alley oop.
short guy asks tall guy.
yo, behind you, is there someone taller than me.
he says yes.

you have your pattern.

***

and how would you write this code?
well, short is relative.
so, you'd really just start from the first guy you see.
and the question is.

who's the next person taller than me?
you find that guy, and ask him a question.

let's write it, see what happens.

okay, i got what they're asking.
and TLE.

so, how can i make it efficient.
the first iteration, where i take on
each maybe short guy is necessary.

the part where i ask, who is the tallest after me
is where things get dicey.
several people could fit the bill.

and it's not clear from where i'm standing.
well what if,
all the guys knew if the tallest shorter person after them.

wouldn't this solve the problem?
well, it'd make it easier.

so, how do you converge on that solution.
each person, needs to know the tallest guy after them.

so, you can track 