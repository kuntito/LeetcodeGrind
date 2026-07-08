i have a string, i want to turn it to another string.

but i have to turn it in a specific way.
i'm changing the string by changing individual letters.

i can change up to `k` letters.

after the change, 
i want to see how many of the same characters form a streak.

***

i have a string, i want to turn it into another string.

really?

well, no.

i have a string.
i'm told i can change any of the characters.
however, i have a limit on how many changes i can make.

my aim, is to change characters
such that i form the longest substring of repeating characters.

***

i have a string.

let's start backwards.

i want to return the number of repeating characters.

***

i want to return the number of same characters.

***

i want to return the longest streak?

AABBBCCCC

i want to return the longest streak.
the length of the longest streak.

***

i want to return the length of the longest streak of characters.

***

i have a string of uppercase characters.
i want to return the length of the longest streak of characters.

***
i have a string,
containing uppercase characters.

i want to return the length of the longest streak of characters.

a streak is back to back same characters.

i can cheat
i can modify the string to give a longer streak.

i can change any character i want to any uppercase character.
but i can only make a certain number of changes.

what's the length of the longest streak i can make.

***

i have a string.

i can replace any character in the string.
but i can only replace `k` times.

given my position,
how can i replace characters in the string
so i form the longest consecutive substring of similar characters.

***

i have a string,
containing uppercase characters.

i want to return the length of the longest streak of characters.
a streak is back to back same characters.

i.e. AAA is the longest streak in BBAAA

i can cheat,
i'm allowed to change the characters in the string to give a longer streak.

i can turn our initial, BBAAA, into AAAAA.
by changing the first two characters.

i can change any character i want to any uppercase character.
but i can only make a certain number of changes.

what's the length of the longest streak i can make.

***


i have a string,
containing uppercase characters.

i want to return the length of the longest streak of characters.
a streak is back to back same characters.

i.e. AAA is the longest streak in BBAAA

i can cheat,
i'm allowed to change the characters in the string to give a longer streak.

for example, 
the longest streak in BBAAA is 3As.

but i can make it longer, if i change the 2Bs into As

BBAAA => AAAAA

now, the longest streak is 5.
however, there's a limit on the number of changes i can make.

this limit is the number `k`.
i can't change more than `k` characters in the given string.

given these conditions,
what's the longest streak i can make?

well, the length of the streak is what i want.
not the streak itself.

so, what really is the problem here?
knowing what to replace to give the longest streak.

the example, BBAAA => AAAAA, is straightforward
when `k` is 2.

but knowing leetcode, it's never this simple.

let's consider another example where the string is

ABAB

and k is 2

without replacing anything, the current longest streak is `1`
i can make 2 replacements

what do i replace?

do i replace the As or the Bs?
how do i know which is better?

well, i can see the whole string.

there's 2As and 2Bs.
and k is 2.

meaning i can replace either.

if i replace both As, i get 4Bs
if i replace both Bs, i get 4As

either way, my longest streak is 4.

however, my code can't exaclty see all the characters.
the decision isn't that simple.

what if my string was:

HOFOBTBYHGRGWLFCZTVTPVCNTDWKIVLMVMSCTFXCMLYAMPAUHBLAFTSUCBLJRJZBOWFVTBKOKNVCSTFZMPD
and k was 7.

how would i approach this?
exactly.

this is why leetcode is crazy.

how can i replace any?
what am i replacing?
yo...

okay, let's start with the first character.
the longest streak is bound to start somewhere.

let's see if it starts at the begining.
okay, so starting at H,
i'd move right, replacing every non-H character with H

the furthest i'd get is:
`HOFOBTBYH` 
{ animations are probably useful for this }
where i'm visually showing the my progression through the string
and decrementing `k`.

if i did this through, i'd definitely get the answer.
i don't expect to include this block in the final write up
but the obvious, down-to-earth, case, is the longest streak
must start somewhere.

so if i explore every position as the start.
i can find the longest streak.

let me write the code and find a TLE to back up my claim.

```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestStreak = 0
        for idx, ch in enumerate(s):
            streakLen = self.exploreStreak(idx, k, s)
            
            longestStreak = max(
                longestStreak,
                streakLen,
            )

        return longestStreak
    
    
    def exploreStreak(self, startIdx, replacementsLeft, s):
        startCh = s[startIdx]
        dim = len(s)
        streakLen = 0
        for idx in range(startIdx, dim):
            ch = s[idx]
            if ch == startCh:
                pass
            elif replacementsLeft > 0:
                replacementsLeft -= 1
            else:
                break
            
            streakLen += 1
            
        return streakLen
```

well, nope.
i can't back up my claim.

"ABBB", k=2
this broke me.

the assumption that the longest streak must start somewhere is true.
but it's not to say, the first character is the character that forms the longest streak.

this example makes it obvious, the longest streak after replacements is 4.
since you'd replace the A with a B.

but the way i wrote the code, i would never hit this case.
since,
i start at each character, 
then assume the subsequent characters are it's streakers.

i don't think you're meant to solve leetcode in one-go.
i think big tech filters for those who've been through the fire.
