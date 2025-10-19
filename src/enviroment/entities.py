# src/environment/entities.py

class Entity:
    """Clase base para cualquier objeto del entorno."""
    def __init__(self, position):
        self.position = position  # (fila, columna)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position})"


class Ant(Entity):
    """La hormiga agente inteligente."""
    def __init__(self, position):
        super().__init__(position)
        self.path = []  # camino recorrido

    def move_to(self, new_position):
        self.position = new_position
        self.path.append(new_position)


class Mushroom(Entity):
    """El hongo mágico (meta)."""
    def __init__(self, position):
        super().__init__(position)


class Poison(Entity):
    """Una celda venenosa (obstáculo)."""
    def __init__(self, position):
        super().__init__(position)
