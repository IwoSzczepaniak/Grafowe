class Node:
    # słownik  mapujący wierzchołki do których są krawędzie na ich wagi
    def __init__(self, index):
        self.edges = {}
        self.index = index
        self.exist = True
        self.overlord = -1

    # dodaj wagę do krawędzi istniejącej, a jeśli nie istnieje, zwróć zero i dodaj wagę
    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    # usuń krawędź do zadanego wierzchołka
    def delEdge(self, to):
        del self.edges[to]

    # usuń wszystkie krawędzie
    def del_all_edges(self):
        self.exist = False
        self.edges = {}

    # Zwróć krawędzie żeby podglądnąć graf
    def get_edges(self):
        return list(self.edges.keys())

    def get_values(self):
        return sum(self.edges.values())

    def get_index(self):
        return self.index

    # widać w debuggerze
    def __str__(self):
        return f"Values sum: {sum(self.edges.values())}, Edges: {self.edges}"


def create_node_graph(V,L):
    G = [Node(i) for i in range(V)]
    for (x, y, c) in L:
        G[x-1].addEdge(y-1, c)
        G[y-1].addEdge(x-1, c)
    return G


def print_node_graph(G):
    for i, element in enumerate(G):
        # print(f"Wierzchołek nr {i} ma krawędzie o łącznej sumie {element.get_values()} do: {element.get_s_points()}")
        print(element)