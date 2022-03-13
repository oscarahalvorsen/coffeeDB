import sqlite3
import setupDatabase

con, cursor = setupDatabase.createDatabase("test2.db")

try:
    setupDatabase.createTables(cursor)
except Exception as e:
    print(e)

con.close()
