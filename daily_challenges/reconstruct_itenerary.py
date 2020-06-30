# Reconstruct Itenerary

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.
# JFK ->  ATL
#     ->  SFO 
# 
# ATL ->  JFK
#     ->  SFO
#
# SFO ->  ATL

from collections import defaultdict
def findItinerary(tickets):
    result_list = []
    def dfs(airport):
        while tickets_dict[airport]:
            dfs(tickets_dict[airport].pop())
        result_list.append(airport)
    tickets_dict = defaultdict(list)
    for ticket in tickets:
        from_airport, to_airport = ticket[0], ticket[1]
        tickets_dict[from_airport].append(to_airport)
    for ticket in tickets_dict.keys():
        tickets_dict[ticket].sort(reverse=True)
    dfs("JFK")
    return result_list[::-1]

    


tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK", "LGA"]]
tickets4 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets5 = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(findItinerary(tickets1),end='\n\n')
print(findItinerary(tickets2),end='\n\n')
print(findItinerary(tickets3),end='\n\n')
print(findItinerary(tickets4),end='\n\n') # ["JFK","NRT","JFK","KUL"]
print(findItinerary(tickets5),end='\n\n') # ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]