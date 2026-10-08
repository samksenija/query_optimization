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