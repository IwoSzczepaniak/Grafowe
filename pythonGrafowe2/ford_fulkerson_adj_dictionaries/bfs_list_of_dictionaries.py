from collections import deque
from dict_list import dict_list
from check import check_flow_solution

# implement solution here


def bfs(s, sink, parents, graph, ver):
    visited = [False for _ in range(ver)]
    visited[s] = True
    parents[s] = -1
    d_queue = deque()
    min_cap = 10**10
    d_queue.append((s, min_cap))
    while d_queue:
        u, capacity = d_queue.popleft()
        for x in graph[u]:
            if not visited[x] and graph[u][x] != 0:
                    parents[x] = u
                    visited[x] = True
                    min_cap = min(capacity, graph[u][x])
                    if x == sink:
                        return min_cap
                    d_queue.append((x, min_cap))


def ford_fulk(G, source, sink, ver):
    parent = [-1 for _ in range(ver)]
    max_flow = 0
    min_cap = bfs(source, sink, parent, G, ver)
    while min_cap:
        max_flow += min_cap
        u = sink
        while u != source:
            v = parent[u]
            G[u][v] += min_cap
            G[v][u] -= min_cap
            u = v
        min_cap = bfs(source, sink, parent, G, ver)
    return max_flow


def solution(V, L):
    dict_list_graph = dict_list(V, L)
    return ford_fulk(dict_list_graph, 0, V-1, V)


if __name__ == "__main__":
    check_flow_solution(solution)
