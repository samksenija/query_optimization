import re

query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910 AND TEST = 15;"

extract_column_names_first_step = re.findall('((AND )|(where )|(WHERE )|(and ))(\w+)( =)', query)
print(extract_column_names_first_step)


