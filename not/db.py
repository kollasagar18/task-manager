import mysql.connector
import os

def db_con():

    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST", "localhost"),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", "Kollasagar@93"),
        database=os.getenv("MYSQLDATABASE", "railway"),
        port=os.getenv("MYSQLPORT", "3306")
    )