# src/environment/grid.py

from src.enviroment.cell import Cell, CellType
from src.enviroment.entities import Ant, Mushroom, Poison


class Grid:
    """
    Representa el entorno donde se mueve la hormiga.
    Maneja las celdas, entidades y validaciones de movimiento.
    """

    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.ant = None
        self.mushroom = None
        self.poisons = []

    # ---------------------------------------------------------
    # Métodos para configuración del entorno
    # ---------------------------------------------------------

    def set_start(self, row, col):
        """Coloca la hormiga (agente) en una posición inicial."""
        if self.ant:
            old_r, old_c = self.ant.position
            self.cells[old_r][old_c].set_type(CellType.EMPTY)
        self.ant = Ant((row, col))
        self.cells[row][col].set_type(CellType.ANT)

    def set_goal(self, row, col):
        """Coloca el hongo mágico (meta)."""
        if self.mushroom:
            old_r, old_c = self.mushroom.position
            self.cells[old_r][old_c].set_type(CellType.EMPTY)
        self.mushroom = Mushroom((row, col))
        self.cells[row][col].set_type(CellType.MUSHROOM)

    def add_poison(self, row, col):
        """Coloca una celda venenosa (obstáculo)."""
        poison = Poison((row, col))
        self.poisons.append(poison)
        self.cells[row][col].set_type(CellType.POISON)

    def clear(self):
        """Limpia toda la cuadrícula."""
        self.cells = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
        self.ant = None
        self.mushroom = None
        self.poisons = []

    # ---------------------------------------------------------
    # Métodos de navegación
    # ---------------------------------------------------------

    def is_valid(self, pos):
        """Verifica si una celda es transitable."""
        r, c = pos
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return False
        return self.cells[r][c].is_walkable()

    def neighbors(self, pos):
        """Devuelve las posiciones vecinas válidas (4 direcciones)."""
        r, c = pos
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        valid = []
        for dr, dc in moves:
            new_r, new_c = r + dr, c + dc
            if self.is_valid((new_r, new_c)):
                valid.append((new_r, new_c))
        return valid

    # ---------------------------------------------------------
    # Métodos de visualización (texto o GUI)
    # ---------------------------------------------------------

    def show(self):
        """Imprime la cuadrícula en consola (para depuración)."""
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(self.cells[r][c].type)
            print(" ".join(row))
        print()

    def get_matrix(self):
        """Devuelve una representación en lista de listas (útil para GUI o tests)."""
        return [[self.cells[r][c].type for c in range(self.cols)] for r in range(self.rows)]

    # ---------------------------------------------------------
    # Utilidades varias
    # ---------------------------------------------------------

    @property
    def start(self):
        return self.ant.position if self.ant else None

    @property
    def goal(self):
        return self.mushroom.position if self.mushroom else None
