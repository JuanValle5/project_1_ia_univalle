"""
Constantes de colores para la visualización
Formato: (R, G, B) donde cada valor es 0-255
"""

# Colores de fondo
BACKGROUND = (40, 44, 52)
GRID_LINE = (60, 64, 72)

# Colores de celdas
CELL_EMPTY = (255, 255, 255)
CELL_WALL = (44, 62, 80)
CELL_POISON = (231, 76, 60)

# Colores de entidades
ANT_COLOR = (46, 204, 113)
MUSHROOM_COLOR = (241, 196, 15)

# Colores de búsqueda
EXPLORED = (52, 152, 219, 100)  # Azul semi-transparente
FRONTIER = (155, 89, 182, 100)  # Púrpura semi-transparente
PATH = (46, 204, 113, 150)  # Verde semi-transparente

# Colores de UI
TEXT_COLOR = (255, 255, 255)
TEXT_SHADOW = (0, 0, 0)

def rgb_to_normalized(color):
    """Convierte RGB (0-255) a formato normalizado (0.0-1.0) para Pyglet"""
    if len(color) == 3:
        return (color[0]/255, color[1]/255, color[2]/255)
    elif len(color) == 4:
        return (color[0]/255, color[1]/255, color[2]/255, color[3]/255)
    return color