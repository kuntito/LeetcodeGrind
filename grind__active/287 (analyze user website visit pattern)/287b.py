# https://leetcode.com/problems/analyze-user-website-visit-pattern/description/

# what are we dealing with?
# we are to implement a function `mostVisitedPattern`


# it receives three string arrays, `username`, `timestamp` and `website`
# all arrays are same length and each idx represents info about a user
# their username and the time they visited a particular website

# a pattern is a list of three websites, the websites don't have to be distinct
# i.e. "home -> web -> jay" and "jay -> jay -> jay"
# are both patterns

# the score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern

# that's a lot to unpack, a pattern is a list of three visited websites
# also, the patterns don't have to be contiguous i.e.
# if a user visits a -> b -> c -> d -> e
# the following are patterns abc, abd, abe, acd.... and so on

# we'd need to obtain all the unique patterns
# and determine the score of each pattern.

# it's giving multiple nested loop vibes, or perhaps, i misread the question
# obtaining the distinct patterns is tedious in itself

# let's take it one step at a time. for each user, we need to know what websites they visited, are the timestamps in sorted order?? let's assume they are
from collections import defaultdict


# TODO, perhaps i don't understand the question but i'm close
class Solution:
    def mostVisitedPattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        pass

        # let's use a hashmap to store each user and the websites they visited
        # username => [array of websites]

        # apparently, timestamp isn't sorted so let's sort the timestamp and carry the username and website along.

        # python has a neat trick
        combined = sorted(zip(timestamp, username, website))

        userAndWebsites = defaultdict(list)
        for _, user, site in combined:

            userAndWebsites[user].append(site)
        

        # we'd use a default dict to store the unique patterns and the number of times they appeared
        patterns = defaultdict(int)
        for user, sites in userAndWebsites.items():
            # print(f"{user}-{sites}")

            # for each user, we explore all their patterns,
            # this would be a recursive function
            # we need the current index, initialized to zero
            # and for each index we start another recursive call with index + 1
            # and count how deep we are?

            # to be fair, i could just write three nested loops
            # and track the unique patterns in an array
            # concatenate into a string, separate each website with a hyphen
            # store in patterns
            self.explorePatterns(patterns, sites)

        # for pat, score in patterns.items():
        #     print(f'{pat} => {score}')

        x = sorted(patterns.items(), key=lambda i: (-i[1], i[0]))
        for foo in x:
            print(foo)

        return x[0][0].split("-")

    def explorePatterns(self, patterns, sites):
        dim = len(sites)

        for i in range(dim):
            uno = sites[i]
            for j in range(i + 1, dim):
                dos = sites[j]
                for k in range(j + 1, dim):
                    tres = sites[k]
                    key = f"{uno}-{dos}-{tres}"

                    patterns[key] += 1


arr = [
    [
        [
            "joe",
            "joe",
            "joe",
            "james",
            "james",
            "james",
            "james",
            "mary",
            "mary",
            "mary",
        ],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            "home",
            "about",
            "career",
            "home",
            "cart",
            "maps",
            "home",
            "home",
            "about",
            "career",
        ],
    ],
    [
        ["ua", "ua", "ua", "ub", "ub", "ub"],
        [1, 2, 3, 4, 5, 6],
        ["a", "b", "a", "a", "b", "c"],
    ],
    [
        ["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"],
        [
            527896567,
            334462937,
            517687281,
            134127993,
            859112386,
            159548699,
            51100299,
            444082139,
            926837079,
            317455832,
            411747930,
        ],
        [
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "hibympufi",
            "yljmntrclw",
            "hibympufi",
            "yljmntrclw",
        ],
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.mostVisitedPattern(foo, bar, baz)
print(res)
