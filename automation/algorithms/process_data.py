import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import connection
from patterns import capture_all_the_tabes, joins_and_filters
from temp import test_query


# TODO Add exception handling

tables = capture_all_the_tabes(test_query)
tables = tables[0].split(",")

filter_information = joins_and_filters(test_query)
joins = filter_information[0]
filters = filter_information[1]
like = filter_information[2]

table_information = []

for table in tables:
    # process the result into more meaningful format
    table = table.replace("\n", "").replace(",", "").lstrip().rstrip()
    alias = ''

    table_name = table.split()

    # check if there is an alias assigned to table
    if len(table_name) >= 3 and table_name[1].lower() == "as":
        alias = table_name[2]

    # Create table dictionary that will be used to process information per table, before joins
    table_information.append({
        'name': table_name[0],
        'alias': alias,
        'filter': []
    })


# Here, a mapping of corresponding table & filter column is conducted
for filter in filters:
    table_name_filter = filter[0].split('.')[0]

    for table in table_information:
        if table_name_filter == table['name'] or table_name_filter == table['alias']:
            table['filter'].append(filter)


cursor = connection.cursor
# Query for the needed statistical data
for table in table_information:
    row_count_per_table_query = "SELECT COUNT(*) FROM " + table['name'] + ";"

    cursor.execute(row_count_per_table_query)
    row_count_per_table = cursor.fetchall()

    print(row_count_per_table)