from heapq import heappop, heappush
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Direções para movimentos (cima, baixo, esquerda, direita)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Min-heap para Dijkstra (tempo máximo acumulado, linha, coluna)
        min_heap = [(grid[0][0], 0, 0)]
        # Conjunto de visitados
        visited = set()
        # Custo inicial é a altura da célula de partida
        cost = grid[0][0]

        while min_heap:
            current_cost, row, col = heappop(min_heap)
            # Atualiza o custo máximo do caminho até o momento
            cost = max(cost, current_cost)
            # Se chegamos no destino, retornamos o custo
            if row == n - 1 and col == n - 1:
                return cost
            # Marca a célula como visitada
            if (row, col) in visited:
                continue
            visited.add((row, col))
            # Explora os vizinhos
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    heappush(min_heap, (grid[new_row][new_col], new_row, new_col))

        return -1  # Se não encontramos um caminho, o que não deve acontecer neste problema.
