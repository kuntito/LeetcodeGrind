i'm given two strings.

`s` and `p`.

***

i'm given two strings.
one of them is a plain string, the other is a pattern.

***

what am i doing?
i want to check if the characters in `p` match the characters in `s`.

the characters in `p` are tokens.

the characters in `p` are descriptors.
they describe other characters.

there are three types of characters in `p`.
+ lowercase alphabets
+ an asterisk, '*'
+ a period, '.'

***

`p` is a regex. a regex is a group of characters. they describe the shape of a string.

***
`p` is a group of characters.

***
`p` is a string, but not a regular string.
what it does, is describe the shape of another string.

it is a descriptor.

it's characters are used to describe.

***
i'm given two strings.

one string is used to describe the other.

***

i'm given two strings.

one string describes the other.

i want to find out if the description is accurate.

i'd return a boolean indicating this.

the two strings are, `s` and `p`

`p` is the one describing `s`.
the way it works is, `p` is a string, and contains three types of characters.

+ a period, '.'
+ an asterisk, '*'
+ lowercase english letters

together, these characters can describe another string.
think of them as placeholders.

some examples are:
`.a`
`b*`
`.*b`

the period, '.', is a placeholder for any character.
`.` can describe `b` or `a` or `c`

any character.

the asterisk, `*`, is also placeholder, but it doesn't work in isolation.
it references the character before it.
i.e `a*` or `.*`

the question guarantees there would always be a character before the asterisk.

what the asterisk stands for is a placeholder for zero or more of the character before it.

so, 
`a*` can match:
    '',
    'a',
    'aa',
    'aaa',

