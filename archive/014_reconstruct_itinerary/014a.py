# https://leetcode.com/problems/reconstruct-itinerary/description/


from collections import deque
class Solution:
    def findItinerary(self, tickets: list) -> list:
        self.destinations = self.get_destinations(tickets)

        self.eulerian_path = deque()
        self.explore("JFK")
        return list(self.eulerian_path)
    

    def explore(self, origin):
        while self.destinations[origin]:
            self.explore(
                self.destinations[origin].pop()
            )

        self.eulerian_path.appendleft(origin)


    def get_destinations(self, tickets: list) -> dict:
        res = {}
        for depart, arrive in tickets:
            if depart not in res:
                res[depart] = []
            if arrive not in res:
                res[arrive] = []

            res[depart].append(arrive)

        for depart, locations in res.items():
            locations.sort(reverse=True)

        return res


arr = [
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
    [
        ["EZE","AXA"],
        ["TIA","ANU"],
        ["ANU","JFK"],
        ["JFK","ANU"],
        ["ANU","EZE"],
        ["TIA","ANU"],
        ["AXA","TIA"],
        ["TIA","JFK"],
        ["ANU","TIA"],
        ["JFK","TIA"]
    ],
    [
        ["AUA","ADL"],
        ["AUA","ANU"],
        ["AUA","AXA"],
        ["ADL","ANU"],
        ["ADL","EZE"],
        ["ADL","EZE"],
        ["AXA","TIA"],
        ["AXA","EZE"],
        ["AXA","AUA"],
        ["ANU","JFK"],
        ["ANU","AUA"],
        ["ANU","EZE"],
        ["EZE","TIA"],
        ["EZE","HBA"],
        ["EZE","ADL"],
        ["EZE","ANU"],
        ["JFK","AXA"],
        ["JFK","AXA"],
        ["TIA","ADL"],
        ["TIA","AUA"],
    ],
    # [
    #     ["JFK","KUL"],
    #     ["JFK","NRT"],
    #     ["NRT","JFK"],
    # ],
    # [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
]

foo = arr[-1]
sol = Solution()
res = sol.findItinerary(foo)

print(res)
