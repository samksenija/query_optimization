from query_performance_capture import query_execution_capture

query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;"
identifier = 1
layer_tag = 'original'
change_applied = None
note = None

query_execution_capture(query, identifier, layer_tag, change_applied, note)