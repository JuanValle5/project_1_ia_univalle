"""
Configuración global del proyecto
"""


class Settings:
    # Ventana
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 800
    WINDOW_TITLE = "Hormiga Buscadora - Beam Search & Dynamic Weighting"
    FPS = 60

    # Grilla
    GRID_ROWS = 20
    GRID_COLS = 20
    CELL_SIZE = 35
    CELL_MARGIN = 2

    # Algoritmos
    BEAM_BETA = 3  # Amplitud de la viga
    DYNAMIC_EPSILON = 2.0  # Factor de ponderación
    DYNAMIC_MAX_DEPTH = 100  # N en la fórmula

    # Animación
    ANIMATION_SPEED = 0.1  # Segundos entre movimientos (más bajo = más rápido)
    SHOW_EXPLORED = True  # Mostrar nodos explorados
    SHOW_PATH = True  # Mostrar camino final

    # Heurística por defecto
    HEURISTIC = "manhattan"  # "manhattan", "euclidean", "chebyshev"