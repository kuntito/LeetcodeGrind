longest repeating character replacement.

why would you even want to know this? why?
so, you could show your friends?
is that what this is?
oh, look, i can find the longest repeating chara-

get outta here.

now, that, that's said.
how do i solve this?

i've read the question and would just write how i understand it.
i have two things.
actually, i'm given two things and want to return one thing.

what else?
there's a string, `s` and an integer, `k`.
all this just feels like beating around the bush.

what am i supposed to do?
i have a string.

i can change characters in the string.
i can change a certain amount of times.

i think it's best i write down the things that are true from the question
then put it together to know what this is really saying.

* i have a string, `s`
* i have an integer, `k`
* i want to replace characters in the string.
* i can only replace with uppercase English characters.
* i can perform up to `k` replacements.
* i want to return the length of the longest substring containing the same letter i can get after performing the above operations.

    this is a mouthful, what's it saying really?
    i want to return the length of a substring.

    simply put, i want to return a number.

    but what is this number?
    the length of the longest substring containing the same letter i can get after performing the above operations.

    this is still crazy.

    i want to return a number.
    the number is the length of a substring.

    what is this substring?
    the substring is the longest substring containing the same letter i can get after performing the above operations.

    what operations?
    the character replacement?

    oh, i see.
    i want to replace characters in the original string `s`
    in a way that it forms the longest substring of the same character?

    i guess. what is a substring?
    back to back characters.

    i see.
    so, the question is, given a string, `s`
    where i can replace up to `k` characters
    what's the length of the longest streak of the same character.

    i omitted it, but it goes without saying,
    the characters in the string `s` are all uppercase characters.

i swear, the writing on this leetcode joint drives me nuts.
what's wrong with saying:

    there's a string that only contains uppercase characters.
    you, John Cena, can replace any character you want with another uppercase character.
    but you can't replace more than `k` times.

    the goal is to create the longest streak of the same character.
    and tell us how long that streak is.