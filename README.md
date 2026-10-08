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

-------

Database name must be added in .env.

------

Packages:

`pip install networkx`

`pip install pygraphviz`

`pip install matplotlib`

`pip install graphviz`

---------

Installations:

Graphviz: https://graphviz.org/download/

--------
## Overview

#### `directed_graph_dynamically.py`

- In JOINS we have the tables from 'both sides' of the equality operator
- In order to create a meaningful graph structure, the number of table occurences is counted this sum determines the side that will contain the root node, in this case the node that would have most edges to other nodes, and this sum is crucial factor in the root node choice
- Since JOIN creation does not have to follow a predetermined structure of how many and which tables will be joined, such a presumption had to be made in order to setup the structure that could come close to optimal one, as main point was to enable graph traversal
- Tables are 'chained' to one another depending, of course, to their logic in the original query, and should there be a duplicate, the one closest to the root & already processed is preserved
