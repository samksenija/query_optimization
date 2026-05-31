INSERT INTO STATISTICS (id, executed_query, execution_plan, duration, layer_tag, change_applied)
VALUES (
,
"",
"",
"",
"",
""
);

#EXAMPLES
INSERT INTO STATISTICS (id, executed_query, execution_plan, duration, layer_tag, change_applied)
VALUES (
1,
"SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;",
"-> Filter: ((orders.O_CUSTKEY = 1910) and (orders.O_ORDERPRIORITY = ''5-LOW''))  (cost=156835 rows=14868) (actual time=1725..7085 rows=1 loops=1)
    -> Table scan on orders  (cost=156835 rows=1.49e+6) (actual time=2.19..6807 rows=1.5e+6 loops=1)",
"9.016 sec / 0.000 sec",
"original",
NULL
);

INSERT INTO STATISTICS (id, executed_query, execution_plan, duation, layer_tag, change_applied)
VALUES (
1,
"SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';",
"'-> Filter: ((orders.O_ORDERPRIORITY = \'5-LOW\') and (orders.O_CUSTKEY = 1910))  (cost=156376 rows=14868) (actual time=1360..6997 rows=1 loops=1)\n    -> Table scan on orders  (cost=156376 rows=1.49e+6) (actual time=15.3..6498 rows=1.5e+6 loops=1)\n'",
"10.235 sec / 0.000 sec",
"1st",
"Change of filter column order"
);

SELECT * FROM STATISTICS;

ALTER TABLE STATISTICS RENAME COLUMN cost TO duration;
