from dimacs import *
import os, sys, time
from queue import PriorityQueue


def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    for (x,y,c) in L:
        adj_graph[int(x-1)].append((int(y-1), int(c)))
        adj_graph[int(y-1)].append((int(x-1), int(c)))
    return adj_graph


def dijkstra(G, s, visited, stream):
    pq = PriorityQueue()
    pq.put((0, s))
    stream[s] = 10**9
    while not pq.empty():
        (current_stream, current_vertex_nr) = pq.get()
        visited[current_vertex_nr] = True
        for neighbor in G[current_vertex_nr]:
                if not visited[neighbor[0]]:
                    distance = max(stream[neighbor[0]], min(stream[current_vertex_nr], neighbor[1]))
                    if distance > stream[neighbor[0]]:
                        stream[neighbor[0]] = distance
                        pq.put((-1 * stream[neighbor[0]], neighbor[0]))
    return stream[1]


def m_bottleneck(V, L, visited, stream):
    adj_graph = adjacency_list(V, L)
    return dijkstra(adj_graph, 0, visited, stream)


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe1\testy'
copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe1/testy/'
# list file and directories
res = os.listdir(copy)
for el in res:
# el = "pp100"
    start = time.time()
    name = copy + el
    (V, L) = loadWeightedGraph(name)

    visited = [None for _ in range(V)]
    stream = [-1 for _ in range(V)]
    moja_funkcja = m_bottleneck(V, L, visited, stream)
    poprawny_wynik = int(readSolution(name))
    if moja_funkcja == poprawny_wynik:
        print("Wynik poprawny dla:", el)
    else:
        print("Wynik niepoprawny dla:", el, "moja funkcja:", moja_funkcja, "poprawny:", poprawny_wynik)
    end = time.time()
    print("Czas wykonania:", end - start,"s")
    print()