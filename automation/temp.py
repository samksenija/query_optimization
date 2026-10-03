# This is temporary variable & helper code contaner
# TODO Remove

import re

# TEST VALUES AND PARAMETERS
# Test queries for validation of RegEx
query = "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910 AND TEST = 15;"
query_multitable_join = "SELECT c.name, o.order_id, p.product_name, oi.quantity, p.price FROM customers c JOIN orders o ON c.customer_id = o.customer_id JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id;"
test_query = """
            SELECT MIN(chn.name) AS uncredited_voiced_character, MIN(t.title) AS russian_movie
            FROM char_name AS chn,
                cast_info AS ci,
                company_name AS cn,
                company_type AS ct,
                movie_companies AS mc,
                role_type AS rt,
                title AS t
            WHERE ci.note LIKE '%(voice)%'
            AND ci.note LIKE '%(uncredited)%'
            AND cn.country_code = '[ru]'
            AND rt.role = 'actor'
            AND t.production_year > 2005
            AND t.id = mc.movie_id
            AND t.id = ci.movie_id
            AND ci.movie_id = mc.movie_id
            AND chn.id = ci.person_role_id
            AND rt.id = ci.role_id
            AND cn.id = mc.company_id
            AND ct.id = mc.company_type_id
        """

# RegEx definitions, temporary
extract_column_names_first_step = re.findall('(?i)(where| and) (\w+)', query)
extract_main_table_name_first_step =  re.findall('(?i)FROM (\w+)', query)
extract_join_table_names_first_step = re.findall('(?i)JOIN (\w+)', query_multitable_join)
# ON (\w+.\w+ = \w+.\w+), join condition
# This join regex catches aliases JOIN (\w+) (\w+), if an alias has been asigned to join
# Catch filter column values /(?i) (\w+) = ([A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+)
# JOIN conditions (\w+.\w+ = \w+.\w+)
# ALL filters ([(^AND)(\w.+)]+) ([=><]) ([A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+)
# LIKEs ([(^WHERE)(\w.+)]+) LIKE ([A-Za-z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+)
# ALL the tables between FROM and WHERE (?is)\bFROM\b(.*?)\bWHERE\b


# What data currently looks like (un)processed

# tables = tables[0].split(",") 
# [' char_name AS chn', '\n                cast_info AS ci', '\n                company_name AS cn',
#  '\n                company_type AS ct', '\n                movie_companies AS mc', '\n                role_type AS rt',
#  '\n                title AS t\n            ']


# table_name = table.split() 
# ['title', 'AS', 't']

# table_information
# [
# {'name': 'char_name', 
#   'alias': 'chn', 
#   'filter': []
#  }, 
# {'name': 'cast_info', 
#   'alias': 'ci', 
#   'filter': []
#   }, 
# {'name': 'company_name', 
#   'alias': 'cn', 
#   'filter': [('cn.country_code', '=', "'[ru]'")]
#   }, 
# {'name': 'company_type', 
#   'alias': 'ct', 
#   'filter': []
#   }, 
# {'name': 'movie_companies', 
#   'alias': 'mc', 
#   'filter': []
#   }, 
# {'name': 'role_type', 
#   'alias': 'rt', 
#   'filter': [('rt.role', '=', "'actor'")]
#   }, 
# {'name': 'title',     
#   'alias': 't', 
#   'filter': [('t.production_year', '>', '2005')]
#    }
# ]