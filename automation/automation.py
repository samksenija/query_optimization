import connection
from utils import flush_cache

cursor = connection.cursor

flush_cache(cursor)

