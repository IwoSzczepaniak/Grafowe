from dimacs import *
import os, sys, time
from collections import deque
import copy

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


def matrix_graph(V, L):
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for (x,y,c) in L:
        matrix[x-1][y-1] = 1
    return matrix


def solution(V,L):
    matrix_g = matrix_graph(V, L)
    result = 0
    for vertex in range(1, V):
        g_copy = copy.deepcopy(matrix_g)
        result = max(result, ford_fulk(g_copy, 0, vertex, V))
    return result


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe2\connectivity'
d_path_copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/connectivity/'
# list file and directories
res = os.listdir(d_path_copy)
beg = time.time()
good = 0
all = 0
for el in res:
    if el != "grid100x100":
    # if el == "cycle":
        start = time.time()
        name = d_path_copy + el
        (V, L) = loadWeightedGraph(name)

        moja_funkcja = solution(V, L)
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

        end = time.time()
        print("Orientacyjny czas wykonania:", end - start,"s")
        print()

print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:",time.time() - beg, "s")
