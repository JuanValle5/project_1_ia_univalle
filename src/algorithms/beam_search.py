from src.utils.node import Node
from src.utils.heuristics import manhattan_distance


def beam_search(grid, beam_width=3):

    # Nodo inicial
    start = Node(grid.start, None, g=0, h=manhattan_distance(grid.start, grid.goal))
    start.f = start.h

    # Inicializar frontera y conjunto de visitados
    frontier = [start]
    visited = set()

    while frontier:
        new_frontier = []

        for node in frontier:
            visited.add(node.position)

            # Verificar si se alcanzó la meta
            if node.position == grid.goal:
                return reconstruct_path(node)

            # Expandir vecinos
            for next_pos in grid.neighbors(node.position):
                if next_pos not in visited:
                    g = node.g + 1
                    h = manhattan_distance(next_pos, grid.goal)
                    child = Node(next_pos, node, g=g, h=h, f=h)
                    new_frontier.append(child)

        # Ordenar por heurística y limitar por el ancho del haz
        new_frontier.sort(key=lambda n: n.h)
        frontier = new_frontier[:beam_width]

    # ------------------------------------------------------------------
    # Si no se encuentra un camino, guardar las posiciones visitadas
    # ------------------------------------------------------------------
    save_unsuccessful_path(visited)

    return None


def reconstruct_path(node):

    #Reconstruye el camino desde el nodo objetivo hasta el nodo inicial.
    

    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return list(reversed(path))


def save_unsuccessful_path(visited):
    
    #Guarda en un archivo .txt todas las posiciones visitadas durante la búsqueda
    #cuando no se encuentra un camino válido.

    
    filename = "recorrido_no_encontrado.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("BÚSQUEDA BEAM SEARCH - SIN SOLUCIÓN\n")
        file.write("=" * 45 + "\n\n")
        file.write(f"Total de nodos visitados: {len(visited)}\n\n")
        file.write("Recorrido de posiciones visitadas (r, c):\n")
        for i, pos in enumerate(visited):
            file.write(f"{i+1}. {pos}\n")


