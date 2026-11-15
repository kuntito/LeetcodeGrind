i have a queue of numbers.

in how many ways can i select a chunk from that queue

where the chunk has a `k` unique numbers?

****

so, what's the plan?

well a sliding window.
but how would it work?

consider, `121` where i need `2` unique numbers.

the chunks are:

`12`, `21` and `121`

say i start with `1`
i increase the window, i have `12`
i have one value.

now, i increase the window to `121`
the condition remains valid.

but how do i find the `21`?
not sure, what comes to mind first.

is starting the window at every number.
then what?

keep going till you stop.
it'd be inefficient, but should work.

this had a TLE.
apparently, they want the count.

not the elements themselves.
does that simplify things?

you'd still have to explore every window.
well, do you?

i'd watch a video.
