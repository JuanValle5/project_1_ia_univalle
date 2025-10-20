from heapq import heappush, heappop
from src.utils.node import Node
from src.utils.heuristics import manhattan_distance

def dynamic_weighting_astar(grid, epsilon=1.0):
    start = Node(grid.start, None, g=0, h=manhattan_distance(grid.start, grid.goal))
    start.f = start.h
    frontier = [(start.f, start)]
    visited = set()

    N = grid.rows * grid.cols  # profundidad máxima estimada

    while frontier:
        _, node = heappop(frontier)
        if node.position in visited:
            continue
        visited.add(node.position)

        if node.position == grid.goal:
            return reconstruct_path(node)

        for next_pos in grid.neighbors(node.position):
            if next_pos in visited:
                continue

            g = node.g + 1
            h = manhattan_distance(next_pos, grid.goal)
            d = node.depth + 1
            f = g + h + epsilon * (1 - (d / N)) * h

            child = Node(next_pos, node, g=g, h=h, f=f, depth=d)
            heappush(frontier, (child.f, child))

    return None


def reconstruct_path(node):
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return list(reversed(path))
