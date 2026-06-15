class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, idx, visited):

            # Entire word matched
            if idx == len(word):
                return True

            # Out of bounds, already visited, or character mismatch
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visited or
                board[row][col] != word[idx]
            ):
                return False

            visited.add((row, col))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                if dfs(row + dr, col + dc, idx + 1, visited):
                    return True

            # Backtrack
            visited.remove((row, col))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, set()):
                    return True

        return False