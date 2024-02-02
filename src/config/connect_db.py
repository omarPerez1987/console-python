import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()


sql_host = os.getenv("SQL_HOST")
sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")
sql_database = os.getenv("SQL_DATABASE")
sql_port = os.getenv("SQL_PORT")


def connect():
    try:
        connection = mysql.connector.connect(
            host=sql_host,
            user=sql_user,
            database=sql_database,
            password=sql_password
        )

        if connection.is_connected():
            print('Conexión exitosa a MySQL')
            return connection

    except Error as e:
        print(f'Error: {e}')
