import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        min_heap = [(0, 0)]  # (custo inicial, ponto inicial)
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost

            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))

        return total_cost

# Teste do problema
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
solution = Solution()
print(solution.minCostConnectPoints(points))  # Saída esperada: 20
