class Solution:
    def swimInWater(self, grid):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(row, col, steps):
            n = len(grid)
            if row == n - 1 and col == n - 1:
                return steps
            if row < 0 or row >= n or col < 0 or col >= n:
                return float('inf')
            return min(
                dfs(row + 1, col, max(steps, grid[row][col])),
                dfs(row, col + 1, max(steps, grid[row][col]))
            )

        return dfs(0, 0, grid[0][0])
