class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        reds, blues = defaultdict(set), defaultdict(set)
        for i, j in red_edges: reds[i].add(j)
        for i, j in blue_edges: blues[i].add(j)
        result = [-1] * n
        result[0] = 0
        queue = [(0,0,'r'), (0,0,'b')] # distance, index, next_color
        heapq.heapify(queue)
        visited = set()
        while queue:
            distance, index, next_color = heapq.heappop(queue)
            if (index, next_color) in visited: continue
            if result[index] == -1 or result[index] > distance:
                result[index] = distance
            if next_color == 'r':
                for j in reds[index]:
                    heapq.heappush(queue, (distance + 1, j, 'b'))
            else:
                for j in blues[index]:
                    heapq.heappush(queue, (distance + 1, j, 'r'))
            visited.add((index, next_color))
        return result