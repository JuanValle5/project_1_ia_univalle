"""
Clase Node para representar estados en el árbol de búsqueda
"""


class Node:
    """
    Representa un nodo en el árbol de búsqueda

    Attributes:
        position (tuple): Posición (row, col) en la grilla
        parent (Node): Nodo padre (para reconstruir camino)
        g (float): Costo desde el inicio
        h (float): Heurística estimada al objetivo
        f (float): Función de evaluación f(n) = g(n) + h(n)
        depth (int): Profundidad en el árbol de búsqueda
    """

    # src/utils/node.py

class Node:
    def __init__(self, position, parent=None, g=0, h=0, f=None, depth=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f if f is not None else g + h
        self.depth = depth

    def __eq__(self, other):
        return isinstance(other, Node) and self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.position)


    def __repr__(self):
        return f"Node(pos={self.position}, g={self.g:.1f}, h={self.h:.1f}, f={self.f:.1f})"

    def get_path(self):
        """
        Reconstruye el camino desde el inicio hasta este nodo

        Returns:
            list: Lista de posiciones desde el inicio hasta este nodo
        """
        path = []
        current = self
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]  # Invertir para tener inicio -> fin

    def get_neighbors(self, grid):
        """
        Obtiene las posiciones vecinas válidas (4-conectividad)

        Args:
            grid: Objeto Grid del entorno

        Returns:
            list: Lista de posiciones (row, col) vecinas válidas
        """
        row, col = self.position
        neighbors = []

        # Movimientos: arriba, derecha, abajo, izquierda
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Verificar que esté dentro de los límites
            if grid.is_valid_position(new_row, new_col):
                # Verificar que no sea un obstáculo
                if not grid.is_wall(new_row, new_col):
                    neighbors.append((new_row, new_col))

        return neighbors