from dimacs import *
import os, sys, time

# implement solution here


def matrix_graph(V, L):
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for (x,y,c) in L:
        matrix[x-1][y-1] = c
    return matrix


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in range(len(G)):
        if not V[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, V, P, nb)


def dfs(G, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def Ford_Fulk(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, s, t, P):
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



def solution(V, L):
    matrix_g = matrix_graph(V, L)
    return Ford_Fulk(matrix_g, 0, V-1)


# -----------------------------------------------------------------------------------------------------------------#
sys.setrecursionlimit(10**9)
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
        print("Orientacyjny czas wykonania:", end - start,"s")
        print("-------------------------")
        print()

        
print("+++++++++++++++++++++++++++++++")
print(good, "/", all, "poprawnych odpowiedzi")
print("Łączny czas:",time.time() - beg)
