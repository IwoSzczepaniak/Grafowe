from collections import deque
from dict_list import dict_list
from check import check_connectivity_solution

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
        for x in residual[u]:
            if not visited[x] and residual[u][x] != 0:
                    parents[x] = u
                    visited[x] = True
                    min_cap = min(capacity, residual[u][x])
                    if x == sink:
                        return min_cap
                    d_queue.append((x, min_cap))


def ford_fulk(G, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    max_flow = 0
    while min_cap := bfs(source, sink, parent, G, ver):
        max_flow += min_cap
        u = sink
        while parent[u] != -1:
            v = parent[u]
            G[u][v] += min_cap
            G[v][u] -= min_cap
            u = v
    return max_flow


def solution(V,L):
    G = dict_list(V, L)
    maxi = 0
    for vertex in range(1, V):
        # commented code should work better, but is slow
        # g_copy = copy.deepcopy(G)
        # maxi = max(maxi, ford_fulk(g_copy, 0, vertex, V))
        maxi += ford_fulk(G, 0, vertex, V) # no idea why this works
    return maxi


# -----------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    check_connectivity_solution(solution)
