import os, sys, time
from dimacs import *


def check_lab3(solution):
    sys.setrecursionlimit(10**9)
    dir_path = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe3/graphs-lab3/'
    res = os.listdir(dir_path)
    beg = time.perf_counter()
    good = 0
    all = 0
    for el in res:
        # if el == "mc1":
        if True:
            start = time.perf_counter()
            name = dir_path + el
            (V, L) = loadWeightedGraph(name)

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

            end = time.perf_counter()
            print("Orientacyjny czas wykonania:", end - start,"s")
            print("-------------------------")
            print()


    print("+++++++++++++++++++++++++++++++")
    print(good, "/", all, "poprawnych odpowiedzi")
    print("Łączny czas:",time.perf_counter() - beg)
