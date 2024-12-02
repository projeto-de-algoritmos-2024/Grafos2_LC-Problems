import heapq

class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):

        adj = [[] for _ in range(n)]      # Grafo original
        rev_adj = [[] for _ in range(n)]  # Grafo Reverso

        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))  # Inverte a direção da aresta para o grafo reverso

        def dijkstra(n, adj, src):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(src, 0)]

            #utilizando heap para lista dos candidatos
            while heap:
                d, u = heapq.heappop(heap)

                if d > dist[u]:
                    continue

                for v, w in adj[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap, (dist[v], v))

            return dist

        # Cálculo das distâncias mínimas
        dist1 = dijkstra(n, adj, src1)
        dist2 = dijkstra(n, adj, src2)
        dist_dest = dijkstra(n, rev_adj, dest)

        # Cálculo do peso mínimo total
        min_total_cost = float('inf')
        for v in range(n):
            if dist1[v] == float('inf') or dist2[v] == float('inf') or dist_dest[v] == float('inf'):
                continue
            total_cost = dist1[v] + dist2[v] + dist_dest[v]
            min_total_cost = min(min_total_cost, total_cost)

        return min_total_cost if min_total_cost != float('inf') else -1