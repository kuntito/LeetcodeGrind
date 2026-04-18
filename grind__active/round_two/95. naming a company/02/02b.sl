i have a list of strings.

i want to form a company name from the list.
any two strings can form a company name if they meet a condition.

i want to find out how many unique company names i can form.

how do two strings form a company name?
there's two steps.

step one,
    you swap the first letter in both strings.

    i.e. if you have `cat` and `bar`
    after swapping, it becomes
    `bat` and `car`

two,
    after swapping, to form the company name
    the two new words must not exist in the list.

    if they do exist in the list,
    you can't form a company name with the strings.

    if they don't exist in the list,
    you can form a company name.

    the company name is formed by joining both strings with a space.

    hence, you'd have "bat car"

my job is to find out how many distinct company names i can form.
and return that number.

***

what's the way to look at this?

for one, i'd have to explore every pair in the string.
swap their first letters
after swapping,
check if any of the new strings exist in the list.
if none of them do,
i have a valid company name.

i'd benefit from converting the list into a set.
so i can do O(1) checking.

***
ran it, but time limit exceeded.

what can i speed up?

consider,
(car, bat)
(car, bad)

in both cases, one of the words is `bar`
if i know `bar` is a valid word.

i don't need to make the swap for both words.

in other words, for each string, 
i can save time, 
by knowing the first characters it's been swapped with and the outcome.

and what's the shape of this memo?
i need the first char it pairs with
i need to know the outcome of that pairing.
i need to be able to check that pairing in real time.

you can pair each word with it's chars.
word => {
    chOne => result,
    chTwo => resultTwo,
}

so a dictionary of words.
each word points to another dictionary, the sub-dict.
the sub-dict points to each result.

what if i pair the first char against the word and result instead.

chOne => (word, result)
this is simpler to model