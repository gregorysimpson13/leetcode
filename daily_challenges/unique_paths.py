def uniquePaths(m:int, n:int) -> int:
    cache = {(m,n): 1}
    def paths(row, col):
        if (row, col) in cache:
            return cache[(row,col)]
        if row > m or col > n:
            return 0
        cache[(row,col)] = paths(row+1, col) + paths(row, col+1)
        return cache[(row,col)]
    return paths(1,1)