okay, a game.

two people pick stones.
each person, can pick one stone, two stones or three stones.
whoever picks the last stone wins.

the question is, if i start
can i win if i play optimally?

the optimally there is the problem?
what the hell is optimally?

i can stones.
how do i know if it's optimal?

well, you don't really,
because you don't know your opponents pick.

you can only guess.
so, ideally, i'd want to assume
what my opponent would do
to see what i'd pick.

this is excessive.
how about i explore every option,
and see if there's one where i win.

on the first one
say so.


this is deceptively simple.
how do i write it.

what's really happening.
you're taking turns.

okay, so you need to track turns.
you pick, then you see what happens next.
in essence, you're tracking game iterations.

you always start.
so, if you start with 1, what happens?

okay, consider the four stones example.
you pick one.

then what? your opponent has to pick the remaining stones.
they win.

so, you know, if you pick one, your opponent wins.

so, the return is who wins.
somebody always wins, it's just if it's you.

and so, how would the exploration go.
pick one, see what happens.
pick two, see what happens.
pick three see what happens.

