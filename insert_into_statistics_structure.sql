INSERT INTO STATISTICS (id, executed_query, explain_query, explain_json, explain_tree, explain_analyze, duration, layer_tag, change_applied)
VALUES (
,
"",
"",
"",
"",
"",
"",
"",
""
);

#EXAMPLES
INSERT INTO STATISTICS (id, executed_query, explain_query, explain_json, explain_tree, explain_analyze, duration, layer_tag, change_applied)
VALUES (
1,
"SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;",
"# id, select_type, table, partitions, type, possible_keys, key, key_len, ref, rows, filtered, Extra
'1', 'SIMPLE', 'orders', NULL, 'ALL', NULL, NULL, NULL, NULL, '1486760', '1.00', 'Using where'",
"'{\n  \"query_block\": {\n    \"select_id\": 1,\n    \"cost_info\": {\n      \"query_cost\": \"155991.06\"\n    },\n    \"table\": {\n      \"table_name\": \"orders\",\n      \"access_type\": \"ALL\",\n      \"rows_examined_per_scan\": 1486760,\n      \"rows_produced_per_join\": 14867,\n      \"filtered\": \"1.00\",\n      \"cost_info\": {\n        \"read_cost\": \"154504.30\",\n        \"eval_cost\": \"1486.76\",\n        \"prefix_cost\": \"155991.06\",\n        \"data_read_per_join\": \"6M\"\n      },\n      \"used_columns\": [\n        \"O_ORDERKEY\",\n        \"O_CUSTKEY\",\n        \"O_ORDERSTATUS\",\n        \"O_TOTALPRICE\",\n        \"O_ORDERDATE\",\n        \"O_ORDERPRIORITY\",\n        \"O_CLERK\",\n        \"O_SHIPPRIORITY\",\n        \"O_COMMENT\"\n      ],\n      \"attached_condition\": \"((`tpch`.`orders`.`O_CUSTKEY` = 1910) and (`tpch`.`orders`.`O_ORDERPRIORITY` = \'5-LOW\'))\"\n    }\n  }\n}'",
"'-> Filter: ((orders.O_CUSTKEY = 1910) and (orders.O_ORDERPRIORITY = \'5-LOW\'))  (cost=155991 rows=14868) (actual time=4502..11650 rows=1 loops=1)\n    -> Table scan on orders  (cost=155991 rows=1.49e+6) (actual time=26.8..11434 rows=1.5e+6 loops=1)\n'",
"-> Filter: ((orders.O_CUSTKEY = 1910) and (orders.O_ORDERPRIORITY = ''5-LOW''))  (cost=156835 rows=14868) (actual time=1725..7085 rows=1 loops=1)
    -> Table scan on orders  (cost=156835 rows=1.49e+6) (actual time=2.19..6807 rows=1.5e+6 loops=1)",
"9.016 sec / 0.000 sec",
"original",
NULL
);

INSERT INTO STATISTICS (id, executed_query, explain_query, explain_json, explain_tree, explain_analyze, duration, layer_tag, change_applied)
VALUES (
1,
"SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';",
"# id, select_type, table, partitions, type, possible_keys, key, key_len, ref, rows, filtered, Extra
'1', 'SIMPLE', 'orders', NULL, 'ALL', NULL, NULL, NULL, NULL, '1486760', '1.00', 'Using where'",
"'{\n  \"query_block\": {\n    \"select_id\": 1,\n    \"cost_info\": {\n      \"query_cost\": \"155192.60\"\n    },\n    \"table\": {\n      \"table_name\": \"orders\",\n      \"access_type\": \"ALL\",\n      \"rows_examined_per_scan\": 1486760,\n      \"rows_produced_per_join\": 14867,\n      \"filtered\": \"1.00\",\n      \"cost_info\": {\n        \"read_cost\": \"153705.84\",\n        \"eval_cost\": \"1486.76\",\n        \"prefix_cost\": \"155192.60\",\n        \"data_read_per_join\": \"6M\"\n      },\n      \"used_columns\": [\n        \"O_ORDERKEY\",\n        \"O_CUSTKEY\",\n        \"O_ORDERSTATUS\",\n        \"O_TOTALPRICE\",\n        \"O_ORDERDATE\",\n        \"O_ORDERPRIORITY\",\n        \"O_CLERK\",\n        \"O_SHIPPRIORITY\",\n        \"O_COMMENT\"\n      ],\n      \"attached_condition\": \"((`tpch`.`orders`.`O_ORDERPRIORITY` = \'5-LOW\') and (`tpch`.`orders`.`O_CUSTKEY` = 1910))\"\n    }\n  }\n}'",
"'-> Filter: ((orders.O_ORDERPRIORITY = \'5-LOW\') and (orders.O_CUSTKEY = 1910))  (cost=155193 rows=14868)\n    -> Table scan on orders  (cost=155193 rows=1.49e+6)\n'",
"'-> Filter: ((orders.O_ORDERPRIORITY = \'5-LOW\') and (orders.O_CUSTKEY = 1910))  (cost=156376 rows=14868) (actual time=1360..6997 rows=1 loops=1)\n    -> Table scan on orders  (cost=156376 rows=1.49e+6) (actual time=15.3..6498 rows=1.5e+6 loops=1)\n'",
"10.235 sec / 0.000 sec",
"1st",
"Change of filter column order"
);

SELECT * FROM STATISTICS;

#Testing out formats, old needs to be dropped
TRUNCATE STATISTICS;

#Alterations
ALTER TABLE STATISTICS RENAME COLUMN cost TO duration;
ALTER TABLE STATISTICS RENAME COLUMN execution_plan TO explain_analyze;
ALTER TABLE STATISTICS 
ADD COLUMN explain_query TEXT, 
ADD COLUMN explain_json TEXT, 
ADD COLUMN explain_tree TEXT; 
