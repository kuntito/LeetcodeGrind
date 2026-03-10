# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List

# i have an array of integers.
# each integer represents the height of a pillar.

# if there's a depression between two pillars
# we can store water in it.

# in that depression.

# for instance, if the array is [1, 0, 1]
# at value `0`
# we have a depression, and because, we can store water in it.

# the job was to find the total amount of water
# the entire array can store.

# my approach was to determine the tallest pillar on either end of each cell.
# this way i can determine if there's a depression.

# the shorter of the two pillars determines how much water can be stored
# at a particular position
# and since, the particular position can also have a pillar.

# i have to deduct from the height of the shorter pillar.
# to deduct the height of the current pillar.

# this tells me if water is in a particular cell.

# i totaled this and found the result.

# for knowing the tallest left pillar at each position.
# i tracked it as i iterated through the array.

# for the right pillars, i had to cache it.
# i iterated in reverse, storing the righmost tallest pillar at each point.

# the overall space time complexity of this algo is O(n), the right most cache.

# Navdeep boasts of an O(1) space time and this is what i want to explore.

# https://www.youtube.com/watch?v=ZI2z5pq0TqA
# TODO 16:08 `you move the smaller one because you know there's something taller than it in front.`

# i think i get the idea.
# two pointers, `left` and `right`, starting at the extreme ends.

# whichever pointer has the shorter value moves forward.
# then we can calculate the water stored at this particular position.

# by decrementing the shorter value we just left by the current value we just reached.

# in my head, it sounds like it'd work.
# but why..

# why did i have to move the shorter one?
# well, the shorter one always decides the water you can store.

# but at index `0`
# if i viewed this through my own algorithm..
# i'd need the tallest left and the tallest right.

# at index `0`, there is no tallest left.
# so whatever is right wards is irrelevant.

# i can feel free to set the result for index `0` to be zero
# and start the iteration from index 1

# okay, still on my algo..
# at index 1, i need the tallest left and the tallest right
# at this point the tallest left has to be whatever is at index 0

# and the tallest right?
# well i don't know..

# but when would it matter? or rather, why would it matter to know
# the tallest on either side.

# well, at any position.
# the amount of water you can store is determined by your boundaries.

# i know my left boundary.
# and i know the furthest boundary to the left.

# Navdeep says to move the smaller of the two boundaries.
# i think i have this wrong.

# starting at index 1 is the wrong way to look at it.

# you place two pointers at the extreme boundaries.
# whichever one is less, is the one that moves.

# but why?
# the first iteration is either trying to figure out the storage
# at index 1 or index second to the last.

# if it was index 1, we'd do leftHeight - currentHeight
# i understand why this would work because 
# if the left height was the shorter of the two and 
# i moved it's pointer forward to index 1 
# at index 1, i know for sure.. the left is the shorter..

# well, yes, the shorter between the extreme left and the extreme right.
# not the shorter between the tallest left and the tallest right.

# consider
# [3, 0, 2, 5]

# with Nav's algo..
# i'd move the left pointer to index 1, value 0
# and then say the leftHeight - currentHeight is how much water i can store at index 1

# this would be 3 - 0 = 3
# this isn't the case.

# looking at the array.
# at index 1, the shorter of the two boundaries is `2`
# well, not really.

# even from your algo.
# you were searching for the tallest to the left
# and the tallest to the right.

# not what's immediately left or what's immediately right.
# with your algo, you'd have (3) and (5)
# and rightfull so, end up doing 3 - 0...

# Nav works.. with this example.

# so what exactly is your concern?

# it's just the approach doesn't seem intuitive.
# why does moving the shorter extreme pointer guarantee
# that at the new index, the pointer you left would be
# the shortest tallest pointer on either side of the new position.

# let's look at it from index 1's perspective..
# what's the tallest on my left, i can know that since i'm index 1
# what's the tallest on my right? i don't know..

# but when would the right matter?
# if it's shorter..
# is it if it's shorter..
# it's if it's shorter and there's no taller boundary after it.

# but how do i know that there's no taller boundary after it
# if i don't seek.

# how does the extreme right pointer tell me what's the tallest pointer
# to the right.

# well, you clearly don't need to know the tallest to the right.

# another way to look at it is this.
# from the jump, two pointers..

# left and right
# if the left is the lesser height.
# what that means is, it determines the ceiling of the next position.

# it doesn't matter what happens on the right.
# i know the left is less than it.

# what do you mean..
# what if you have a value on the right of next pointer less than the starting left.
# it wouldn't matter, because i know it goes up, at the extreme right pointer.
# so that still tells me the starting left is the limiting factor.

# what if there was a taller pointer than the rightmost one.
# it wouldn't change anything.

# i'd still be comparing the tallest right pointer
# with the starting left and starting left is still taller.

# the insight here.. is both leftmost and rightmost heights..
# have a say of the position right next to them.
class Solution:
    def trap(self, height: List[int]) -> int:
        pass