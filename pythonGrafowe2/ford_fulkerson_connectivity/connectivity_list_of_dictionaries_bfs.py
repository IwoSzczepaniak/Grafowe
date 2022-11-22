from collections import deque
from dimacs import *
import os, sys, time

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.


def dict_list(V, L):
    dict_list = [{} for _ in range(V)]
    for (x,y,c) in L:
        dict_list[x-1][y-1] = c
        dict_list[y-1][x-1] = 0
    return dict_list


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


def copy_graph(G):
    X = []
    for item in G:
        X.append(item)
    return X


def solution(V,L):
    G = dict_list(V, L)
    maxi = 0
    for vertex in range(1, V):
        # commented code should work better, but is slow
        # g_copy = copy.deepcopy(G)
        # maxi = max(maxi, ford_fulk(g_copy, 0, vertex, V))
        g_copy = copy_graph(G)
        maxi += ford_fulk(g_copy, 0, vertex, V)
    return maxi


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
d_path_copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/connectivity/'
# list file and directories
res = os.listdir(d_path_copy)
beg = time.time()
good = 0
all = 0
for el in res:
    if True:
    # if el != "grid100x100":
        name = d_path_copy + el
        (V, L) = loadWeightedGraph(name)
        start = time.time()
        moja_funkcja = solution(V, L)
        end = time.time()
        poprawny_wynik = int(readSolution(name))
        print("-------------------------")
        if moja_funkcja == poprawny_wynik:
            good += 1
            print("Wynik poprawny dla:", el)
        else:
            print("Wynik niepoprawny dla:", el)
            print("moja funkcja:", moja_funkcja)
            print("poprawny:", poprawny_wynik)
        all += 1

        print("Orientacyjny czas wykonania:", end - start,"s")
        print()

print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:",time.time() - beg, "s")
