from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

Graph = nx.DiGraph()

left = ['kt', 't', 't', 't', 'mk', 'mk', 'ci', 'chn', 'n', 'k', 'cct1', 'cct2']
right = ['t', 'mk', 'ci', 'cc', 'ci', 'cc', 'cc', 'ci', 'ci', 'mk', 'cc', 'cc']

if len(right) == len(left):
    print(True)

unique_l = list(set(left))
unique_r = list(set(right))
all_elements_unique = list(set(unique_l + unique_r))
processed = []
unprocessed = []

counts_l = Counter(left)
counts_r = Counter(right)


def switch_ones_to_zeroes(collection):
    for key, element in collection.items():
        if element == 1:
            collection[key] = 0

    return collection

def count_sum_and_max_element(collection):
    sum = 0
    max = 0
    for key, element in collection.items():
        sum = sum + element

        if element > max:
            max = element

    return sum, max

def find_max_key(collection, processed):
    key_of_max = None
    max = 0
    for key, element in collection.items():

        if element > max and key not in processed:
            max = element
            key_of_max = key
    
    return key_of_max


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
        if len(processed)  != len(all_elements_unique):
            unprocessed = [x for x in all_elements_unique if x not in processed]

            for index_secondary, element_unprocessed in enumerate(secondary_array):
                if element_unprocessed in unprocessed:
                    Graph.add_edge(primary_array[index_secondary], element_unprocessed)
                    processed.append(element_unprocessed)
                    
                    processed = list(set(processed))
        

pos = nx.nx_agraph.graphviz_layout(Graph, prog="dot")

nx.draw(Graph, pos, with_labels=True, arrows=True, node_color="blue", node_size=1500, font_size=10, arrowsize=10)

edge_labels = nx.get_edge_attributes(Graph, "weight")

nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, font_color="red", font_size=10)

plt.show()