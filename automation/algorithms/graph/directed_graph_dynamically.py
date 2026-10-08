from collections import Counter
import networkx as nx

from utils import switch_ones_to_zeroes, count_sum_and_max_element, find_max_key
from plot_graphs import plot_networkx_graph

Graph = nx.DiGraph()

# TODO: To test other cases, if additional cases coverage is needed
# TODO: Test edgecases
# TODO: Cleanup needed
# Prepare the table arrays, and weights
# TODO: Nicer grpah presentation needed with Graphviz

left = ['an', 'n', 'ci', 't', 'mk', 't', 'mc', 'an', 'ci', 'ci', 'mc']
right = ['n', 'ci', 't', 'mk', 'k', 'mc', 'cn', 'ci', 'mc', 'mk', 'mk']

if len(right) != len(left):
    raise Exception("Tables were not processed accordingly, do check!")

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

primary_array = right
secondary_array = left
max_key = max_key_r
side = 'right'

if sum_l > sum_r:
    primary_array = left
    secondary_array = right
    max_key = max_key_l
    side = 'left'

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

            for index_secondary, element_unprocessed in enumerate(secondary_array):
                if element_unprocessed in unprocessed:
                    Graph.add_edge(primary_array[index_secondary], element_unprocessed)
                    processed.append(element_unprocessed)
                    
                    processed = list(set(processed))


plot_networkx_graph(Graph)