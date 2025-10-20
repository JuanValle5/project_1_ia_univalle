from src.utils.node import Node
from src.utils.heuristics import manhattan_distance

def beam_search(grid, beam_width=3):
    start = Node(grid.start, None, g=0, h=manhattan_distance(grid.start, grid.goal))
    start.f = start.h
    frontier = [start]
    visited = set()

    while frontier:
        new_frontier = []

        for node in frontier:
            visited.add(node.position)
            if node.position == grid.goal:
                return reconstruct_path(node)

            for next_pos in grid.neighbors(node.position):
                if next_pos not in visited:
                    g = node.g + 1
                    h = manhattan_distance(next_pos, grid.goal)
                    child = Node(next_pos, node, g=g, h=h, f=h)
                    new_frontier.append(child)

        new_frontier.sort(key=lambda n: n.h)
        frontier = new_frontier[:beam_width]

    return None


def reconstruct_path(node):
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return list(reversed(path))
