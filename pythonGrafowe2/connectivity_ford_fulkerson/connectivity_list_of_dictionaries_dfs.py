import copy
from dict_list import dict_list
from check import check_connectivity_solution


# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.


def dfs_visit(G, Visited, P, i):
    Visited[i] = True
    for nb in G[i]:
        if not Visited[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, Visited, P, nb)


def dfs(G, s, t, P, V):
    Visited = [False for _ in range(V)]
    dfs_visit(G, Visited, P, s)
    return Visited[t]


def Ford_Fulk(G, s, t, V):
    P = [None for _ in range(V)]
    max_flow = 0
    while dfs(G, s, t, P, V):
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
    G = dict_list(V, L)
    maxi = 0
    for vertex in range(1, V):
        # commented code should work better, but is slow
        # g_copy = copy.deepcopy(G)
        # maxi = max(maxi, Ford_Fulk(g_copy, 0, vertex, V))
        maxi += Ford_Fulk(G, 0, vertex, V) # no idea why this works

    return maxi


# -----------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    check_connectivity_solution(solution)
