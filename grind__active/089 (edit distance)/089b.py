# https://leetcode.com/problems/edit-distance/

# `minDistance` is a function that returns an integer.
# it takes two string arguments, word1, and word2.

# i want to find out the minimum number of operations it would take
# to transform `word1` into `word2`.

# i can do the following three things to `word1`
# insert a character
# delete a character
# replace a character

# that said, how do i find out the minimum number of operations it would take
# to transform `word1` into `word2`.

# i'd say, find all the matches between them.
# what does that mean?

# the first example is
# word1 = "horse"
# word2 = "ros"

# in this case, what would be the match?
# what kind of match am i looking for?
# i think, sequence puts it best
# what's the longest common subsequence between them

# i've got "rs"
# i've got "os"
# what this means is i need three more characters
# three more operations to get to "horse"

# be it insert, delete or replace, the operations are irrelevant here
# so, is that the trick? find the longest common subsequence
# then determine how many more changes need to be made?

# let's look at the second example?
# word1 = "intention", and
# word2 = "execution"

# for longest common subsequence,
# i've got "etion"
# that's 5 characters long, `word2` is 9 characters long.
# meaning i'd need four more characters i.e. four operations

# but the example says the answer is `5`
# let's examine closely "execution"
# the "tion" is constant in both strings,
# so we can remove that, at this point we've made 0 operations

# word1 = "inten"
# word2 = "execu"

# my prior reasoning dictates that,
# since the longest common subsequence is `1`
# i'd need operations of size, len(word2) - len(longestCommonSubsequence)

# but this would only be the case if the longestCommonSubsequence
# was starting or ending the string, that way, i can replace the rest of the string.

# in this particular case "e" occurs twice in `word2`
# if we say the "e" represents the first "e" in "execu"
# what would that mean for word1, "inten"?

# i'd need to delete, "int", that's three operations, resulting in "en"
# and i'd need to replace "n" with "x", that's one more operation

# four operations in, i'd have
# word1 = "ex"
# word2 = "execu"

# now, i'd just need to add "ecu", which is three more operations
# i'd have transformed `word1` into `word2` with 7 operations.


# okay, what if the "e" in `word1`, "inten", represented the second "e" in "execu"

# what would that mean?
# well for one, the "e" in execu has two letters after it, "inten" has one letter after it.

# to make it similar, i'd need two operations
# i'd replace the "n" in "inten" with the "c" in "execu"
# and have:

# word1 = "intec"
# word2 = "execu"

# and the second operation, i'd add a "u" to `word1`
# to give this:

# word1 = "intecu"
# word2 = "execu"

# at this point the two words end the same
# so i'd need to fix the start
# in word1, i have "int" and word2, i have "ex"

# low-key, this is a sub-problem
# i can treat these two as the new `word1` and `word2`
# and have:

# word1 = "int"
# word2 = "ex"

# the question now becomes, how do i turn "int" to "ex"
# with the least number of operations

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass