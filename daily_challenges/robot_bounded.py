class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i = 0
        curr_location = (0,0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(4):
            for direct in instructions:
                if direct == 'G': 
                    curr_location = (curr_location[0] + directions[i][0], curr_location[1] + directions[i][1])
                if direct == 'L':
                    i = i - 1
                if direct == 'R':
                    i = i + 1
                if i >= len(directions): i = 0
                if i < 0: i = len(directions) - 1
            if curr_location == (0, 0): return True
        return False