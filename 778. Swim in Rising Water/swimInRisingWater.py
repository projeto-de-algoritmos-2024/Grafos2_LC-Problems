class Solution:
    def swimInWater(self, grid):
        from collections import deque

        n = len(grid)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = set()
        queue = deque([(0, 0, grid[0][0])])

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) in seen:
                continue
            seen.add((row, col))
            if row == col == n - 1:
                return steps
            for dx, dy in dirs:
                x, y = row + dx, col + dy
                if 0 <= x < n and 0 <= y < n:
                    queue.append((x, y, max(steps, grid[x][y])))

        return -1

