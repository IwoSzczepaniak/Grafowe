from dimacs import *
import os, sys, time
from collections import deque

# implement solution here


def dict_list(V, L):
    dict_list = [{} for _ in range(V)]
    for (x,y,c) in L:
        dict_list[int(x-1)][int(y-1)] = c
        dict_list[int(y-1)][int(x-1)] = 0
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
    name = copy + el
    (V, L) = loadDirectedWeightedGraph(name)
    start = time.time()
    moja_funkcja = solution(V, L)
    end = time.time()
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

    print("Orientacyjny czas wykonania:", end - start, "s")
    print("-------------------------")
    print()

print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:", time.time() - beg, "s")
