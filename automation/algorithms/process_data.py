import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from patterns import capture_all_the_tabes, joins_and_filters
from temp import test_query

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

    # create the table information
    table_information.append({
        'name': table_name[0],
        'alias': alias
    })