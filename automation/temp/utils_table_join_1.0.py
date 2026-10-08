# This function finds minimum weight in a table_information dictionary, 
# with corresponding table name and children
def min_weight(table_information, already_processed_tables = []):
    weight = float('inf')
    table_name = ''
    children = []

    for table in table_information:
        if (table['weight'] < weight and 
            table['name'] not in already_processed_tables and table['alias'] not in already_processed_tables):
            weight = table['weight']
            table_name = table['name']
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
            

# from process_data import table_information
# Added for tet purposes
table_information = [
    {
        'name': 'char_name',
        'alias': 'chn',
        'filter': [],
        'rows': 4314872,
        'filtered_column_number': 0,
        'weight': float('inf'),
        'children': ['ci']
    },
    {
        'name': 'cast_info',
        'alias': 'ci',
        'filter': [],
        'rows': 63475827,
        'filtered_column_number': 0,
        'weight': float('inf'),
        'children': ['mc']
    },
    {
        'name': 'company_name',
        'alias': 'cn',
        'filter': [
            ('cn.country_code', '=', "'[ru]'")
        ],
        'rows': 106736,
        'filtered_column_number': 663,
        'weight': 0.006,
        'children': ['mc']
    },
    {
        'name': 'company_type',
        'alias': 'ct',
        'filter': [],
        'rows': 4,
        'filtered_column_number': 0,
        'weight': float('inf'),
        'children': ['mc']
    },
    {
        'name': 'movie_companies',
        'alias': 'mc',
        'filter': [],
        'rows': 4958296,
        'filtered_column_number': 0,
        'weight': float('inf'),
        'children': []
    },
    {
        'name': 'role_type',
        'alias': 'rt',
        'filter': [
            ('rt.role', '=', "'actor'")
        ],
        'rows': 12,
        'filtered_column_number': 1,
        'weight': 0.083,
        'children': ['ci']
    },
    {
        'name': 'title',
        'alias': 't',
        'filter': [
            ('t.production_year', '>', '2005')
        ],
        'rows': 4736114,
        'filtered_column_number': 2539122,
        'weight': 0.536,
        'children': ['mc', 'ci']
    }
]

table, weight, children = min_weight(table_information)
print(table, weight, children)
processed_tables = []

if table:
    processed_tables.append(table)

childs_children = []

if len(children) > 0:
    childs_children, weight = find_child_table_and_check_weight(children, table_information, weight)

if len(childs_children) > 0:
    pass
else: 
    processed_tables.append(children[0].replace("'", ""))
    table, weight, children = min_weight(table_information, processed_tables)
    print(table, weight, children)
    # Establish the movement of traversing trough nodes, explore the children and weights
    # Until you can, move back up the tree if no more children down the tree
    # Boundaries in circual movement, with concatenating to the processed nodes
    if len(children) > 0:
        childs_children, weight = find_child_table_and_check_weight(children, table_information, weight)
        print(childs_children, weight)

print(processed_tables)