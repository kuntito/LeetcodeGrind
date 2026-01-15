# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# omo, just watched neet code's video on it..
# thinking about the situation really simplifies the problem..
# the bills are either 5, 10 or 20...

# the lemonade is always 5, and the customer only buys one..
# in essence, i would only ever need to give a 5 dollar change
# or a 15 dollar change...

# if it's 5 dollar change, it's basic..
# if it's 15 dollar.. here's where i ran into problems earlier..

# my thinking was if i had three fivers and one tenner..
# would i rather give the customer three fivers
# or give them a tenner and a fiver..

# but with the constraints of the question, the answer becomes obvious
# i can only give two kinds of change, 5 or 15..
# if i gave the customer three fivers, if i need a five later on
# i wouldn't have it..
# however, if i gave them a tenner and one fiver, i keep my fivers when i need them later..

# there's no situation where i need a tenner and multiple fivers
# can't help me, however, there's many situations where i need a fiver and multiple tens wouldn't help me..

# always take the tens first..
# that said, i should be able to write a solution here..


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pass