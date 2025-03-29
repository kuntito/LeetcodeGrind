* screenshot of the question

* explanation
    the way i approach questions is to figure out what they're really asking
    i have an array that contains numbers

    and in that array, there are two numbers that add up to the variable `target`
    my job is to find the indices of those two numbers


    let's first find those two numbers, then we'd worry about the indices

    the bruteforce approach is to explore every combination of numbers
    but with LeetCode, bruteforce is rarely a good strategy

    looking at the equation:
        a + b = target

    we know target, we can assume the first number is `a`
    is the first number part of the solution, well, it needs `b`
    to form target, is `b` in the array?

    go through the array, one step at a time
    whenever, we are at `2`, we set a = 2
    this means b has to be `7`
    is `7` in the array, yes, but we shouldn't know that
    since we're at index `0`
    [2, 7, 11, 15]

    is there a way we could know ahead of time what elements are in the array?
    well, hashmap?

    i could hash each element and pair it with it's index
    that way, we could immediately know if `7` is the array
    and return the index

    right? WRONG!


    let's consider this array
    [3, 3] where the target is `6`
    using the same logic, we assume the first number is `a`
    which means `b` must be `3`
    is `3` in the hashmap?

    yes, but how do we know which `3`?
    what if rather than storing each index,
    we store all the indices for each element { show the hashmap to the side }
    that way, we know that the second `3` is the one we need

    this could work
    `implement it in 01c.py`

