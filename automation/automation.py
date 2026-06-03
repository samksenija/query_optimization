import connection

from utils import flush_cache, query_execution_time, calculate_column_distinctiveness, number_of_rows_per_table, truncate_table, select_from_statitistic_table

cursor = connection.cursor

flush_cache(cursor)

query = "SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';"

identifier = 1
layer_tag = '1st'
change_applied = "Change of filter column order"
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
    
column = ""
table = ""
column_distinctiveness = calculate_column_distinctiveness(cursor, column, table)
number_of_rows_per_table = number_of_rows_per_table(cursor, table)

insert_query = """
    INSERT INTO STATISTICS (
        id, executed_query, 
        explain_query, explain_json, explain_tree, explain_analyze, 
        duration, column_distinctiveness, number_of_rows_per_table, database_information, 
        layer_tag, change_applied, note
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

values = (
    identifier, 
    query, 
    str(results[0][0]), 
    results[1][0][0], 
    results[2][0][0], 
    results[3][0][0], 
    duration, 
    layer_tag,
    change_applied, 
    note
    )

insert_into_statistics = cursor.execute(insert_query, values) 
connection.connection.commit()

# Occasionaly needed functions
# select_from_statitistic_table(cursor)
# truncate_table(cursor, table)
