# https://leetcode.com/problems/find-the-town-judge/

# TODO https://neetcode.io/solutions/find-the-town-judge
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        pass
        # the judge is the guy that trusts no one
        # but is trusted by everybody
        
        # create a set of people who have trusted, `trusting_people`
        trusting_people = set()
        # create a hashmap of {person: number of people who trust in them}
        hashmap = {}
        for truster, trusted in trust:
            hashmap[trusted] = hashmap.get(trusted, 0) + 1
            trusting_people.add(truster)
        
        # the answer is the person who has `n-1` trustees AND is not in `trusting_people`
        for person in range(1, n+1):
            count = hashmap.get(person, 0)
            if count == n -1 and person not in trusting_people:
                return person
        
        return -1

    
arr = [
    [3, [[1,2],[2,3]]],
    [3, [[1,3],[2,3],[3,1]]],
    [3, [[1,3],[2,3]]],
    [2, [[1, 2]]],
    [1, []],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findJudge(foo, bar)
print(res)