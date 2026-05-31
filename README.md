# query_optimization
Query Optimization
<br/>
<br/>
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
