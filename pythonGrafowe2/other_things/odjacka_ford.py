from dimacs import *
import os, sys, time


def change_to_adj_directed(Edges, V):
    G = [[] for _ in range(V)]
    for u, v, w in Edges:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, 0))
    return G


def find_parent(G, u, v):
    for i, x in enumerate(G[u]):
        if x[0] == v:
            return i


def dfs(G, start, end):
    n = len(G)
    min_w = float('inf')
    st = []
    vis = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    parent[start] = start
    st.append(start)
    while st:
        u = st.pop()
        vis[u] = True
        if u == end:
            break
        for v, w in G[u]:
            if not vis[v] and w > 0:
                st.append(v)
                parent[v] = u
                min_w = min(min_w, w)

    if vis[end]:
        curr = end
        while curr != start:
            p = find_parent(G, curr, parent[curr])
            c = find_parent(G, parent[curr], curr)
            G[curr][p] = (G[curr][p][0], G[curr][p][1] + min_w)
            G[parent[curr]][c] = (G[parent[curr]][c][0], G[parent[curr]][c][1] - min_w)

            curr = parent[curr]
        return min_w
    return 0


def ford_fulkerson(G, start, end):
    flow = 0
    while (curr_flow := dfs(G, start, end)) > 0:
        flow += curr_flow
    return flow


def main(V, L):
    G = change_to_adj_directed(L, V)
    n = len(G)
    result = ford_fulkerson(G, 0, n - 1)
    return result



sys.setrecursionlimit(10 ** 9)
# dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe2\flow'
dir_path = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/flow/'
# list file and directories
res = os.listdir(dir_path)
beg = time.time()
good = 0
all = 0
for el in res:
    if True:
        start = time.time()
        name = dir_path + el
        (V, L) = loadDirectedWeightedGraph(name)

        moja_funkcja = main(V, L)
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