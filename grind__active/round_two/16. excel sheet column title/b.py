# https://leetcode.com/problems/excel-sheet-column-title/

# TODO watch https://www.youtube.com/watch?v=X_vJDpCCuoA, 02:48
# omo, even neetcode solution wan run me mad..
# oshan explain, explain.. let's work this one out..

# what are we doing? we have a number, we map to to a set of characters..
# but there's rules to this mapping..
# the simplest case is if the number >= 1 and number <= 26

# this case, each number maps to the corresponding letter of the alphabet
# 1 maps to A
# 2 maps to B
# 3 maps to C
# and so on..

# things.. get tricky when we exceed `26`
# what kind of things..
# if we hit exceed 26 by 1, we'd get 27
# at this point, 27 doesn't map to any character of the alphabet
# so we deduct 26 from it.. to get `1`

# what we do, is add another character to the ..
# the what..

# okay, let's restart.. we're converting a number to string..
# based on certain rules..
# if we get a number between 1 and 26, we know what to do, if we exceed 26..
# i.e. 27, we add another character to what we've been tracking..

# check it,
# 25 maps to Y
# 26 maps to Z
# 27 maps to AA... what is this sorcery..
# once, we exceed 26, we add another character..

# how are we tracking the characters.. an array would suffice..
# okay.. so question one is, we want to get the first character..
# how do we get that.. uh.. if you take out 26.. i guess..
# i guess, but looking at this.. deeper, if we had 26 + 26 + 1, i imagine we want the same behavior..

# so we want to take out all multiples of 26..
# this is sounding like a modulo problem..
# if `number = 5`
# so `number % 26`, if we get `5`, what does this mean?
# it means we map 5 to it's appropriate character, in this case..
# 5 maps E
# subtle problem, what if number = 26, number % 26, would be zero..
# okay, we can map 0 to Z..
# we'd define a map that runs from 0..25.. and..
# isn't it simpler to just mod by 27..
# modding by 27 takes out multiples of 27 not multiples of 26..
# that wouldn't work..

# best we can do is `mod` by 26, then add one..
# yeah, this works, this way, the mapping is direct 1 => A, 2 => B ... Z => 26..
# well, no.. if you did 5 % 26 = 5, you want `5`
# not `6`..
# so the only time you should add `1` is if you get a zero..
# in which case it's just simpler to add to the map 0 => Z

# okay, let's go with this..
# what's the next step..
# now we want to deal with the remainder after adding this 26..

# if number was 27, we do our magic..
# our array has ['A', ]
# and the remainder would be `1`
# how do we get the remainder..
# what am i even talking about..

# first step is take out all multiples of 26.. you're left with `1`
# the remainder, map it to a char, append to the array..
# what next..

# the quotient * 26 is the new number..
# in our case, quotient is 1
# so 1 * 26.. = 26
# start another recursive call with this and pass the array..

# if there's no remainder, we'd run into infinite recursion..
# say you had number as 26..
# 26 % 26  = 0
# you map 0 to Z, add Z to the array
# then start another recursive call..

# now, you're exactly where you started..
# this question is crazy..

# dunno if it's correct, but whenever remainder is zero.. address the zero as discussed
# now, the quotient represents the number of 26's seen.. `2`
# but we've addressed the first `26` in the slot taken by `0`
# so `quotient -= 1`

# so now we start another recursive call with this..

# i wrote the code, figuring things out on the go and it works
# i don't know why though but i'd figure it out on the next visit..
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.num_to_alpha = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            0: "Z",
        }
        
        res = []
        self.explore(columnNumber, res)
        return "".join(res[::-1])

    def explore(self, number, res):
        if number == 0:
            return
        quo, rem = divmod(number, 26)
        
        res.append(
            self.num_to_alpha[rem]
        )
        
        if rem == 0:
            quo -= 1
            
        self.explore(quo, res)
    
arr = [
    1,
    26,
    28,
    52,
]

foo = arr[-1]
sol = Solution()
res = sol.convertToTitle(foo)
print(res)