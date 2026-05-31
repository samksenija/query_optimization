# query_optimization
Query Optimization
<br/>
<br/>
In MySQL 8, the FLUSH STATUS statement resets most runtime status variables to zero, folding active session metrics into global counters. It is primarily used by database administrators to clear metrics before benchmarking or running specific performance tests.
```
FLUSH TABLES;
FLUSH STATUS;
```
