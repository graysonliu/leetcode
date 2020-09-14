# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # in graph theory, this is to find a Eulerian path
        # Eulerian path: a path that visits every edge exactly once (allowing for revisiting vertices)
        tickets.sort(reverse=True)
        import collections
        d = collections.defaultdict(list)
        for trip in tickets:
            # the tickets list is sorted reversely
            # so, for all tickets with the same departure airport, the ticket whose arrival airport is smaller in
            # lexical order will be added at the back of the list
            # thus, it will be popped first when we call list.pop()
            d[trip[0]].append(trip[1])

        # Solution: https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
        path = []

        def visit(airport):
            while d[airport]:
                visit(d[airport].pop())
            # all outbound edges of this vertex have been visited
            # add this vertex to the reversed path
            path.append(airport)

        visit('JFK')
        return path[::-1]


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
