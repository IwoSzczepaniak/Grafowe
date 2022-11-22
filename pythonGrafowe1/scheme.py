from dimacs import *
import os, sys, time


# implement solution here


def solution(V, L, visited, stream):
    return 0


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
    moja_funkcja = solution(V, L, visited, stream)
    poprawny_wynik = int(readSolution(name))
    if moja_funkcja == poprawny_wynik:
        print("Wynik poprawny dla:", el)
    else:
        print("Wynik niepoprawny dla:", el, "moja funkcja:", moja_funkcja, "poprawny:", poprawny_wynik)
    end = time.time()
    print("Czas wykonania:", end - start,"s")
    print()