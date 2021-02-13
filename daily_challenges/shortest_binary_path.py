#Runtime: O(nmlognm)
#Space: O(nm)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] or grid[-1][-1]: return -1
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        heap, seen = [(1,0,0)], set()
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        while heap:
            d, r, c = heappop(heap)
            if r == rows and c == cols: return d
            if (r,c) in seen: continue
            seen.add((r,c))
            for ri, ci in directions:
                nr, nc = r+ri, c+ci
                if 0 <= nr <= rows and 0 <= nc <= cols and not grid[nr][nc]: heappush(heap, (d+1,nr,nc))
        return -1
