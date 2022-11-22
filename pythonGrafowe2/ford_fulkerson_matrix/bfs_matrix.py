from dimacs import *
import os, sys, time
from collections import deque


def matrix_graph(V, L):
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for (x,y,c) in L:
        matrix[x-1][y-1] = c
    return matrix


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
sys.setrecursionlimit(10 ** 9)
dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe2\flow'
copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/flow/'
# list file and directories
res = os.listdir(copy)
beg = time.time()
good = 0
all = 0
for el in res:
    if el != "grid100x100":
        start = time.time()
        name = copy + el
        (V, L) = loadDirectedWeightedGraph(name)

        moja_funkcja = solution(V, L)
        poprawny_wynik = int(readSolution(name))
        print()
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
        print("Orientacyjny czas wykonania:", end - start, "s")
        print("-------------------------")
        print()

print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:", time.time() - beg)
