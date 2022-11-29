from collections import deque
import copy
from check import check_connectivity_solution_no_grid100x100
from matrix_graph import matrix_graph

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.


def bfs(s, sink, parents, residual, ver):
    visited = [False for _ in range(ver)]
    visited[s] = True
    parents[s] = -1
    d_queue = deque()
    min_cap = 10**10
    d_queue.append((s, min_cap))
    while d_queue:
        u, capacity = d_queue.popleft()
        for x in range(ver):
            if residual[u][x] != 0 and not visited[x]:
                    parents[x] = u
                    visited[x] = True
                    min_cap = min(capacity, residual[u][x])
                    if x == sink:
                        return min_cap
                    d_queue.append((x, min_cap))


def ford_fulk(residual, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    max_flow = 0
    min_cap = bfs(source, sink, parent, residual, ver)
    while min_cap:
        max_flow += min_cap
        u = sink
        while u != source:
            v = parent[u]
            residual[u][v] += min_cap
            residual[v][u] -= min_cap
            u = v
        min_cap = bfs(source, sink, parent, residual, ver)
    return max_flow


def solution(V,L):
    matrix_g = matrix_graph(V, L)
    result = 0
    for vertex in range(1, V):
        g_copy = copy.deepcopy(matrix_g)
        result = max(result, ford_fulk(g_copy, 0, vertex, V))
    return result


# -----------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    check_connectivity_solution_no_grid100x100(solution)
