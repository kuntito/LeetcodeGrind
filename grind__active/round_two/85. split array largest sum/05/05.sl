next solution, Neet used dynamic programming.

and the solution does pass, i'd just like to pick it apart and understand why?
and how dynamic programming even applies here?

the cache is on `startIdx` and `splitsLeft`

but how can you repeat this work?

say you have to make three splits over this array,

[2, 3, 4, 5, 6]

the first two splits could pan out this way:

[2] & [3, 4]
[2, 3] & [4]

in both cases, you'd hit [5, 6] with the same data.

same startIdx
same splitsLeft

in this example, it's the last split, but if there were more splits.
the repeated work is obvious.

could i have done the same with my algo?

not the way i wrote it, or perphaps i could?
but this is trying to make sense of pig sty.

not optimizing that.

i wrote my version of neet's dp approach to verify i understand it.