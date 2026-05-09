so, i want to compare my algo with Neet's

what did i do that he did differently?

his is, each recursive function returns the smallest max along all paths.

mine is, i used a global variable for smallest max.
and from the root call, i passed a variable that tracks the max along the path.

the variable goes from root to the leaf call.

i mean both work, but his, i'd argue, more elegant.

in both cases, i'm exploring every variation of a split, and for each variation, i'm exploring all the variations for the next split, unless it's the last split.

in which case, i stop.

the difference, is in consolidating the result.