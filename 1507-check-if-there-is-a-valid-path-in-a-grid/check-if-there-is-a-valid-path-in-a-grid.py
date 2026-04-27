from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # directions: (dr, dc)
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        # reverse direction check
        def is_valid(nr, nc, r, c):
            for dr, dc in dirs[grid[nr][nc]]:
                if nr + dr == r and nc + dc == c:
                    return True
            return False

        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))

        while q:
            r, c = q.popleft()

            if (r, c) == (m - 1, n - 1):
                return True

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if is_valid(nr, nc, r, c):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return False