from dimacs import *
import os, sys, time

# idea
# First of all, create graph with all weights equals to 1.
# Randomise one vertex and treat it as a source. Then iterate through all other vertices and treat them as sinks.
# Last step is to use max_flow algorithm(Ford-Fulkerson) on graph - it will find solution (mathematically proved)

# implement solution here



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
        print("Orientacyjny wykonania:", end - start,"s")
        print()

    print("+++++++++++++++++++++++++++++++")
    print(good, "/", all, "poprawnych odpowiedzi")
    print("Łączny czas:",time.time() - beg, "s")
