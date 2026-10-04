# from process_data import table_information
from utils import min_weight, find_child_table_and_check_weight

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
processed_tables = []

if table:
    processed_tables.append(table)

if len(children) > 0:
    childs_children, weight = find_child_table_and_check_weight(children, table_information, weight)

if len(childs_children) > 0:
    pass
else: 
    processed_tables.append(children[0].replace("'", ""))

print(processed_tables)