# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

# following from `a.py`
# you want to reverse iterate through `s`
# at each index, you want to note all the words that start there..

# once done..
# start an iteration from the first..
# for each point where there's a word..
# explore all the words.. this'd probably be recursive..

# for every word.. you explore if a word occurs after it.. or the indices after it..
# to be more explicit..
# if you're at index = 0, you find a word `lee`

# you want ot check from `index + len("lee")` onwards..
# do other words start here...

# in essence, you want to optimize for ...


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        pass