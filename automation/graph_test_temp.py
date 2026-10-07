import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph

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

#NetworkX
# T = nx.DiGraph()

# T.add_edges_from([
#     ("Root", "A", {"weight": 5}),
#     ("Root", "B", {"weight": 15}),
#     ("A", "C", {"weight": 5}),
#     ("A", "D", {"weight": 0}),
#     ("B", "E", {"weight": 8}),
#     ("B", "F", {"weight": 3}),
#     ("C", "G", {"weight": 7}),
#     ("C", "H", {"weight": 2}),
# ])

# pos = nx.nx_agraph.graphviz_layout(T, prog="dot")

# nx.draw(T, pos, with_labels=True, arrows=True, node_color="blue", node_size=1500, font_size=10, arrowsize=10)

# edge_labels = nx.get_edge_attributes(T, "weight")

# nx.draw_networkx_edge_labels(T, pos, edge_labels=edge_labels, font_color="red", font_size=10)

# plt.show()

# Graphviz
# dot = Digraph(format="png")

# dot.attr(
#     rankdir="TB",
#     nodesep="0.5",
#     rabksep="0.8"
# )

# dot.node("Root","Root")
# dot.node("A","A")
# dot.node("B","B")
# dot.node("C","C")
# dot.node("D","D")
# dot.node("E","E")
# dot.node("F","F")
# dot.node("G","G")
# dot.node("H","H")

# dot.edge("Root", "A", label="5")
# dot.edge("Root", "B", label="3")

# dot.edge("A", "C", label="2")
# dot.edge("A", "D", label="7")

# dot.edge("B", "E", label="4")
# dot.edge("B", "F", label="6")

# dot.edge("C", "G", label="1")
# dot.edge("C", "H", label="8")

# dot.render("my_tree", view=True)

from graphviz import Digraph

dot = Digraph(format="png")

dot.attr(
    rankdir="TB",
    nodesep="0.5",
    ranksep="0.8"
)

dot.node("Root", "Root\nweight = 0")
dot.node("A", "A\nweight = 5")
dot.node("B", "B\nweight = 3")
dot.node("C", "C\nweight = 2")
dot.node("D", "D\nweight = 7")
dot.node("E", "E\nweight = 4")
dot.node("F", "F\nweight = 6")
dot.node("G", "G\nweight = 1")
dot.node("H", "H\nweight = 8")

dot.edge("Root", "A")
dot.edge("Root", "B")

dot.edge("A", "C")
dot.edge("A", "D")

dot.edge("B", "E")
dot.edge("B", "F")

dot.edge("C", "G")
dot.edge("C", "H")

dot.render("my_tree", view=True)