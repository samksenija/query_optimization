import connection

from utils import flush_cache, query_execution_time

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

insert_query = """
    INSERT INTO STATISTICS (id, executed_query, explain_query, explain_json, 
        explain_tree, explain_analyze, duration, layer_tag, change_applied, note) 
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
