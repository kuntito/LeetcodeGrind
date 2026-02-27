# https://leetcode.com/problems/distinct-subsequences/description/

# i'm given two strings, `s` and `t`.

# i want to find the number of distinct subsequences of `s`
# which equal `t`

# but what does this mean?
# a subsequence of `s` that equals `t`

# a subsequence of `s` would be a set of characters in `s`
# that follow each other but not necessarily back to back.

# for instance, "ns" is a subsequence of "nas"
# the characters 'n' and 's' follow each other, 
# they aren't next to each other.

# that said, "na" is also a subsequence of "nas"
# the characters 'n' and 'a' follow each other and in this case,
# next to each other.

# the requirement for a subsequence is that the order of characters
# remains the same.

# "an" wouldn't be a subsequence of "nas"
# since "a" does not come before "n" in "nas"

# so, how does this understanding help solve the question?

# well, for you to find out if a subsequence of `s`
# is equal to `t`

# you'd have to compare every character.
# but how?

# for a start, you go through `s`
# and pause at the first character that matches the first character in `t`

# let's follow this using an example:

# s = 'bbag'
# t = 'bag

# here, at s(0), we have a match with t(0)
# they are both b's

# so what do we do..
# we progress both pointers..

# we get s(1) which is another 'b'
# and t(1) which is another 'a'

# there's a mismatch.. t(1) is an 'a'
# to match we need to find an 'a' in `s`

# so what do we do?

# we move s's pointer forward..
# s(2) is an 'a'

# okay, we got s(2) == t(1)
# we can move both pointers forward..

# and now we have s(3) and t(2), which are both 'g's
# and that's a matching subsequence.

# we know it's a subsequence, because we reached the end of `t`
# actually.. we'd know it's a subsequence because
# t's pointer would go out of bounds after the match

# simpling reaching the last character in `t` only tells us
# the previous character had a match,
# we need to go out of bounds to complete the subsequence.

# we found one subsequence but the question isn't over.
# we want to find the total amount of distinct subsequences.

# revisiting the example
# s = 'bbag'
# t = 'bag'

# there's actually two subsequences in `s` that match `t`.. 

# the first 'b' and the 'ag', i.e. b_ag
# the second 'b' and the 'ag', i.e _bag

# i don't know how to work my way to this
# but i know the right thing to do, when characters match,
# is to start a function call, a recursive function call
# with two pointers, the s pointer and t pointer

# the idea here is we have a match..
# we want to explore this on a separate thread.

# that way, the b at index 0, and b at index 1
# can reach their natural conclusions..

# and we can collate the results upward.

# what would each recursive function look like.
# s_pointer, t_pointer

# the s_pointer keeps moving forward until it's character matches..
# the one at t_pointer, at which point we start another thread..

# the parent thread's s_pointer keeps moving..
# incase there's another match ahead..

# i.e. 'bbag' and 'bag'
# one way we can shortciruit this journey is if 
# s_pointer ever reaches a point where the rest of characters in `s`
# are less than the rest of characters in `t`, you can end the iteration.

# since there's no way to find a matching subsequence 
# with less characters than `t`

# what does each recursive function return...
# if we exhaust `t`, we return `1` else return `0`

# the parent calls can collate all the results
# and return to their parents..

# eventually reaching the source.

# is there an argument for memoization? yes.

# think 'bbag' and 'bag'

# both b's in 'bbag' would reach.. 'a' at index `2`
# so it makes sense to cache (s_pointer, t_pointer) since it would always lead to the same result.

# so the function takes five things..
# s_pointer
# s
# t_pointer
# t
# memo



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sIdx = 0
        tIdx = 0
        memo = {}
        
        return self.explore(sIdx, s, tIdx, t, memo)
    
    def explore(self, sIdx, s, tIdx, t, memo):
        if tIdx == len(t):
            return 1
        
        mitem = (sIdx, tIdx)
        if mitem in memo:
            return memo[mitem]
        
        res = 0
        for idx in range(sIdx, len(s)):
            restOfCharsInS = len(s) - idx
            restOfCharsInT = len(t) - tIdx
            
            if restOfCharsInS < restOfCharsInT:
                break
            
            chOne = s[idx]
            
            if chOne == t[tIdx]:
                res += self.explore(
                    idx + 1,
                    s,
                    tIdx + 1,
                    t,
                    memo
                )
                
                
        memo[mitem] = res
        return memo[mitem]