class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        # Current cell has already matched word[i - 1].
        # Now search neighbors for word[i].
        def dfs(i, r, c):
            if i == len(word):
                return True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and board[nr][nc] == word[i]
                ):
                    visited.add((nr, nc))

                    if dfs(i + 1, nr, nc):
                        return True

                    visited.remove((nr, nc))

            return False

        for r in range(rows):
            for c in range(cols):
                # The starting cell must match word[0].
                if board[r][c] == word[0]:
                    visited.add((r, c))

                    # word[0] is matched, so search for word[1].
                    if dfs(1, r, c):
                        return True

                    visited.remove((r, c))

        return False