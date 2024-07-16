from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row=0, diagonals=set(), anti_diagonals=set(), cols=set(), state=[]):
            if row == n:
                board = []
                for r in state:
                    board.append("".join(r))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                state.append(["Q" if c == col else "." for c in range(n)])

                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                state.pop()

        result = []
        backtrack()
        return result
