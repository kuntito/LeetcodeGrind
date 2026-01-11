# https://leetcode.com/problems/k-th-symbol-in-grammar/description/

# `kthGrammar`, what are it's demands. it wants us to implement a
# function, takes two integer arguments, `n` and `k`, does something with them and returns an integer.

# but what something are we doing? 
# for a start, we want to build a table of `n` rows.

# the first row would contain `0`
# for every row after the first
# each new row would look at the previous row
# and replace every occurence of `0` with `01`
# and also, replace every occurence of `1` with `10`

# for example, n = 3

# row1 = "0"
# row2, looks at row1, replaces every occurence of `0` with `01`
# now, row2 = "01"

# the question is, do i replace the `1` i just added to `row2` with
# `10`, the example says no

# pparently, at the time of populating the row
# i just need to know the locations of 0s and the locations
# of all 1s
# so i can replace accordingly

# when all said and done, i want to return the kth symbol in the nth row of the table.

# bear in mind, k is `1-indexed`
# i.e. if k = 1, i'm referring to index 0

# it seems fairly simple to implement
# i think every time i've said this, i've struggled to solve the problem

# let's see
# i can use a loop to create all the rows
# technically i don't need to store all the rows
# only the previous row

# and for this previous row, i need to know the locations of the `0s`
# and the locations of the `1s`

# it's giving hashmap
# when i replace, wouldn't that change the index of things
# another way is to boycott the hashmap

# i'd iterate through the previous row
# and address each char at a time
# that way i don't need the index
# and i'd be creating the new row on the go

# after addressing all the characters on the previous row
# i'd assign the previous row to the new row
# and proceed

# when all said and done, i'd return `prevRow[k-1]`

# TODO well, memory limit exceeded, i need to find a way to optimize this
# if i pay attention, i might uncover a pattern
# since, i more or less do the same thing with every row
# might be able to calculate the nth row in one go
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        prevRow = [0]
        
        for _ in range(n-1):
            curRow = []
            for ch in prevRow:
                if ch == 0:
                    curRow.append(0)
                    curRow.append(1)
                else:
                    curRow.append(1)
                    curRow.append(0)
                    
            prevRow = curRow
            
        return prevRow[k-1]
    
arr = [
    [2, 2],
    [2, 1],
    [1, 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.kthGrammar(foo, bar)
print(res)
                    