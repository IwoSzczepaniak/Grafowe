import os, sys, time
from dimacs import *


def check_flow_solution_no_grid100x100(solution):
    sys.setrecursionlimit(10**9)
    dir_path = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/flow/'
    res = os.listdir(dir_path)
    beg = time.time()
    good = 0
    all = 0
    for el in res:
        if el != "grid100x100":
            start = time.time()
            name = dir_path + el
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


def check_flow_solution(solution):
    sys.setrecursionlimit(10 ** 9)
    dir_path = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/flow/'
    res = os.listdir(dir_path)
    beg = time.time()
    good = 0
    all = 0
    for el in res:
        start = time.time()
        name = dir_path + el
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


def check_connectivity_solution_no_grid100x100(solution):
    sys.setrecursionlimit(10 ** 9)
    d_path_copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/connectivity/'
    res = os.listdir(d_path_copy)
    beg = time.time()
    good = 0
    all = 0
    for el in res:
        if el != "grid100x100":
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
            print("Orientacyjny czas wykonania:", end - start, "s")
            print()

    print("+++++++++++++++++++++++++++++++")
    print(good, "/", all, "poprawnych odpowiedzi")
    print("Łączny czas:", time.time() - beg, "s")


def check_connectivity_solution(solution):
    sys.setrecursionlimit(10 ** 9)
    d_path_copy = 'C:/Users/iwosz/PycharmProjects/pythonGrafowe2/connectivity/'
    res = os.listdir(d_path_copy)
    beg = time.time()
    good = 0
    all = 0
    for el in res:
        name = d_path_copy + el
        (V, L) = loadWeightedGraph(name)
        start = time.time()
        moja_funkcja = solution(V, L)
        end = time.time()
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

        print("Orientacyjny czas wykonania:", end - start, "s")
        print()

    print("+++++++++++++++++++++++++++++++")
    print(good, "/", all, "poprawnych odpowiedzi")
    print("Łączny czas:", time.time() - beg, "s")
