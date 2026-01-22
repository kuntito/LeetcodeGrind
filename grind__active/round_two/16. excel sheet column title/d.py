# https://leetcode.com/problems/excel-sheet-column-title/

# i'm given a number and asked to map to a set of english alphabets.
# each number maps to a letter of the alphabet.

# the numbers start at `1` and go up to wherever..
# point is, map them.

# how's it work? each number maps to successive characters in the english alphabet.
# uppercase characters.

# i.e.
# 1 => A
# 2 => B
# 3 => C
# and so on..

# but happens once we hit 26, well, we map to Z
# and after wards?

# we add a new character..
# um..
# actually, we do two things..
# once we hit, Z, we return back to A
# but along with that, we add a new character..
# another A

# it's getting confusing..
# 27 maps to AA

# okay but why, we were at Z..
# and this mapped to 26
# moment we hit 27, no more characters, what do we do..
# you can think of it like this..

# 26 + 1
# okay, so you summarize that 26 into it's own 1
# so you have 1 and 1
# when you map both 1s, you get AA

# even though we've summarised 26 as 1, it still retains it's past
# as being a 26, because it's a second character.

# i'm not doing a good job at explaining this..

# one intuition is...
# "every time the rightmost letter hits 26, it's left most letter increases by 1"

# think in terms of buckets, each bucket can hold at most 26 digits.
# once it exceeds 26 digits, we summarise all 26 digits into 1
# and place in the next bucket, the next bucket is always to the left

# hmm.. could be better..

# think in terms of buckets, each bucket can hold no more than 26 digits.
# once you exceed 26, you take the overflow and place in the leftmost bucket.

# the intuition works, if your overflow .. actually it doesn't, you're not taking the overflow
# to the next bucket.

# for the `27` example, taking the overflow, would be taking `1` to the next bucket
# but you're not doing that, you're keeping `1` in the current bucket
# and taking `26` to the left bucket, but the difference is, in the left bucket,
# every `26` that comes is treated as `1`

# the left bucket treats units of 26s as `1`
# so once it sees 26 26s, it takes all that
# passes it to the next bucket..
# this guy sees each 26.26s as 1

# and tracks them until, it reaches it's own unit of 26..
# there's a simple explanation to be found here..
# and i would find it.

# draw it out, rightmost bucket has 26 limit
# say, it's at 26 and you add one more, it checks it's capacity

# `damn, i'm full, i'd move these items to big bro on the left`

# big bro on the left, takes the `26`
# but presents it as `1`
# big bro on the left keeps taking `26`s from small bro on the right
# until..
# big bro has taken 26 26s
# at which point big bro can take no more..

# if small bro, sends another 26..
# big bro has to clear out it's capacity into the bigger bro on the left.

# so big bro would pass, 26.26, to bigger bro..
# bigger bro.. can handle this, each 26.26 to bigger bro..
# is a single `1`

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        pass