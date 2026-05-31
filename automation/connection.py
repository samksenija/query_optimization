import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
import os

load_dotenv() 

try:
    # 1. Establish the connection to the database
    connection = mysql.connector.connect(
        host=os.getenv("host"), # Your database host IP or domain
        user=os.getenv("user"), # Your MySQL database username
        password=os.getenv("password"), # Your MySQL database password
        database=os.getenv("database") # The name of your database
    )

    if connection.is_connected():
        print("Successfully connected to MySQL database")
        
        # 2. Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        
        # 3. Execute a sample query
        cursor.execute("SELECT DATABASE();")
        
        # 4. Fetch and print the result
        record = cursor.fetchone()
        print(f"You are connected to database: {record[0]}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 5. Safely close the cursor and connection blocks
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
