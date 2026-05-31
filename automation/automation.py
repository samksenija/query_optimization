import connection
from utils import flush_cache

cursor = connection.cursor

flush_cache(cursor)

query = "SELECT * FROM tpch.orders WHERE O_ORDERKEY = 290 AND O_ORDERSTATUS = 'F'"
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
values = (2, 
    str(query), 
    str(results[0][0]), 
    str(results[1][0]), 
    str(results[2][0]), 
    str(results[3][0]), 
    None, 
    'original',
    None, 
    "Primary key (O_ORDERKEY) is always index as well, so optimizator will use it first when performing optimization, no matter where it's ordered in query.")

insert_into_statistics = cursor.execute(insert_query, values) 
connection.connection.commit()
