# Temp import
from process_data import table_information

# This function finds minimum weight in a table_information dictionary, 
# with corresponding table
def min_weight(table_information, already_processed_tables = []):
    weight = float('inf')
    for table in table_information:
        table_name = table['name']

        if table['weight'] < weight and table_name not in already_processed_tables:
            weight = table['weight']
            table_name = table_name

    return [table_name, weight]

# Test call
min_weight(table_information)