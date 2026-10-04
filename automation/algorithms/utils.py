# This function finds minimum weight in a table_information dictionary, 
# with corresponding table name and children
def min_weight(table_information, already_processed_tables = []):
    weight = float('inf')
    table_name = ''
    children = []

    for table in table_information:
        table_name = table['name']

        if table['weight'] < weight and table_name not in already_processed_tables:
            weight = table['weight']
            table_name = table_name
            children = table['children']

    return table_name, weight, children

# This is now covering if there is only one child,  TODO: add multiple handling
def find_child_table_and_check_weight(table_name, table_information, weight):
    table_name = table_name[0].replace("'", "")
    name, weight_value = [], False

    for table in table_information:
        if table_name == table['name'] or table_name == table['alias']:
            name, weight_value = table['children'], weight

    return name, weight_value
            

