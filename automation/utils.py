# In order to preform true benchmarking, we need to flush the cache before each test. 
# This is a simple function that does just that.
def flush_cache(cursor):
    cursor.execute("FLUSH TABLES;")
    cursor.execute("FLUSH STATUS;")
    
    print("Cache flushed successfully.")