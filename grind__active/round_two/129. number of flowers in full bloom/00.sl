i want to return a list of numbers.

after receiving two inputs.

***

i have some flowers.
people come to see them.

`n` people are coming
at different times.

when each person arrives,
i want to find out how many flowers would be in full bloom.

this number per person,
is the list of numbers i return.

***

so, a solution

when each person arrives,
what flowers are blooming?

well, heap.

i know when each flower blooms.
i know when each person arrives.

take a person.
the first person to arrive.
look at arrival time.

what flowers are blooming then.
might have to keep popping from the heap
to find it.

when you do, put in an array.

repeat for other persons.
and there you go.

return the array.

TODO fix TLE.

also, had to debug the if conditions.
i didn't match arrival to bloom time.

i did

`bloomStart < arvTime < bloomEnd`

it should be:
`bloomStart <= arvTime <= bloomEnd`