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
def calculate_column_distinctiveness(cursor, column, table):
    distinctiveness_query  = "SELECT COUNT(DISTINCT " + column + ") / COUNT(*) FROM " + table + ";"
    
    cursor.execute(distinctiveness_query)
    distinctiveness = cursor.fetchall()
    
    return [table, column, distinctiveness]


# Even altough this information isn't neccessarily too informative atm
# It is needed to reference which version of tpch was used
def number_of_rows_per_table(cursor, table):
    row_count_per_table_query = "SELECT COUNT(*) FROM " + table + ";"
    
    cursor.execute(row_count_per_table_query)
    row_count_per_table = cursor.fetchall()
    
    return [table, row_count_per_table]


# Empty table for testing purposes
def truncate_table(cursor, table):
    truncate_table_query = "TRUNCATE TABLE " + table + ";"
    
    cursor.execute(truncate_table_query)
    cursor.fetchall()
    
    print("Successfully emptied the table.")
    

# Select from STATISTICS table all rows & columns
def select_from_statitistic_table(cursor):
    select_from_statitistic_table_query = "SELECT * FROM STATISTICS"
    
    cursor.execure(select_from_statitistic_table_query)
    cursor.fetchall()