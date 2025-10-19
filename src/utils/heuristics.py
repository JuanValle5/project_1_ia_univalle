"""
Funciones heurísticas para algoritmos de búsqueda
"""
import math


def manhattan_distance(pos1, pos2):
    """
    Distancia Manhattan (L1) entre dos posiciones

    Args:
        pos1 (tuple): Posición (row, col) inicial
        pos2 (tuple): Posición (row, col) final

    Returns:
        float: Distancia Manhattan
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def euclidean_distance(pos1, pos2):
    """
    Distancia Euclidiana (L2) entre dos posiciones

    Args:
        pos1 (tuple): Posición (row, col) inicial
        pos2 (tuple): Posición (row, col) final

    Returns:
        float: Distancia Euclidiana
    """
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def chebyshev_distance(pos1, pos2):
    """
    Distancia Chebyshev (L∞) entre dos posiciones
    Permite movimiento diagonal

    Args:
        pos1 (tuple): Posición (row, col) inicial
        pos2 (tuple): Posición (row, col) final

    Returns:
        float: Distancia Chebyshev
    """
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))


def get_heuristic(name="manhattan"):
    """
    Obtiene una función heurística por nombre

    Args:
        name (str): Nombre de la heurística ("manhattan", "euclidean", "chebyshev")

    Returns:
        function: Función heurística
    """
    heuristics = {
        "manhattan": manhattan_distance,
        "euclidean": euclidean_distance,
        "chebyshev": chebyshev_distance
    }

    return heuristics.get(name.lower(), manhattan_distance)