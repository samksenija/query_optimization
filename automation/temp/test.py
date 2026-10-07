from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

Graph = nx.Graph()

left = ['kt', 't', 't', 't', 'mk', 'mk', 'ci', 'chn', 'n', 'k', 'cct1', 'cct2']
right = ['t', 'mk', 'ci', 'cc', 'ci', 'cc', 'cc', 'ci', 'ci', 'mk', 'cc', 'cc']

if len(right) == len(left):
    print(True)

unique_l = list(set(left))
unique_r = list(set(right))
all_elements_unique = list(set(unique_l + unique_r))
processed = []

print(all_elements_unique)

counts_l = Counter(left)
counts_r = Counter(right)

print(counts_l)
print(counts_r)

def switch_ones_to_zeroes(collection):
    for key, element in collection.items():
        if element == 1:
            collection[key] = 0

    return collection

def count_sum_and_max_element(collection):
    sum = 0
    max = 0
    key_of_max = None
    for key, element in collection.items():
        sum = sum + element

        if element > max:
            max = element
            key_of_max = key

    return sum, max, key_of_max

counts_l = switch_ones_to_zeroes(counts_l)
counts_r = switch_ones_to_zeroes(counts_r)

print(counts_l)
print(counts_r)

sum_l, max_l, max_key_l = count_sum_and_max_element(counts_l)
sum_r, max_r, max_key_r = count_sum_and_max_element(counts_r)

print(sum_l, max_l, max_key_l)
print(sum_r, max_r, max_key_r)

primary_array = right
secondary_array = left
max_key = max_key_r

if sum_l > sum_r:
    primary_array = left
    secondary_array = right
    max_key = max_key_l


for index, element in enumerate(primary_array):
    Graph.add_node(max_key)

    if primary_array[index] == max_key:
        Graph.add_edge(max_key, secondary_array[index])
        processed.append(max_key)
        processed.append(secondary_array[index])
        

print(list(set(processed)))

pos = nx.spring_layout(Graph)

nx.draw(Graph, with_labels=True)
edge_labels = nx.get_edge_attributes(Graph, "weight")

nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels)
plt.show()