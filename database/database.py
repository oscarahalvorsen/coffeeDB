from os import curdir
import sqlite3
import setupDatabase

def create_database(name: str):
    con, cursor = setupDatabase.createDatabase(name)

    try:
        setupDatabase.createTables(cursor)
    except Exception as e:
        print(e)

    return con, cursor

def close_database(con: sqlite3.Connection):
    con.close()

def add_coffee(name: str, roasting_degree: str, roasting_date: str, 
    description: str, price_per_kilo: int, batch_ID: int, roastery_ID: int):
    cursor.execute(f"INSERT INTO Coffee (CoffeeName, RoastingDegree, RoastingDate, Description, PricePerKilo, BatchID, RoasteryID) VALUES ({name}, {roasting_degree}, {roasting_date}, {description}, {price_per_kilo}, {batch_ID}, {roastery_ID})")

def get_all_coffees(cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM COFFEE")

if __name__ == "__main__":
    con, cursor = create_database("test.db")
    get_all_coffees(cursor)
