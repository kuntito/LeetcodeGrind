okay, let's name the stops.

a, b, c, d, e.

i start at a and run out of money at e.

what's to say, starting at c also means i run out of money at e?

what if b was a very negative number.
well if it was it would have at most equalled a.

since the streak didn't stop.
it means starting from a you can reach c.
and so, starting from c, you can reach e.

well, what if c was negative.
what would that mean?
well, you wouldn't be able to make progress from c.
you would never reach e.

so, why's it relevant.
and keep in mind, my answer does use Kadane.

i just know how how to walk to the intuition of the optimal solution.


actually, it doesn't mean starting from c
you can reach e.

it means, starting from c.
you can't pass e.

and so, it's a start and stop.
you start at any number, and you track a stop.

a stop becomes the starting point for the next.
and you keep going.

and so, if you reach the a stop, what do you do?
start on it.

but how does the entire loop stop.
when you've explored the last stop.

you started somewhere,
and so your last stop has to be the cell before it.

and what if your best sum was circular.
around the starting point.

but how would this work?
if the sum wrapped round,
then that case, would be the best sum
since, it's all characters.

for the best sum to be across that pivot.
it would mean the sum stopped somewhere in the middle
and we would have explored the starting point.

it's basically start anywhere,
when you stop, start right there.

and keep going till you hit the first stop that's 
past the starting end point.

