from adjacency_list import adjacency_list
from check import check_flow_solution


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in G[i]:
        if not V[nb[0]] and nb[1] != 0:
            P[nb[0]] = i
            dfs_visit(G, V, P, nb[0])


def dfs(G, P, s, t):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, P, s, t):
        curr_flow = 10**9
        current = t
        while current != s: # cofanie do początku szukając bottlenecka
            parent = P[current]
            for i in range(len(G[parent])):
                if G[parent][i][0] == current:
                    curr_flow = min(curr_flow, G[parent][i][1])
                    break
            current = P[current]
        max_flow += curr_flow

        v = t
        while v != s: # uaktualnie grafu po przepływie
            u = P[v]
            for i in range(len(G[u])):
                if G[u][i][0] == v:
                    G[u][i][1] -= curr_flow
                    break
            for i in range(len(G[v])):
                if G[v][i][0] == u:
                    G[v][i][1] += curr_flow
                    break
            v = P[v]
    return max_flow



def solution(V, L):
    adj_g = adjacency_list(V, L)
    return Ford_Fulk(adj_g, 0, V-1)


# -----------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    check_flow_solution(solution)