# Runtime: O(nmlognm); beats 50.54%
# Space: O(m)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        starts = [(n,0) for n in range(rows)] + [(0,m) for m in range(cols)]
        new_mat = [[0] * cols for _ in range(rows)]
        while starts:
            r, c = starts.pop()
            new_list, positions = [], []
            while r < rows and c < cols:
                new_list.append(mat[r][c]); positions.append((r,c))
                r = r + 1; c = c + 1
            new_list.sort()
            for i in range(len(positions)):
                r, c = positions[i]
                new_mat[r][c] = new_list[i]
        return new_mat