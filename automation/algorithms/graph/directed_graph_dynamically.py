from collections import Counter
import networkx as nx

from algorithms.graph.utils import switch_ones_to_zeroes, count_sum_and_max_element, find_max_key
from algorithms.graph.plot_graphs import plot_networkx_graph

left = ['t', 't', 'chn', 'rt', 'cn', 'ct', 'ci']
right = ['mc', 'ci', 'ci', 'ci', 'mc', 'mc', 'mc']
weights = {'chn': float('inf'), 'ci': float('inf'), 'cn': 0.006, 'ct': float('inf'), 'mc': float('inf'), 'rt': 0.083, 't': 0.536}

# Number of rows to be processed TODO add & plays a factor in traversing the graph
def directed_graph_dynamically(left, right, weights):
    if len(right) != len(left):
        raise Exception("Tables were not processed accordingly, do check!")

    Graph = nx.DiGraph()

    unique_l = list(set(left))
    unique_r = list(set(right))
    all_elements_unique = list(set(unique_l + unique_r))
    processed = []
    unprocessed = []

    counts_l = Counter(left)
    counts_r = Counter(right)

    counts_l = switch_ones_to_zeroes(counts_l)
    counts_r = switch_ones_to_zeroes(counts_r)

    sum_l, max_l = count_sum_and_max_element(counts_l)
    sum_r, max_r = count_sum_and_max_element(counts_r)

    max_key_l = find_max_key(counts_l, processed)
    max_key_r = find_max_key(counts_r, processed)

    primary_array, secondary_array, max_key, side = right, left, max_key_r, "right"

    if sum_l > sum_r:
        primary_array, secondary_array, max_key, side = left, right, max_key_l, "left"

    for i in primary_array:
        if max_key:
            for index, element in enumerate(primary_array):
                Graph.add_node(max_key)

                if primary_array[index] == max_key:
                    Graph.add_edge(max_key, secondary_array[index])
                    processed.append(max_key)
                    processed.append(secondary_array[index])

                    processed = list(set(processed))

            if side == 'left':
                max_key = find_max_key(counts_l, processed)
            else:
                max_key = find_max_key(counts_r, processed)
        else: 
            if len(processed) != len(all_elements_unique):
                unprocessed = [x for x in all_elements_unique if x not in processed]

                # Mirror unprocessed from both sides - left & right
                # TODO optimize the functions
                for index_secondary, element_unprocessed in enumerate(secondary_array):
                    if element_unprocessed in unprocessed:
                        Graph.add_edge(primary_array[index_secondary], element_unprocessed)
                        processed.append(element_unprocessed)
                        
                        processed = list(set(processed))

                for index_secondary, element_unprocessed in enumerate(primary_array):
                    if element_unprocessed in unprocessed:
                        Graph.add_edge(secondary_array[index_secondary], element_unprocessed)
                        processed.append(element_unprocessed)
                                        
                        processed = list(set(processed))

    for node in Graph.nodes:
        Graph.nodes[node]["weight"] = weights[node]

    plot_networkx_graph(Graph)