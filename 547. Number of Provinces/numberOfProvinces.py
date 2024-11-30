class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        pre_order = [0] * n
        post_order = [0] * n
        time = [1]  # Usamos uma lista para manter a referência mutável
        provinces = 0

        def dfs(city):
            visited[city] = True
            pre_order[city] = time[0]
            time[0] += 1

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

            post_order[city] = time[0]
            time[0] += 1

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces
