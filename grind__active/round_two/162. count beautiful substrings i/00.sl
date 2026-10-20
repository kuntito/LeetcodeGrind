what are the entities.

a string.

i want to find out number of beautiful sub strings
within it.

what's a beautiful substring?
it's one with as many consonants as vowels, and also
one where the number the product of vowel count and consonant count
is the multiple of a given number `k`.

that's a lotta words, 
but i want to find the number of substrings
that meet a given condition.
in a given big string.

that didn't come out right.
i have a string,
and want to find out
how many substrings within it meet a given condition

a substring is a back to back sequence of characters.
empty characters don't count.
one character counts as a substring, 
but would fail the condition of equal vowels and consonants

but that's besides the point.
the idea is explore every substring within the string.
and see if they meet the condition.

how do you explore every substring?
you summarise.

a substring must start somewhere
and it must end somewhere.

and what does that mean?
well, at every character in the main string.
a substring of several lengths could start there.

so a single character is the starting point.
okay, at that point, what can you do?

well, one of two things?
continue the substring or stop.

are those really the options.
well, yes.

stopping is intuitive.
and what does continuing look like?

well, you can pick the next character
well, you have to pick the next character.
since the substring is contiguous, or simpler, continuous.

so, your decisions are:

stop here
or continue.

and at some point, you'd run out of places to continue
and have to stop.

so it all stops.
and when it does, find out if your substring meets the condition.
and problem solved.

so, you explore. it's recursive.

at each point, you have a substring.
but really you care about the vowel count
and consonant count
so, is that not what i should be measuring?
well, i guess.

i also need to know what part of the main string i am.
and perhaps caching.

what does each branch tell us.
the number of valid substrings at this point.

yeah, a memo would work.
and the base case, when we run out of characters.