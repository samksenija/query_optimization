import connection

from utils import flush_cache, query_execution_time, calculate_column_distinctiveness, number_of_rows_per_table, truncate_table, select_from_statitistic_table
# from patterns import extract_column_names, extraxt_main_table_name, extract_joined_table_names

cursor = connection.cursor

flush_cache(cursor)

query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;"

identifier = 1
layer_tag = 'original'
change_applied = None
note = None
duration = query_execution_time(cursor, query)

results = []

queries = [
    "EXPLAIN " + query,
    "EXPLAIN FORMAT=JSON " + query,
    "EXPLAIN FORMAT=TREE " + query,
    "EXPLAIN ANALYZE " + query
]

for q in queries:
    cursor.execute(q)
    results.append(cursor.fetchall())
    
columns = ["O_ORDERPRIORITY", "O_CUSTKEY"]
tables = ["orders"]
database_information = "tpch"
column_distinctiveness_array = []
number_of_rows_per_table_array = []

#TODO Cleanup, Add functions
for table in tables:
    number_of_rows_per_table_values = number_of_rows_per_table(cursor, table)
    number_of_rows_per_table_array.append(number_of_rows_per_table_values)
    
    for column in columns:
        column_distinctiveness_value = calculate_column_distinctiveness(cursor, column, table)
        column_distinctiveness_array.append(column_distinctiveness_value)

insert_query = """
    INSERT INTO STATISTICS (
        id, executed_query, 
        explain_query, explain_json, explain_tree, explain_analyze, 
        duration, column_distinctiveness, number_of_rows_per_table, database_information, 
        layer_tag, change_applied, note
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

values = (
    identifier, 
    query, 
    str(results[0][0]), 
    results[1][0][0], 
    results[2][0][0], 
    results[3][0][0], 
    duration,
    str(column_distinctiveness_array), 
    str(number_of_rows_per_table_array), 
    database_information, 
    layer_tag,
    change_applied, 
    note
    )

insert_into_statistics = cursor.execute(insert_query, values) 
connection.connection.commit()

# Occasionaly needed functions
# select_from_statitistic_table(cursor)
# truncate_table(cursor, table)