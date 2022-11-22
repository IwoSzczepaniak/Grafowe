from dimacs import *
import os

# # name is string
# def see_graph(name):
#     (V,L) = loadWeightedGraph( name )        # wczytaj graf
#     for (x,y,c) in L:                        # przeglądaj krawędzie z listy
#       print( "krawedz miedzy", x, "i", y,"o wadze", c )


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def m_bottleneck(V, L):
    vertex = [Node(x) for x in range(V+1)]
    for j in range(len(L)):
        check = (vertex[L[j][0]], vertex[L[j][1]])
        birth_parent = find(vertex[L[j][0]])
        destiny_parent = find(vertex[L[j][1]])
        if birth_parent != destiny_parent:
            union(birth_parent, destiny_parent)
            if find(vertex[1]) == find(vertex[2]):
                return L[j][2]
    return None


# -----------------------------------------------------------------------------------------------------------------#

dir_path = r'C:\Users\iwosz\PycharmProjects\pythonGrafowe1\testy'
copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe1/testy/'
# list file and directories
res = os.listdir(dir_path)
i = 0
for el in res:
    i += 1
    name = copy + el
    (V, L) = loadWeightedGraph(name)
    L.sort(key=lambda x: x[2], reverse=True)
    if int(m_bottleneck(V, L)) == int(readSolution(name)):
        print("Wynik poprawny dla:", el)
    else:
        print("Wynik niepoprawny dla:", el)
