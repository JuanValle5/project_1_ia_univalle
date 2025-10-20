# tests/test_beam_search.py
from src.enviroment.grid import Grid
from src.algorithms.beam_search import beam_search

def test_beam_search_finds_path():
    g = Grid(5, 5)
    g.set_start(0, 0)
    g.set_goal(4, 4)
    g.add_poison(2, 2)
    g.add_poison(1, 3)

    path = beam_search(g, beam_width=3)
    assert path is not None
    assert g.start in path
    assert g.goal in path

def test_beam_search_no_path():
    g = Grid(3, 3)
    g.set_start(0, 0)
    g.set_goal(2, 2)
    # bloqueamos todas las rutas
    g.add_poison(1, 0)
    g.add_poison(0, 1)
    g.add_poison(1, 1)

    path = beam_search(g, beam_width=2)
    assert path is None
