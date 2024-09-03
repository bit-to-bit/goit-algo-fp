"""Task 5 - Path visualization DFS and BFS"""

import uuid
import heapq as heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_hex_gradient(current_color, step_r, step_g, step_b):
    r = int(current_color[1:3], 16)
    g = int(current_color[3:5], 16)
    b = int(current_color[5:7], 16)
    r = r + step_r if r + step_r < 256 else 0
    g = g + step_g if g + step_g < 256 else 0
    b = b + step_b if b + step_b < 256 else 0
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_tree(tree_root, title=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міто
    plt.figure(title, figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_tree(binary_heap):
    if not binary_heap:
        return
    last = len(binary_heap) - 1
    nodes = [Node(e) for e in binary_heap]
    for i, n in enumerate(nodes):
        n.left = nodes[2 * i + 1] if 2 * i + 1 <= last else None
        n.right = nodes[2 * i + 2] if 2 * i + 2 <= last else None
    return nodes[0]


def tree_dfs(root_node):

    color = "#124080"
    visited = set()
    stack = [root_node]
    while stack:
        node = stack.pop()
        node.color = color
        color = generate_hex_gradient(color, 0, 10, 10)
        if node not in visited:
            visited.add(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return root_node


def tree_bfs(root_node):

    color = "#124080"
    visited = set()
    queue = deque([root_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = color
            color = generate_hex_gradient(color, 0, 10, 10)
            visited.add(node)
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
    return root_node


if __name__ == "__main__":
    h = [3, 44, 7, 15, 77, 8, 17, 4, 2, 1, 33, 22]
    heapq.heapify(h)
    tree = build_tree(h)
    print("Enter path search algoritm type to continue:")
    print("1 - DFS >> Depth first search")
    print("2 - BFS >> Breadth first search")
    print(">>")
    algorithm = input()
    if algorithm == "1":
        tree_dfs(tree)
        draw_tree(tree, "DFS path search")
    elif algorithm == "2":
        tree_bfs(tree)
        draw_tree(tree, "BFS path search")
    else:
        print("Try again")
