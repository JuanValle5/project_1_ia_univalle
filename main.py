import tkinter as tk
from tkinter import ttk, messagebox
import time
import sys
import os

# Agregar la carpeta src al path para importar correctamente
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importar clases y algoritmos
from src.enviroment.grid import Grid
from src.enviroment.cell import CellType
from src.algorithms.beam_search import beam_search
from src.algorithms.dynamic_weighting import dynamic_weighting_astar

# Colores para el grid
COLOR_EMPTY = "white"
COLOR_ANT = "orange"
COLOR_GOAL = "green"
COLOR_POISON = "red"
COLOR_PATH = "yellow"
COLOR_VISITED = "lightblue"

CELL_SIZE = 50  # Tamaño de cada celda en píxeles


class AntApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hormiga Inteligente 🐜 - Búsqueda Informada")

        # Parámetros iniciales
        self.rows = 8
        self.cols = 8
        self.grid = Grid(self.rows, self.cols)
        self.algorithm = tk.StringVar(value="beam")
        self.beam_width = tk.IntVar(value=3)
        self.epsilon = tk.DoubleVar(value=1.0)

        # Crear interfaz
        self.create_widgets()
        self.draw_grid()

    def create_widgets(self):
        # Panel lateral de control
        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.grid(row=0, column=0, sticky="ns")

        ttk.Label(control_frame, text="Algoritmo:").pack(pady=3)
        ttk.Radiobutton(control_frame, text="Beam Search", variable=self.algorithm, value="beam").pack(anchor="w")
        ttk.Radiobutton(control_frame, text="Dynamic Weighting A*", variable=self.algorithm, value="dynamic").pack(anchor="w")

        ttk.Label(control_frame, text="Beam width (β):").pack(pady=5)
        ttk.Entry(control_frame, textvariable=self.beam_width, width=6).pack()

        ttk.Label(control_frame, text="Epsilon (ε):").pack(pady=5)
        ttk.Entry(control_frame, textvariable=self.epsilon, width=6).pack()

        ttk.Button(control_frame, text="Ejecutar búsqueda", command=self.run_search).pack(pady=10)
        ttk.Button(control_frame, text="Reiniciar", command=self.reset_grid).pack(pady=5)

        # Canvas donde se dibuja el entorno
        self.canvas = tk.Canvas(self.root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="white")
        self.canvas.grid(row=0, column=1)
        self.canvas.bind("<Button-1>", self.handle_click)

    # -----------------------------------------------------------------
    # Dibujo del entorno
    # -----------------------------------------------------------------
    def draw_grid(self):
        """Dibuja la cuadrícula completa."""
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                cell = self.grid.cells[r][c]
                color = COLOR_EMPTY
                if cell.type == CellType.ANT:
                    color = COLOR_ANT
                elif cell.type == CellType.MUSHROOM:
                    color = COLOR_GOAL
                elif cell.type == CellType.POISON:
                    color = COLOR_POISON
                elif cell.in_path:
                    color = COLOR_PATH

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    # -----------------------------------------------------------------
    # Interacción con clics del usuario
    # -----------------------------------------------------------------
    def handle_click(self, event):
        """Permite colocar la hormiga, el hongo y los venenos con clics."""
        c = event.x // CELL_SIZE
        r = event.y // CELL_SIZE

        if not self.grid.ant:
            self.grid.set_start(r, c)
        elif not self.grid.mushroom:
            self.grid.set_goal(r, c)
        else:
            self.grid.add_poison(r, c)

        self.draw_grid()

    # -----------------------------------------------------------------
    # Animación del camino encontrado
    # -----------------------------------------------------------------
    def animate_path(self, path):
        """Muestra visualmente el movimiento de la hormiga paso a paso."""
        for (r, c) in path:
            if (r, c) != self.grid.start and (r, c) != self.grid.goal:
                self.grid.cells[r][c].in_path = True
                self.draw_grid()
                self.root.update()
                time.sleep(0.3)

    # -----------------------------------------------------------------
    # Ejecución del algoritmo seleccionado
    # -----------------------------------------------------------------
    def run_search(self):
        if not self.grid.ant or not self.grid.mushroom:
            messagebox.showwarning("Advertencia", "Debes colocar una posición inicial (A) y una meta (M).")
            return

        self.draw_grid()
        self.canvas.update()

        if self.algorithm.get() == "beam":
            path = beam_search(self.grid, beam_width=self.beam_width.get())
        else:
            path = dynamic_weighting_astar(self.grid, epsilon=self.epsilon.get())

        if path:
            self.animate_path(path)
            messagebox.showinfo("Resultado", f"Camino encontrado con {len(path)-1} pasos.")
        else:
            messagebox.showerror("Sin solución", "No se encontró un camino posible.")

    # -----------------------------------------------------------------
    # Reinicio del entorno
    # -----------------------------------------------------------------
    def reset_grid(self):
        self.grid = Grid(self.rows, self.cols)
        self.draw_grid()


# ---------------------------------------------------------------------
# EJECUCIÓN PRINCIPAL
# ---------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AntApp(root)
    root.mainloop()
