from query_performance_capture import query_execution_capture
from queries import queries

for main_key, items in queries.items():
    query = items["query"]
    identifier = int(main_key[0])
    layer_tag = items["layer_tag"]
    change_applied = items["change_applied"]
    note = items["note"]
    
    query_execution_capture(query, identifier, layer_tag, change_applied, note)
