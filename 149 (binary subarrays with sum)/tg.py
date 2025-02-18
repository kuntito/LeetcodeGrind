# TODO intuition?
def count_contiguous_sub_arrays(n):
    count = 0
    for i in range(1, n + 1):
        count += i
        
    return count

# this function determines the number of contiguous arrays
# but my intuition about it is wrong

# i'm of the opinion that at each iteration, it adds one new item
# and that item would either stand alone, or combine with every existing sub array

# for instance
# at i == 1
# let's say the item is `a`
# since there's no existing item
# `a` can only stand alone
# res = [`a`]

# at i == 2
# let's say the new item is `b`
# `b` would both stand alone as `b` and combine with the existing item `ab`

# now `res = [`a`, `b`, `ab`]`

# however at i == 3
# let's say the new item is `c`
# `c` would both stand alone as `c` and combine with each of `a`, `b`, `ab`
# forming res = [a, b, ab, c, ca, cb, ab]
# this is where my intuition fails since at this point, there would be `7` items
# but an array of size `3` can only have 6 contiguous sub arrays
# i can identify that `ca` shouldn't be possible since that's not contiguous
# but i want to have a model in my brain of what's wrong with my approach to understanding the code

a = count_contiguous_sub_arrays(3)
print(a)