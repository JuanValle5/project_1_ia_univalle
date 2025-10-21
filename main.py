import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
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
COLOR_PATH = "yellow"

CELL_SIZE = 50  # Tamaño de cada celda en píxeles
ICON_SIZE = 40  # Tamaño de los íconos

# Ruta hacia los íconos dentro de tests/assets
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "tests", "assets")


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

        # Cargar imágenes
        self.load_images()

        # Crear interfaz
        self.create_widgets()
        self.draw_grid()

    # Cargar imágenes
    def load_images(self):
        """Carga y redimensiona los íconos."""
        self.img_ant = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "ant.png")).resize((ICON_SIZE, ICON_SIZE)))
        self.img_ant_yellow = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "antyellow.png")).resize((ICON_SIZE, ICON_SIZE)))
        self.img_mushroom = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "mushroom.png")).resize((ICON_SIZE, ICON_SIZE)))
        self.img_skull = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "skull.png")).resize((ICON_SIZE, ICON_SIZE)))


    # Interfaz
    def create_widgets(self):
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

        # Canvas principal
        self.canvas = tk.Canvas(self.root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="white")
        self.canvas.grid(row=0, column=1)
        self.canvas.bind("<Button-1>", self.handle_click)

   
    # Dibujo del entorno
    def draw_grid(self):
        """Dibuja la cuadrícula con íconos e indicadores visuales."""
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                cell = self.grid.cells[r][c]

                # Fondo amarillo para el camino
                if cell.in_path:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=COLOR_PATH, outline="gray")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=COLOR_EMPTY, outline="gray")

                # Dibujar ícono según tipo
                if cell.type == CellType.ANT:
                    self.canvas.create_image(x1 + CELL_SIZE / 2, y1 + CELL_SIZE / 2, image=self.img_ant)
                elif cell.type == CellType.MUSHROOM:
                    self.canvas.create_image(x1 + CELL_SIZE / 2, y1 + CELL_SIZE / 2, image=self.img_mushroom)
                elif cell.type == CellType.POISON:
                    self.canvas.create_image(x1 + CELL_SIZE / 2, y1 + CELL_SIZE / 2, image=self.img_skull)

   
    # Interacción con clics del usuario
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


    # Animación del movimiento
    def animate_path(self, path):
        """Muestra visualmente el movimiento animado de la hormiga."""
        for (r, c) in path:
            if (r, c) != self.grid.start and (r, c) != self.grid.goal:
                self.grid.cells[r][c].in_path = True
                self.draw_grid()

                x = c * CELL_SIZE + CELL_SIZE / 2
                y = r * CELL_SIZE + CELL_SIZE / 2
                self.canvas.create_image(x, y, image=self.img_ant_yellow)

                self.root.update()
                time.sleep(0.25)


    # Limpieza del camino anterior
    def clear_previous_path(self):
        """Limpia solo el camino anterior sin borrar los objetos ni íconos."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid.cells[r][c].in_path:
                    self.grid.cells[r][c].in_path = False
        self.draw_grid()

    # Ejecución del algoritmo seleccionado
    def run_search(self):
        if not self.grid.ant or not self.grid.mushroom:
            messagebox.showwarning("Advertencia", "Debes colocar una posición inicial (A) y una meta (M).")
            return

        # 🔹 Limpia el camino anterior al iniciar una nueva búsqueda
        self.clear_previous_path()

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

   
    # Reinicio del entorno completo
  
    def reset_grid(self):
        self.grid = Grid(self.rows, self.cols)
        self.draw_grid()



# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    root = tk.Tk()
    app = AntApp(root)
    root.mainloop()
