# query_optimization
### Query Optimization
Capture query performance metrics and diagnostics, including the executed query, EXPLAIN output, EXPLAIN JSON, EXPLAIN ANALYZE results, execution duration, and other relevant parameters. These provide visibility into the query execution plan, helping to assess current performance and identify opportunities for optimization and selection of the most efficient execution plan.

Extracting table & column information from executed query, calculating distinctiveness, number of rows, with steps forward to understanding selected indexes when executing query plan.

Defining the structure for query processing & evaluation. 
<br/>
<br/>
### Setting the test environment
In MySQL 8, the FLUSH STATUS statement resets most runtime status variables to zero, folding active session metrics into global counters. It is primarily used by database administrators to clear metrics before benchmarking or running specific performance tests.
```
FLUSH TABLES;
FLUSH STATUS;
```
<br/>
If you want to measure the true "cold" execution speed of a query without any caching help, apply these temporary aggressive flushing parameters (my.ini):

```
[mysqld]
innodb_old_blocks_pct = 5
innodb_max_dirty_pages_pct = 0
```
