from check import check_connectivity_solution_no_grid100x100
from matrix_graph import matrix_graph
import copy

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in range(len(G)):
        if not V[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, V, P, nb)


def dfs(G, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, s, t, P):
        curr_flow = 10**9
        current = t
        while current != s:
            curr_flow = min(curr_flow, G[P[current]][current])
            current = P[current]
        max_flow += curr_flow
        v = t
        while v != s:
            u = P[v]
            G[u][v] -= curr_flow
            G[v][u] += curr_flow
            v = P[v]
    return max_flow


def solution(V,L):
    matrix_g = matrix_graph(V, L)
    result = 0
    for vertex in range(1, V):
        g_copy = copy.deepcopy(matrix_g)
        result = max(result, Ford_Fulk(g_copy, 0, vertex))
    return result
    # return result


# -----------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    check_connectivity_solution_no_grid100x100(solution)