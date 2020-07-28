from typing import List
from copy import deepcopy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(idx=0, path=[0]):
            if idx == len(graph) - 1:
                result.append(deepcopy(path))
            for i in graph[idx]:
                dfs(i, path + [i])
        if graph and graph[0]: dfs()
        return result