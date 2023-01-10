from queue import PriorityQueue


class NodeGroup:
    def __init__(self):
        self.s_points = []
        self.nei_pq = PriorityQueue()

    def __str__(self):
        return f"s_points: {self.s_points}, PQ: {self.nei_pq} "

    def add_edge(self, element):
        if element.exist:
            if element not in self.s_points:
                self.s_points.append(element)
                # for nei_key, nei_value in element.edges.items():
                #     if nei_key not in self.s_points:
                #         self.nei_pq.put((nei_value, nei_key))


def merge_vertices_with_group(sequence, y):
    if y.exist:
        sequence.add_edge(y)
        y.del_all_edges()
