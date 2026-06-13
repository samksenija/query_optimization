# Here column names are extracted in order for further processing to occur
import re

column_names = []
table_names = []
joined_table_names = []

# Test queries for validation of RegEx
query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910 AND TEST = 15;"
query_multitable_join = "SELECT c.name, o.order_id, p.product_name, oi.quantity, p.price FROM customers c JOIN orders o ON c.customer_id = o.customer_id JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id;"

# RegEx definitions
extract_column_names_first_step = re.findall('(?i)(where| and) (\w+)', query)
extract_main_table_name_first_step =  re.findall('(?i)FROM (\w+)', query)
extract_join_table_names_first_step = re.findall('(?i)JOIN (\w+)', query_multitable_join)

# print functions are just temporary add on for testing purposes
# Here just column names are extracted without the other additional matches
def extract_column_names(extract_column_names_first_step, query):
    extract_column_names_first_step = re.findall('(?i)(where| and) (\w+)', query)
    
    for result in extract_column_names_first_step:
        column_names.append(result[1])
        
    print(column_names)
    return column_names


# Extract main table name
def extraxt_main_table_name(extract_main_table_name_first_step, query):
    extract_main_table_name_first_step =  re.findall('(?i)FROM (\w+)', query)
    
    for result in extract_main_table_name_first_step:
        table_names.append(result)

    print(table_names)
    return table_names
    

# Extract joined table names
def extract_joined_table_names(extract_join_table_names_first_step, query):
    extract_join_table_names_first_step = re.findall('(?i)JOIN (\w+)', query)
    
    for result in extract_join_table_names_first_step:
        joined_table_names.append(result)
        
    print(joined_table_names)
    return joined_table_names


# Internal calls
# extract_column_names(extract_column_names_first_step, query)
# extraxt_main_table_name(extract_main_table_name_first_step, query)
# extract_joined_table_names(extract_join_table_names_first_step, query_multitable_join)