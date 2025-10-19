# src/environment/cell.py

class CellType:
    EMPTY = " "
    ANT = "A"
    MUSHROOM = "M"
    POISON = "X"
    OBSTACLE = "#"
    PATH = "."

class Cell:
    def __init__(self, row, col, cell_type=CellType.EMPTY):
        self.row = row
        self.col = col
        self.type = cell_type
        self.visited = False
        self.in_path = False

    def set_type(self, cell_type):
        self.type = cell_type

    def is_walkable(self):
        """Una celda es transitable si no es veneno ni obstáculo."""
        return self.type not in (CellType.POISON, CellType.OBSTACLE)

    def __repr__(self):
        return f"Cell({self.row},{self.col},'{self.type}')"
