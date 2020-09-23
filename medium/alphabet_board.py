class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        board_dict = {board[row][col]: (row,col) for row in range(len(board)) for col in range(len(board[row]))}
        res = []
        curr_row = curr_target = curr_col = 0
        for letter in target:
            target_row, target_col = board_dict[letter]
            if curr_row == len(board) - 1 and letter != 'z': curr_row -= 1; res.append("U")
            while curr_col != target_col:
                if target_col > curr_col: curr_col += 1; res.append("R")
                else: curr_col -= 1; res.append("L")
            while curr_row != target_row:
                if target_row > curr_row: curr_row += 1; res.append("D")
                else: curr_row -= 1; res.append("U");
            res.append("!")
        return "".join(res)