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
    tickets_lookup = defaultdict(int)
    tickets_dict = defaultdict(list)
    for ticket in tickets:
        from_airport, to_airport = ticket[0], ticket[1]
        tickets_dict[from_airport].append(to_airport)
        tickets_lookup[to_airport] += 1
    current_airport = "JFK"
    result_list = []
    while current_airport:
        result_list.append(current_airport)
        if not tickets_dict[current_airport]:
            return result_list
        current_airport = tickets_dict[current_airport].pop(0)
    return result_list

    


tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK", "LGA"]]
tickets4 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(findItinerary(tickets1))
print(findItinerary(tickets2))
print(findItinerary(tickets3))
print(findItinerary(tickets4)) # ["JFK","NRT","JFK","KUL"]