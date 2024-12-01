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
            candidatosQueue = [(src, 0)]

            while candidatosQueue:
                # Encontrar o nó com a menor distância na lista
                u, d = None, float('inf')
                min_idx = -1
                for idx, (node, distance) in enumerate(candidatosQueue):
                    if distance < d:
                        u, d = node, distance
                        min_idx = idx

                candidatosQueue.pop(min_idx)

                # Verificar se a distância atual é maior que a registrada
                if d > dist[u]:
                    continue

                for v, w in adj[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        candidatosQueue.append((v, dist[v]))

            return dist
