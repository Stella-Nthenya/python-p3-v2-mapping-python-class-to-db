# lib/config.py
import sqlite3
#establish connection to the SQlite db file i.e. company.db. connect is what establishes the connection
#CONN variable is assigned the connection object returned by sqlite3.connect(). 

CONN = sqlite3.connect('company.db')
#The CONN variable now holds the connection to the SQLite database, allowing you to interact with it using Python.
#.cursor method allows us to execute SQL commands and retrieve data from db
# This line assigns the cursor object returned by CONN.cursor() to the variable CURSOR.
CURSOR = CONN.cursor()