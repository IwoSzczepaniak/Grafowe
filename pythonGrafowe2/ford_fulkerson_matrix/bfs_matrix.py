from matrix_graph import matrix_graph
from check import check_flow_solution_no_grid100x100
from collections import deque


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
            if residual[u][x] != 0:
                if not visited[x]:
                    parents[x] = u
                    visited[x] = True
                    min_cap = min(capacity, residual[u][x])
                    if x == sink:
                        return min_cap
                    d_queue.append((x, min_cap))


def ford_fulk(graph, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    residual = [graph[i][:] for i in range(ver)]
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


def solution(V, L):
    matrix_g = matrix_graph(V, L)
    return ford_fulk(matrix_g, 0, V-1, V)


# -----------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    check_flow_solution_no_grid100x100(solution)
