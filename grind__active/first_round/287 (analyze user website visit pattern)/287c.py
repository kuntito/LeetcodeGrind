# https://leetcode.com/problems/analyze-user-website-visit-pattern/description/

from collections import defaultdict

# i think the missing link is a pattern can appear multiple times for a user
# but it is only counted once

# consider:
# ["a", "a", "a", "a"]
# the pattern ["a", "a", "a"] appear four times in the array but it should only count as one addition to the pattern score.
class Solution:
    def mostVisitedPattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        combined = sorted(zip(timestamp, username, website))

        userAndWebsites = defaultdict(list)
        for _, user, site in combined:
            userAndWebsites[user].append(site)
            
        # for user, websites in userAndWebsites.items():
        #     print(f"{user}-{websites}")

        patterns = defaultdict(int)
        for user, sites in userAndWebsites.items():
            self.exploreUserPatterns(patterns, sites)

        x = sorted(patterns.items(), key=lambda i: (-i[1], i[0]))
        # for foo in x:
        #     print(foo)

        return x[0][0].split("-")

    def exploreUserPatterns(self, patterns, sites):
        dim = len(sites)
        seen = set()
        for i in range(dim):
            uno = sites[i]
            for j in range(i + 1, dim):
                dos = sites[j]
                for k in range(j + 1, dim):
                    tres = sites[k]
                    key = f"{uno}-{dos}-{tres}"
                    
                    if key in seen: continue
                    seen.add(key)

                    patterns[key] += 1


arr = [
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
