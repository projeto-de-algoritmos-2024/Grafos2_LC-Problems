class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = {}
        candidatos = []  # Arestas com duplo pai

        graph = [[] for _ in range(n + 1)]  # Grafo original

        for u, v in edges:
            if v in parent:
                # Nó com dois pais encontrado
                candidatos.append((parent[v], v))  # Primeira aresta
                candidatos.append((u, v))          # Segunda aresta
            else:
                parent[v] = u
                graph[u].append(v)

        # Primeira DFS no grafo original
        visited = [False] * (n + 1)
        pre_order = [0] * (n + 1)
        post_order = [0] * (n + 1)
        time = [1]
        order = []

        def dfs1(u):
            visited[u] = True
            pre_order[u] = time[0]
            time[0] += 1
            for v in graph[u]:
                if not visited[v]:
                    dfs1(v)
            post_order[u] = time[0]
            time[0] += 1
            order.append(u)

        for i in range(1, n + 1):
            if not visited[i]:
                dfs1(i)

        # Grafo reverso
        reverse_graph = [[] for _ in range(n + 1)]
        for u in range(1, n + 1):
            for v in graph[u]:
                reverse_graph[v].append(u)

        # DFS no grafo reverso
        visited = [False] * (n + 1)
        sccs = []

        def dfs2(u, component):
            visited[u] = True
            component.append(u)
            for v in reverse_graph[u]:
                if not visited[v]:
                    dfs2(v, component)

        for u in reversed(order):
            if not visited[u]:
                component = []
                dfs2(u, component)
                if len(component) > 1:
                    sccs.append(component)

        # Análise dos resultados
        if sccs:
            if candidatos:
                # Caso 1: Nó com dois pais e ciclo
                return list(candidatos[0])
            else:
                # Caso 2: Apenas ciclo
                # Encontrar a aresta que faz parte do SCC
                for u, v in reversed(edges):
                    for scc in sccs:
                        if u in scc and v in scc:
                            return [u, v]
        else:
            if candidatos:
                # Caso 3: Apenas nó com dois pais
                return list(candidatos[1])

        return edges[-1]
