import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()

# G.add_node("A")
# G.add_node("B")
# G.add_edge("A", "B", weight=10)
# G.add_edge("B", "C", weight=10)
# G.add_edge("A", "D", weight=10)
# G.add_edge("A", "E", weight=10)

# print(G.nodes)
# print(G.edges)

# pos = nx.spring_layout(G)

# nx.draw(G, with_labels=True)
# edge_labels = nx.get_edge_attributes(G, "weight")

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()

T = nx.DiGraph()

T.add_edges_from([
    ("Root", "A", {"weight": 5}),
    ("Root", "B", {"weight": 15}),
    ("A", "C", {"weight": 5}),
    ("A", "D", {"weight": 0}),
    ("B", "E", {"weight": 8}),
    ("B", "F", {"weight": 3}),
    ("C", "G", {"weight": 7}),
    ("C", "H", {"weight": 2}),
])

pos = nx.nx_agraph.graphviz_layout(T, prog="dot")

nx.draw(T, pos, with_labels=True, arrows=True, node_color="blue", node_size=1500, font_size=10, arrowsize=10)

edge_labels = nx.get_edge_attributes(T, "weight")

nx.draw_networkx_edge_labels(T, pos, edge_labels=edge_labels, font_color="red", font_size=10)

plt.show()