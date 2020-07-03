 def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells:
            return cells
        cells[0] = 0
        for _ in range(N):
            prev_value = 0
            for i in range(1, len(cells)-1):
                tmp_value = cells[i]
                cells[i] = 1 if prev_value == cells[i+1] else 0
                prev_value = tmp_value
            cells[-1] = 0
        return cells