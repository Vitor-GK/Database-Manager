import mysql.connector
import time
import datetime
from decimal import Decimal
import sys
from db_function import *

choice = None
sub_choice = None

host = None
user = None
password = None
db_name = None
invalid_digits = " @#$%&*"


try:
    print("////////////////////////////////////////This is the DataBase Manager!////////////////////////////////////////\n")
    print("Connect to the Database:\n")

    host = input("Enter host (default: localhost): ") or "localhost"
    user = input("Enter user (default: root): ") or "root"
    password = input("Enter password (default: empty): ") or ""
    db_name = input("Enter database name (default: test): ") or "test"
except mysql.connector.Error as error:
    print(f"Error conecting to database: {error}")

conn = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)

cursor = conn.cursor()

while True:
    Menu(cursor, conn)

cursor.close()
conn.close()