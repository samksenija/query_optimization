import networkx as nx
import matplotlib.pyplot as plt

# TODO: Nicer grpah presentation needed with Graphviz, leave NetworkX for test purposes

# Plot the weights alongside the graph
def plot_networkx_graph(Graph):
    plt.figure(figsize=(9, 6))  

    pos = nx.nx_agraph.graphviz_layout(Graph, prog="dot")

    nx.draw(Graph, pos, with_labels=True, arrows=True, node_color="white", edgecolors="black", node_size=700, font_size=10, arrowsize=10)

    labels = {
        node: f"{Graph.nodes[node]['weight']:>25}"
        for node in Graph.nodes
    }

    nx.draw_networkx_labels(Graph, pos, labels = labels, font_color="black", font_size=10)

    plt.show()