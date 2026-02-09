# https://leetcode.com/problems/reconstruct-itinerary/

from typing import List

# i'm given a list of airline tickets, `tickets`
# each ticket is a string array of two items, 
# the departure airport and the destination airport, `from` and `to`

# i'm to reconstruct the itinerary in order and return it.
# what does this mean?

# apparently, all the tickets belong to a man who departs from "JFK"
# so the itinerary must begin with "JFK".

# in essence, i want to outline every where the man went starting fro "JFK".
# all tickets in `tickets` form a valid itinerary.

# and each ticket can only be used once.

# if there are multiple valid iteneraries, i should return the one with the smallest
# lexical order when read as a single string.

# what does this mean?
# consider the tickets:
# JFK => ATL
# JFK => LON
# LON => JFK
# ATL => JFK

# we have to start from a JFK, we have two tickets starting at JFK
# JFK => ATL and JFK => LON

# ATL has the better lexical order, so i explore ATL first
# now, i'm at ATL, where can i go from here..

# i've got a ticket from ATL => JFK
# so i go back to JFK

# now, i can go to LON
# i take JFK => LON

# at LON, there's only one ticket i can take..
# LON => JFK

# so, it's calm now.

# when you line em up..
# it's:
# JFK => ATL => JFK => LON => JFK

# this is the best lexical order.
# so, at every airport, always explore the next airport
# with the smallest lexical order.

# seems simple enough but because i know..
# it's possible the best lexical order does not allow you explore all the destinations

# consider:
# JFK => ATL
# JFK => LON
# LON => JFK

# here, even though ATL lexically comes before LON
# if i go to ATL first, i'm stuck there.
# there's no return flight to JFK..

# so i must go to LON first, go back to JFK, then go to ATL
# the itinerary becomes:

# JFK => LON => JFK => ATL

# but how would i have known there's no return ticket from ATL?
# the giveaway is if you still have tickets to explore
# and no new destinations.. you should backtrack..

# have you solved the problem?
# it would seem so..

# create a graph of tickets
# each `aiport => a sorted array of destinations`
# then you always pick the first destination to explore..

# i'm not sure how this would work?

# let's look at this way, at any point during exploration
# there's always a next best ticket, but we don't know that until we explore.

# for one, we know, the first ticket must be a JFK one..
# we would still need a graph, at least for JFK tickets..

# we explore the first destination..
# say `SFO`
# at `SFO`, we want to know where we can go to next..

# a graph is still helpful here..
# okay..

# okay, but how do you keep track of used tickets..
# we can use a hashmap of tuples..

# for every ticket we explore, we can deduct it from the hasmap
# count, if we ever hit zero, remove from hashmap..

# this way, the hashmap let's me know when i've exhausted tickets..
# if i ever hit a point where there's no new destinations
# and i have tickets, i'd back track and re-add tickets to the hashmap

# but how do you structure each destination..
# say i got JFK => [ATL, MEM, LON]
# i explore ATL and realize, it's a no go..
# by the time i'm back here.. i want to explore LON next..

# i could use a sorted array but how do i handle the fact
# what whenever i explore an airport, i want to remove it from the destination..

# going back to this:
# JFK => [ATL, MEM, LON]

# while exploring ATL, if i ever come across JFK again, i should know
# that i've seen ATL once and shouldn't explore it again..

# the cleanest way would be to remove it from the destinations..
# so if i come across JFK again, i'd only see [MEM, LON]

# okay.. and if ATL turns out a bust and you get back to the OG JFK
# what happens, youb pick LON, and remove from the list..
# so slicing..

# certainly looks like that for now..
# i think i can solve this now..

# create graph of origin to sorted destinations..
# start your exploration from JFK, run through the sorted destinations..

# for each destination, remove from the array..
# actually a cleaner way to do this, is to store the index of the destination you explored.

# before you explore, set the index to None..
# if it becomes bust.. re-add the destination..
# make sure to avoid None's in your explorations..

# add a tracking array, `itinerary` that stores all visited destinations..
# period..

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = self.getGraph(tickets)
        ticketMap = self.getTicketMap(tickets)
        
        itinerary = []
        self.explore("JFK", graph, itinerary, ticketMap)
        return itinerary
    
    def getTicketMap(self, tickets):
        ticketMap = {}
        
        for to, fro in tickets:
            tk = (to, fro)
            ticketMap[tk] = ticketMap.get(tk, 0) + 1
            
        return ticketMap
    
    
    def explore(self, currAirport, graph, itinerary, ticketMap):
        itinerary.append(currAirport)
        
        nextDestinations = graph[currAirport]
        for idx, dest in enumerate(nextDestinations):
            if dest is None: continue
            
            nextAirport = dest
            
            nextDestinations[idx] = None
            
            currentTk = (currAirport, nextAirport)
            ticketMap[currentTk] -= 1
            if ticketMap[currentTk] == 0:
                del ticketMap[currentTk]
            
            if not self.explore(nextAirport, graph, itinerary, ticketMap):
                nextDestinations[idx] = nextAirport
                ticketMap[currentTk] = ticketMap.get(currentTk, 0) + 1
                
        isExhaustDestination = len(ticketMap) == 0
        if not isExhaustDestination:
            itinerary.pop()
                
        return isExhaustDestination
            
        
    def getGraph(self, tickets):
        graph = {}
        
        for origin, destination in tickets:
            if origin not in graph:
                graph[origin] = []
            
            if destination not in graph:
                graph[destination] = []
                
            graph[origin].append(destination)
            
        for origin, destinations in graph.items():
            destinations.sort()
            
        return graph
    
arr = [
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
    [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]],
]
foo = arr[-1]
sol = Solution()

res = sol.findItinerary(foo)
print(res)