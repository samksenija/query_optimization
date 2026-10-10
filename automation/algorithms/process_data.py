import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import connection
from patterns import capture_all_the_tabes, joins_and_filters
from temp.job import job_1a

from algorithms.graph.directed_graph_dynamically import directed_graph_dynamically

# TODO Add exception handling
# TODO LIKE, IN filter needs it's own processing - filters can have different selectivity concatenated with AND, OR in single statement
# TODO Cleanup

test_query = job_1a
tables = capture_all_the_tabes(test_query)
tables = tables[0].split(",")

filter_information = joins_and_filters(test_query)
joins = filter_information[0]
filters = filter_information[1]
like = filter_information[2]

table_information = []

left = []
right = []

# Procesing of table name and alias, creating the dictionary structure
for table in tables:
    # Process the result into more meaningful format
    table = table.replace("\n", "").replace(",", "").lstrip().rstrip()
    alias = ''

    table_name = table.split()

    # Check if there is an alias assigned to table
    if len(table_name) >= 3 and table_name[1].lower() == "as":
        alias = table_name[2]

    # Create table dictionary that will be used to process information per table, before join algorithm processing
    table_information.append({
        'name': table_name[0],
        'alias': alias,
        'filter': [], 
        'rows': 0,
        'filtered_column_number': 0,
        'weight': float('inf'),
        'children': []
    })


# Here, a mapping of corresponding table & filter column is conducted
for filter in filters:
    table_name_filter = filter[0].split('.')[0]

    for table in table_information:
        # Tables can be 'summoned' by name or alias, so both are checked
        if table_name_filter == table['name'] or table_name_filter == table['alias']:
            table['filter'].append(filter)


cursor = connection.cursor
# Query for the needed statistical data, total row count + filtered out row count
for table in table_information:
    # Count rows in the table
    row_count_per_table_query = "SELECT COUNT(*) FROM " + table['name'] + ";"

    cursor.execute(row_count_per_table_query)
    row_count_per_table = cursor.fetchall()

    table['rows'] = row_count_per_table[0][0]

    if table['filter']:
        conditions = []

        for filter_item in table['filter']:
            column = filter_item[0].split('.')[-1]
            sign = filter_item[1]
            value = filter_item[2]

            conditions.append(f"{column} {sign} {value}")

        # Count filtered out rows in the table
        filter_count_per_table_query = (
            f"SELECT COUNT(*) FROM {table['name']} "
            f"WHERE {' AND '.join(conditions)};"
        )
            
        cursor.execute(filter_count_per_table_query)
        filter_count_per_table = cursor.fetchall()

        table['filtered_column_number'] = filter_count_per_table[0][0]

# Calculate the weights
for table in table_information:
    # Weight is only relevant if we have both parameters
    # If not, to leave weight at impossibly high number so it's not processed
    if table['filtered_column_number'] and table['rows']:
        weight = 0
        # Weight is calculated as filtered colums count divided by total column count
        weight = table['filtered_column_number'] / table['rows']

        table['weight'] = round(weight, 3)


# Create the parent-child node table relationship
# Example item: ('t.id', '=', 'mc.movie_id')
# Tables on the left side are chosen as parents, and those on the right side of '=' sign are chosen as children
# This choice has no particular meaning
# As one side had to be parent and other the child, left to right model was chosen
for table in table_information:
    for join in joins:
        parent = join[0].split('.')[0]
        child = join[2].split('.')[0]
        if parent == table['name']  or parent == table['alias']:
            table['children'].append(child)


# Prepare JOIN data for graph processing
for join in joins:
    left.append(join[0].split('.')[0])
    right.append(join[2].split('.')[0])


# Prepare weights for graph processing
# TODO Exception handling to be added!
weights_alias = {}
weights_table = {}
for table in table_information:
    if table['alias'] != '':
        weights_alias[table['alias']] = table['weight']

    weights_table[table['name']] = table['weight']

#Testing
directed_graph_dynamically(left, right, weights_alias)