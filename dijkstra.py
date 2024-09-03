"""Task 3 - Dijkstras algorithm"""

import graph
import heapq as heapq
import networkx as nx
import matplotlib.pyplot as plt


from dataclasses import dataclass, field


@dataclass(order=True)
class Vertex:
    name: str = field(compare=False)
    distance: float
    visited: bool

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: Vertex(vertex, float("infinity"), False) for vertex in graph}
    distances[start].distance = 0

    unvisited = [v for k, v in distances.items() if v.visited is False]
    heapq.heapify(unvisited)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = heapq.heappop(unvisited)

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if current_vertex.distance == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex.name].items():
            distance = current_vertex.distance + weight["weight"]

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor].distance:
                distances[neighbor].distance = distance

        current_vertex.visited = True
        # Оновимо купу невідвіданих вершин
        unvisited = [v for k, v in distances.items() if v.visited is False]
        heapq.heapify(unvisited)

    return {v.name : v.distance for k, v in distances.items()}


def draw_dijkstra_graph(g, shortest_paths, suffix: None):

    pos = nx.spring_layout(g, seed=3113794652)  # positions for all nodes

    blue = f"#{70:02x}{70:02x}{200:02x}"

    lables = {k: f"{k}\n<{v}>" for k, v in shortest_paths.items()}

    nx.draw_networkx_labels(g, pos, labels=lables, font_size=8)

    nx.draw_networkx_nodes(g, pos, node_color=blue, node_size=500, alpha=0.5)

    nx.draw_networkx_edges(
        g,
        pos,
        width=8,
        alpha=0.3,
        edge_color=blue,
    )
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.title(f"Граф метро Харкова\n{suffix}", wrap=True)
    # plt.text(4, 1, suffix, ha="left", rotation=15, wrap=True)
    plt.text(
        5, 10, "suffix", fontsize=18, style="oblique", ha="center", va="top", wrap=True
    )

    plt.show()


vertexes = [
    Vertex("A", 0, True),
    Vertex("N", 12, True),
    Vertex("B", 15, False),
    Vertex("T", 12, False),
    Vertex("Y", 12, True),
    Vertex("G", 12, False),
]

heapq.heapify(vertexes)

v = [heapq.heappop(vertexes) for _ in range(len(vertexes))]

print(f"{v = }")

if __name__ == "__main__":
    g = graph.build_graph()
    dijkstra = dijkstra(g, "G7")
    sorted_list = {k: v for k, v in sorted(dijkstra.items(), key=lambda item: item[1])}
    result_suffix = f"Найкоротші відстані від вершини {"G7"} = {sorted_list}"
    draw_dijkstra_graph(g, sorted_list, result_suffix)
