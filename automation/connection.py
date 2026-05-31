import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
import os

load_dotenv() 

try:
    connection = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )

    if connection.is_connected():
        cursor = connection.cursor()

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
