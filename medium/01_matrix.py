class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return matrix
        max_row, max_col = len(matrix), len(matrix[0])
        new_matrix = [[None] * max_col for _ in range(max_row)]
        queue = []
        for row in range(max_row):
            for col in range(max_col):
                if not matrix[row][col]: new_matrix[row][col] = 0; queue.append((row,col))
        distance = 1
        while queue:
            new_queue = []
            for row, col in queue:
                for r, c in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = row + r, col + c
                    if nr < 0 or nr >= max_row or nc < 0 or nc >= max_col or new_matrix[nr][nc] != None: continue
                    new_queue.append((nr,nc))
                    new_matrix[nr][nc] = distance
            queue = new_queue
            distance = distance + 1
        return new_matrix