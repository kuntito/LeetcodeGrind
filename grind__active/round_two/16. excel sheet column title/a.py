# https://leetcode.com/problems/excel-sheet-column-title/

# what are we doing? what am i doing?

# given an integer, i want to convert it into what is called a column title..
# they say it's similar to an excel sheet but let me understand what's going on..

# `A` maps to `1`
# `B` maps to `2`
# you do this until you hit
# `Z` which maps to `26`

# then what..
# once you hit `26`, you start a new count..
# in english please.. you introduce a new character

# so `AZ`, not quite.. you introduce a new character and rest
# `Z` to `A`

# so `AA`
# right... `27` is `AA`
# what's 28, that would be `AB`

# in essence, you'd be restarting the same iteration
# only that the right character stays still, the left character iterates..

# in a way, the right character is a summary of 26 left characters..
# so when you hit `AZ` which would be `26 + 26`
# what would be `47`? add a new character?..

# well, not quite, you're incrementing the right side by `1`
# it becomes `BA`, `47` becomes `BA`..

# how's this working...

# the right side always increases by `1`
# it runs through `A` to `Z`
# after which it resets.. but along with each reset, it increments the left side by `1`
# by it's next character,

# i.e.
# if `A`, it becomes `B`
# if `D`, it becomes `E`
# if `Z`, it becomes `A`, but increments the left character by `1`

# ..this is recursion, but how would you represent it in code..
# ..i can use an array, but understand the characters are in reverse..
# if i want to return the result, i'd reverse the array

# so i'd start with [A]
# hit `Z`, then become [AA] on the next one

# i understand the build up but how do you convert a number into this..
# if you're given 20, it's easy to map
# if given 28, still easy to map..
# how about `328`

# we're dealing in units of 26's
# when i divide by 26, i get 12 remainder 16..
# with 16 i know the left side.. with 12, i know the right side..

# `16` would map to `P`
# `12` would map to `L`

# so `LP`..

# what if the quotient is more than 26..
# do the same thing again..

# that's the recursive bit..

# start with the number, and a result array..
# define a dictionary mapping

# do a div mod..
# your mod is what you use to access the dictionary mapping..
# add result to result array..

# start another recursive call with the quotient..
# keep going until quotient is zero...

# concat the result array and reverse..

# this approach presents a weird problem..
# if i mod 26 by 26, i get 0...
# zero doesn't map to 'Z'
# the quotient logic works for the remainder but nothing else..
# feels like this is an edge case..
# `26` is the only number where this is a problem..
# if you had `25`, you'd get `0` and `25`
# if you had `27`, you'd get `1` and `1`
# the only problematic ones are the multiples of `26`
# well, that doesn't stop much.. rather than map `26` => `Z`
# map `0` => `Z`

# nope, this doesn't work.. `26`
# the zero logic is fine but 26 divmod 26 is 1 remainder 0
# this calls the recursive function with `1` and this creates an `A`
# so we'd have `AZ`

# back to the drawing board...

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
        
        return ''.join(res[::-1])
        
    def explore(self, number, res):
        if number == 0:
            return

        quotient, rem = divmod(number, 26)
        res.append(self.num_to_alpha[rem])
        
        self.explore(quotient, res)
        
arr = [
    1,
    28,
    26,
]

foo = arr[-1]
sol = Solution()
res = sol.convertToTitle(foo)
print(res)