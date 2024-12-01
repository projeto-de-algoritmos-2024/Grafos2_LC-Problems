class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        total_cost = 0
        current_point = 0

        while len(visited) < n:
            visited.add(current_point)
            min_dist = float('inf')
            next_point = None

            for i in range(n):
                if i not in visited:
                    dist = abs(points[current_point][0] - points[i][0]) + abs(points[current_point][1] - points[i][1])
                    if dist < min_dist:
                        min_dist = dist
                        next_point = i

            if next_point is not None:
                total_cost += min_dist
                current_point = next_point

        return total_cost
