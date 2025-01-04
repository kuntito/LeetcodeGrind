# https://leetcode.com/problems/path-crossing/


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [0, 0]

        seen = set()
        seen.add((0, 0))

        for p in path:
            if p == 'N':
                pos[1] += 1
            elif p == 'S':
                pos[1] -= 1
            elif p == 'W':
                pos[0] -= 1
            else:
                pos[0] += 1

            foo = tuple(pos)
            if foo in seen: return True
            seen.add(foo)

        return False

            
