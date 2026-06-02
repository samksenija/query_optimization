import time

# Define the parameters for references
changes_applied = [None, "Change of filter column order"]
notes = [
    None,
    "How filter order when no primary key is used affects the execution.", 
    "Primary key (O_ORDERKEY) is always index as well, so optimizator will use it first when performing optimization, no matter where it's ordered in query."
]
layer_tags = ["original", "1st", "2nd"]


# In order to preform true benchmarking, we need to flush the cache before each test. 
# This is a simple function that does just that.
def flush_cache(cursor):
    cursor.execute("FLUSH TABLES;")
    cursor.execute("FLUSH STATUS;")
    
    print("Cache flushed successfully.")
    

# Even although this parameter can't be too relevant atm,
# It would be nice to see db execution time as captured parameter if needed to be referenced further
def query_execution_time(cursor, query):
    start_time = time.perf_counter()
    cursor.execute(query)
    cursor.fetchall()
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    
    return f"{execution_time:.6f} sec"


# When deciding which column has higher selectivity
def calculate_column_distinctiveness(column, table):
    distinctiveness  = "SELECT COUNT(DISTINCT " + column + ") / COUNT(*) FROM " + table + ";"
    
    return [table, column, distinctiveness]