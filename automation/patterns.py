# Here column names are extracted in order for further processing to occur
import re

column_names = []
table_names= []

query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910 AND TEST = 15;"

extract_column_names_first_step = re.findall('([(AND )]|[(where )]|[(WHERE )]|[(and )]|[(\s)])(\w+)( =)', query)
extract_main_table_name_first_step =  re.findall('FROM (\w+)', query)

# Here just column names are extracted without the other additional matthes
def extract_column_names(extract_column_names_first_step):
    for result in extract_column_names_first_step:
        column_names.append(result[1])
        
    print(column_names)
  
extract_column_names(extract_column_names_first_step)

#Extract main table name
def extraxt_main_table_name(extract_main_table_name_first_step):
    for result in extract_main_table_name_first_step:
        table_names.append(result)

    print(table_names)
    
extraxt_main_table_name(extract_main_table_name_first_step)


