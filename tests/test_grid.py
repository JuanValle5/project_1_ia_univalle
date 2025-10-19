# tests/test_grid.py
import pytest
from src.enviroment.grid import Grid

def test_grid_creation():
    g = Grid(5, 5)
    assert g.rows == 5
    assert g.cols == 5
    assert g.get_matrix() is not None

def test_set_start_and_goal():
    g = Grid(5, 5)
    g.set_start(0, 0)
    g.set_goal(4, 4)
    assert g.start == (0, 0)
    assert g.goal == (4, 4)
    assert g.cells[0][0].type == 'A'
    assert g.cells[4][4].type == 'M'

def test_add_poison_and_validity():
    g = Grid(5, 5)
    g.add_poison(2, 2)
    assert not g.is_valid((2, 2))
    assert g.is_valid((1, 1))
    assert g.cells[2][2].type == 'X'

def test_neighbors_exclude_poison():
    g = Grid(3, 3)
    g.add_poison(1, 1)
    neighbors = g.neighbors((1, 0))
    assert (1, 1) not in neighbors
