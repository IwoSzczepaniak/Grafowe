from dimacs import *
import os, sys, time
import copy

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# On every step use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution.

# implement solution here


def adjacency_list(V, L):
    adj_graph = [[] for _ in range(V)]
    for (x,y,c) in L:
        adj_graph[x-1].append([y-1, c])
        adj_graph[y-1].append([x-1, 0])
    return adj_graph


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
        while v != s:
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

# def maxi(graph):
#     res = 0
#     for el in graph:
#         res = max(el,res)
#     return res

def solution(V,L):
    G = adjacency_list(V, L)
    maxi = 0
    for vertex in range(1, V):
        g_copy = copy.deepcopy(G)
        maxi = max(maxi, Ford_Fulk(g_copy, 0, vertex))
    return maxi
    # return result


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
    # if True:
        start = time.time()
        name = d_path_copy + el
        (V, L) = loadDirectedWeightedGraph(name)

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
