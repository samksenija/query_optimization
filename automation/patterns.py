# Here column names are extracted in order for further processing to occur
import re

query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910 AND TEST = 15;"

extract_column_names_first_step = re.findall('([(AND )]|[(where )]|[(WHERE )]|[(and )]|[(\s)])(\w+)( =)', query)

column_names = []

# Here just column names are extracted without the other additional matthes
def extract_column_names(extract_column_names_first_step):
    for result in extract_column_names_first_step:
        column_names.append(result[1])
        
    print(column_names)
  
extract_column_names(extract_column_names_first_step)



