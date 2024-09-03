"""Task 1 - Build Graph"""

import networkx as nx
import matplotlib.pyplot as plt

NODES = [
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
    "B8",
    "G1",
    "G2",
    "G3",
    "G4",
    "G5",
    "G6",
    "G7",
    "G8",
    "G9",
    "G10",
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
    "R7",
    "R8",
    "R9",
    "R10",
    "R11",
    "R12",
    "R13",
    "R14",
]

EDGES = [
    ("R1", "R2", 3),
    ("R2", "R3", 7),
    ("R3", "R4", 15),
    ("R4", "R5", 7),
    ("R5", "R6", 8),
    ("R6", "R7", 3),
    ("R7", "R8", 4),
    ("R8", "R9", 12),
    ("R9", "R10", 4),
    ("R10", "R11", 7),
    ("R11", "R12", 5),
    ("R12", "R13", 3),
    ("R13", "R14", 7),
    ("B1", "B2", 8),
    ("B2", "B3", 9),
    ("B3", "B4", 10),
    ("B4", "B5", 1),
    ("B5", "B6", 11),
    ("B6", "B7", 7),
    ("B7", "B8", 6),
    ("G1", "G2", 3),
    ("G2", "G3", 5),
    ("G3", "G4", 9),
    ("G4", "G5", 8),
    ("G5", "G6", 2),
    ("G6", "G7", 2),
    ("G7", "G8", 2),
    ("G8", "G9", 5),
    ("G9", "G10", 8),
    ("B7", "G7", 10),
    ("R4", "B8", 1),
    ("R6", "G10", 3),
]


def build_graph():
    """Build graph"""
    g = nx.Graph()
    g.add_nodes_from(NODES)
    # g.add_edges_from(EDGES)
    g.add_weighted_edges_from(EDGES)
    return g


def draw_graph(g):
    blue_nodes = [n for n in NODES if n[0] == "B"]
    green_nodes = [n for n in NODES if n[0] == "G"]
    red_nodes = [n for n in NODES if n[0] == "R"]

    blue_edges = [e for e in EDGES if e[0][0] == "B"]
    green_edges = [e for e in EDGES if e[0][0] == "G"]
    red_edges = [e for e in EDGES if e[0][0] == "R"]

    num_nodes = g.number_of_nodes()
    num_edges = g.number_of_edges()
    degree_centrality = dict(nx.degree_centrality(g))
    max_degree = 0
    max_degree_list = []
    for k, v in degree_centrality.items():
        if v > max_degree:
            max_degree_list = [k]
            max_degree = v
        elif v == max_degree:
            max_degree_list.append(k)

    pos = nx.spring_layout(g, seed=3113794652)  # positions for all nodes

    blue = f"#{70:02x}{70:02x}{200:02x}"
    green = f"#{70:02x}{200:02x}{70:02x}"
    red = f"#{200:02x}{70:02x}{70:02x}"

    nx.draw_networkx_labels(g, pos, font_size=8)

    nx.draw_networkx_nodes(g, pos, nodelist=green_nodes, node_color=green)
    nx.draw_networkx_nodes(g, pos, nodelist=blue_nodes, node_color=blue)
    nx.draw_networkx_nodes(g, pos, nodelist=red_nodes, node_color=red)

    nx.draw_networkx_edges(
        g,
        pos,
        edgelist=blue_edges,
        width=8,
        alpha=0.7,
        edge_color=blue,
    )
    nx.draw_networkx_edges(
        g,
        pos,
        edgelist=green_edges,
        width=8,
        alpha=0.7,
        edge_color=green,
    )

    nx.draw_networkx_edges(
        g,
        pos,
        edgelist=red_edges,
        width=8,
        alpha=0.7,
        edge_color=red,
    )

    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.title(
        f"Мапа метро Харкова\nВершин = {num_nodes}; Ребер = {num_edges};\nВершини з MAX ступенем = {max_degree_list}"
    )
    plt.show()
