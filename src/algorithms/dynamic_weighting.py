from heapq import heappush, heappop
from src.utils.node import Node
from src.utils.heuristics import manhattan_distance


def dynamic_weighting_astar(grid, epsilon=1.0):

    # Crear el nodo inicial
    start = Node(grid.start, None, g=0, h=manhattan_distance(grid.start, grid.goal))
    start.f = start.h

    # Inicializar frontera como cola de prioridad (min-heap)
    frontier = [(start.f, start)]
    visited = set()

    # Estimar profundidad máxima (para ajustar el peso dinámico)
    N = grid.rows * grid.cols

    while frontier:
        # Extraer el nodo con menor costo f
        _, node = heappop(frontier)

        # Evitar re-visitar nodos
        if node.position in visited:
            continue
        visited.add(node.position)

        # Si llegamos al objetivo, reconstruir camino
        if node.position == grid.goal:
            return reconstruct_path(node)

        # Expandir vecinos
        for next_pos in grid.neighbors(node.position):
            if next_pos in visited:
                continue

            # Calcular costos
            g = node.g + 1
            h = manhattan_distance(next_pos, grid.goal)
            d = node.depth + 1
            f = g + h + epsilon * (1 - (d / N)) * h  # peso dinámico

            # Crear nodo hijo y agregarlo a la frontera
            child = Node(next_pos, node, g=g, h=h, f=f, depth=d)
            heappush(frontier, (child.f, child))

    # Si no hay solución
    return None


def reconstruct_path(node):
    
    #Reconstruye el camino desde el nodo objetivo hasta el inicial.

  
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return list(reversed(path))
