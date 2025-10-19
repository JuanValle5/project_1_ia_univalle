# tests/test_dynamic_weighting.py
from src.enviroment.grid import Grid
from src.algorithms.dynamic_weighting import dynamic_weighting_astar

def test_dynamic_weighting_basic():
    g = Grid(4, 4)
    g.set_start(0, 0)
    g.set_goal(3, 3)

    path = dynamic_weighting_astar(g, epsilon=1.0)
    assert path is not None
    assert g.start in path
    assert g.goal in path
    assert len(path) >= 3  # debe haber al menos algunos pasos

def test_dynamic_weighting_with_obstacles():
    g = Grid(5, 5)
    g.set_start(0, 0)
    g.set_goal(4, 4)
    g.add_poison(1, 2)
    g.add_poison(2, 2)
    g.add_poison(3, 1)

    path = dynamic_weighting_astar(g, epsilon=1.5)
    assert path is not None
    assert g.start in path
    assert g.goal in path

def test_dynamic_weighting_no_path():
    g = Grid(3, 3)
    g.set_start(0, 0)
    g.set_goal(2, 2)
    g.add_poison(1, 0)
    g.add_poison(1, 1)
    g.add_poison(0, 1)

    path = dynamic_weighting_astar(g, epsilon=1.0)
    assert path is None
