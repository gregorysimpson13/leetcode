class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minpath, rows, cols = float('inf'), len(heights) - 1, len(heights[0]) - 1
        lookup = {}
        queue = [(0,0,0,heights[0][0])]
        while queue and queue[0][0] < minpath:
            ad, r, c, last = heappop(queue)
            ad = max(ad, abs(last-heights[r][c]))
            if (r,c) in lookup and lookup[(r,c)] <= ad: continue
            lookup[(r,c)] = ad
            if r == rows and c == cols: minpath = min(ad, minpath); continue
            d = [(0,1),(0,-1),(1,0),(-1,0)]
            for nr, nc in d:
                nrow, ncol = nr+r, nc+c
                if nrow >= 0 and nrow <= rows and ncol >= 0 and ncol <= cols:
                    heappush(queue, (ad,nrow,ncol,heights[r][c]))
        return minpath
        