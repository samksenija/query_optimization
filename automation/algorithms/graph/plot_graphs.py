import networkx as nx
import matplotlib.pyplot as plt

def plot_networkx_graph(Graph):
    pos = nx.nx_agraph.graphviz_layout(Graph, prog="dot")

    nx.draw(Graph, pos, with_labels=True, arrows=True, node_color="blue", node_size=1500, font_size=10, arrowsize=10)

    edge_labels = nx.get_edge_attributes(Graph, "weight")

    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, font_color="red", font_size=10)

    plt.show()