what can i say i've deduced from this problem?

first define it.

`
i have a string,
containing uppercase characters.

i want to return the length of the longest streak of characters.
a streak is back to back same characters.

i.e. 'AAA' is the longest streak in 'BBAAA'
`

i'd say this is a good starting point.
then context.

i'm allowed to change characters within the string,
why does it feel problematic adding this.

cause it changes what i have in memory
in a way that makes me uncomfortable.

the case is, i have a string.
a string where i can make replacements.
replacements to it's characters.

i can take any character and replace it with 

actually,
i have a string.
a string where i can change it's characters.

actually,
i'm given a string.
and told i can change any of it's characters.

but i can only make `k` changes.

my goal is to find the longest streak of characters
back to back characters.

and since, i can change up to `k` characters,
it means, i can affect the longest streak within the string.

is this case?
it still feels like it's missing something.

as the string exists, it has a longest streak.
you can have a longer streak if you replace characters.

no.

you have a string.
of uppercase characters.

i.e. ABCDE

when characters appear back to back within the string.
we can call them a streak.

i.e. ABCCDE has a streak of 2, `CC`

several streaks can appear within the same string.
ABCCDCCE, here there's two streaks of 2, 
the `CC` after AB and the `CC` after D

several of these streaks can occur.
but we want to find out what's the longest streak
we can create if we can modify the string.

let's reconsider this:

ABCCDCCE

here, we have two streaks of CC.
now, if we can modify the string,
and replace the `D` with another `C`
we'd have a streak of `5`

ABCCCCCE

changing characters can lead to a longer streak.
so, the question is.. 

what's the longest streak that can be formed within the string.
if i can change up to `k` characters.

how would i know this?
what characters would benefit from replacements.
well, ones where existing characters are not separated by more than `k` characters.

the idea is to fill in the gaps between similar characters.
well, the most popular characters within a window.

what window?
well, a window of gaps.

what do you mean?

if you have ABA
as far as A is concerned, B is a gap.
and that gap gives it a longer streak.

and what about B?
B would cost more changes.
it does have gaps on it's left and right, 

but it's simpler to fill As gap than to fill Bs gap.
since A has less.

so, it's a question of, what's the most popular character in the string
and how many gaps does it have?

well, not quite.
you want the most popular character
with not more than `k` gaps.

how do you define this?

looking at the string.
do you ask what's the most popular character in the entire string?
then find out how many gaps in there?

if you had:

HOFOBTBYHGRGWLFCZTVTPVCNTDWKIVLMVMSCTFXCMLYAMPAUHBLAFTSUCBLJRJZBOWFVTBKOKNVCSTFZMPD

and `k` was 2.

you could only replace 2 characters, no point searching the entire string.
since, it's unlikely to cover all the gaps with just 2 changes.

i know that because i see the string.
but you wouldn't be able to see the string in your test cases.

and so, what's the approach here?
if you picked the first character, you can explore at most 2 characters ahead.


so, say you pick H, your range extends to HOF

since, k is 2.

now, your window is HOF.

what can you deduce here, the most popular characters
are all three.

nobody is more popular than the other.
your longest streak would be three here.

however, you change the characters.
so what do you do now?

well, we'd need to explore another window.

so what, we move the window rightwards.
leaving out the initial H.

really?
what if the H could merge with other things.
well, that's a fair point.

say the string was:

HOFHH

this would mean replacing the OF with HH would give us a longer string.
but i never bothered to check.

but i wouldn't know to check till i saw the next H.
so what do you say?

if at HOF.
i have three characters.

nobody's more popular than the next.
then the best streak i can get is 3.

now, i know that's the best i can get here,
so i'd have check other characters.

now, i don't just move the string
because what if the next character was an H like we discussed.

what i'd do is expand the window and if ...

i just got an insight, 
and i don't know if this helps my mission
of step by step guidance.

the idea, is you have a window of `k + 1`
that's the worst case.

you have a single character and exhaust k filling the gaps around it.
now, you want to increase your window.

you're allowed to increase your window, if your gaps don't exceed `k`
which is the case that catches the HOFHH

since the starting window is k+1, 3.
then HOF is your first window and the gap is 2.

when you expand to HOFH, your gap remains 2, so that expansion is valid.
when you expand to HOFHH, your gap remains 2, so the expansion is also valid.

now, what happens when the expansion is no longer valid.

say you have a HOFHHA
at that point, your gap becomes 3.

you have to drop one character.
who do you drop? the leftmost character?

well, maybe?
you definitely want to drop from the left,
but what moves the needle is number of gaps.

you want to reduce the gaps to at most 2.
so you keep dropping characters until the gap is acceptable.

does this solve the problem?
well, let me write the code.