from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        heap = [(grid[0][0], 0, 0)]

        while heap:
            steps, row, col = heappop(heap)
            if row == col == n - 1:
                return steps
            for dx, dy in dirs:
                x, y = row + dx, col + dy
                if 0 <= x < n and 0 <= y < n:
                    heappush(heap, (max(steps, grid[x][y]), x, y))

        return -1
