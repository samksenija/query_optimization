# Here table, column names are extracted in order for further processing to occur
import re
from temp import test_query

# Here just column names are extracted without the other additional matches
def extract_column_names(query):
    column_names = []
    extract_column_names_first_step = re.findall('(?i)(where| and) (\w+)', query)
    
    for result in extract_column_names_first_step:
        column_names.append(result[1])
        
    return column_names


# Extract main table name
def extraxt_main_table_name(query):
    table_names = []
    extract_main_table_name_first_step =  re.findall('(?i)FROM (\w+)', query)
    
    for result in extract_main_table_name_first_step:
        table_names.append(result)

    return table_names
    

# Extract joined table names
def extract_joined_table_names(query):
    joined_table_names = []
    extract_join_table_names_first_step = re.findall('(?i)JOIN (\w+)', query)
    
    for result in extract_join_table_names_first_step:
        joined_table_names.append(result)
        
    return joined_table_names

# This function is used for checking the filter and join conditions
def joins_and_filters(query):
    joins, filters, like = [], [], []

    joins =re.findall(r"(\w+\.\w+)\s*(=)\s*(\w+\.\w+)", query)
    all_filters = re.findall(r"(?i) ([(^AND)(\w.+)]+) ([=><]) ([A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]+)", query)
    like = re.findall(r"(?i)\b([\w.]+)\s+LIKE\s+([A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]+)", query)

    filters = [x for x in all_filters if x not in joins]
        
    return [joins, filters, like]


def capture_all_the_tabes(query):
    tables = re.findall(r"(?is)\bFROM\b(.*?)\bWHERE\b", query)

    return tables