from os import curdir
import sqlite3
import create_tables

def create_database(name: str):

    try:
        con = sqlite3.connect(name)
        con.execute("PRAGMA foreign_keys = 1")
        cursor = con.cursor()
        create_tables.createTables(cursor)
        con.commit()
        return con, cursor

    except Exception as e:
        print(e)

    return con, cursor

def close_database(con: sqlite3.Connection):
    con.close()


def add_user(con: sqlite3.Connection, cursor: sqlite3.Cursor, password: str, full_name: str, email: str):
    try:
        cursor.execute('''INSERT INTO Email (Email) VALUES (?);''', (email,))
    except Exception as e:
        print("Could not insert into Email table")
        return(e)
    try:
        cursor.execute('''SELECT UserID from Email WHERE Email == ?''', (email,))
        user_ID = cursor.fetchone()
        cursor.execute('''INSERT INTO User (UserID, Password, Fullname) VALUES (?, ?, ?)''', (user_ID[0], password, full_name))
        con.commit()
    except Exception as e:
        print("Could not insert into User table")
        return(e)
    return 1


def add_review(con: sqlite3.Connection, cursor: sqlite3.Cursor, user_ID: int, coffee_ID: int, date: str, 
                note: str, score: int):
    try:
        cursor.execute('''INSERT INTO Review (UserID, CoffeeID, Date, Note, Score) 
        VALUES (?, ?, ?, ?, ?);''', (user_ID, coffee_ID, date, note, score))
        con.commit()
    except Exception as e:
        print("Could not insert into Coffee table")
        return(e)
    return 1


def add_coffee(con: sqlite3.Connection, cursor: sqlite3.Cursor, name: str, roasting_degree: str, roasting_date: str, 
                description: str, price_per_kilo: int, batch_ID: int, roastery_ID):
    try:
        cursor.execute('''INSERT INTO Coffee (CoffeeName, RoastingDegree, RoastingDate, Description, PricePerKilo, BatchID, RoasteryID) 
        VALUES (?, ?, ?, ?, ?, ?, ?);''', (name, roasting_degree, roasting_date, description, price_per_kilo, batch_ID, roastery_ID))
        con.commit()
    except Exception as e:
        print("Could not insert into Coffee table")
        return(e)
    return 1

def add_roastery(con: sqlite3.Connection, cursor: sqlite3.Cursor, name: str, region_ID: int):
    try:
        cursor.execute('''INSERT INTO Roastery (Name, RegionID) 
        VALUES (?, ?);''', (name, region_ID))
        con.commit()
    except Exception as e:
        print("Could not insert into Coffee table")
        return(e)
    return 1

def add_batch(con: sqlite3.Connection, cursor: sqlite3.Cursor, harvest_year: int, pay_per_kilo: int, method_name: str, farm_ID: int):
    try:
        cursor.execute('''INSERT INTO Batch (HarvestYear, PayPerKilo, MethodName, FarmID) 
        VALUES (?, ?, ?, ?);''', (harvest_year, pay_per_kilo, method_name, farm_ID))
        con.commit()
    except Exception as e:
        print("Could not insert into Batch table")
        return(e)
    return 1

def add_batch_contains_bean(con: sqlite3.Connection, cursor: sqlite3.Cursor, batch_ID: int, species: str):
    try:
        cursor.execute('''INSERT INTO BatchContainsBean (BatchID, Species) 
        VALUES (?, ?);''', (batch_ID, species))
        con.commit()
    except Exception as e:
        print("Could not insert into BatchContainsBean table")
        return(e)
    return 1
    
def add_bean(con: sqlite3.Connection, cursor: sqlite3.Cursor, bean: str):
    try:
        cursor.execute('''INSERT INTO Bean (Species) 
        VALUES (?);''', [bean])
        con.commit()
    except Exception as e:
        print("Could not insert into Bean table")
        return(e)
    return 1

def add_bean_from_farm(con: sqlite3.Connection, cursor: sqlite3.Cursor, species: str, farm_ID: int):
    try:
        cursor.execute('''INSERT INTO BeanFromFarm(Species, FarmID)
        VALUES (?, ?);''', (species, farm_ID))
        con.commit()
    except Exception as e:
        print("Could not insert into BeanFromFarm table")
        return(e)
    return 1

def add_farm(con: sqlite3.Connection, cursor: sqlite3.Cursor, elevation: int, name: str, region_ID: int):
    try:
        cursor.execute('''INSERT INTO Farm(Elevation, Name, RegionID)
        VALUES (?, ?, ?);''', (elevation, name, region_ID))
        con.commit()
    except Exception as e:
        print("Could not insert into Farm table")
        return(e)
    return 1

def add_region(con: sqlite3.Connection, cursor: sqlite3.Cursor, name: str, country: str):
    try:
        cursor.execute('''INSERT INTO Region(Name, Country)
        VALUES (?, ?);''', (name, country))
        con.commit()
    except Exception as e:
        print("Could not insert into Region table")
        return(e)
    return 1

def add_refining_method(con: sqlite3.Connection, cursor: sqlite3.Cursor, method_name: str, desc: str):
    try:
        cursor.execute('''INSERT INTO RefiningMethod(MethodName, Description)
        VALUES (?, ?);''', (method_name, desc))
        con.commit()
    except Exception as e:
        print("Could not insert into RefiningMethod table")
        return(e)
    return 1


def get_all_from_table(cursor: sqlite3.Cursor, table: str):
    return cursor.execute("SELECT * FROM %s" % (table)).fetchall()


if __name__ == "__main__":
    con, cursor = create_database("test.db")
    # add_user(con, cursor, "123", "Ola Nordmann", "ola@nordmann.no")
    # add_region(con, cursor, "Santa Ana", "El Salvador")
    regions = get_all_from_table(cursor, "Region")
    my_region = [x for x in regions if x[1] == "Santa Ana" and x[2] == "El Salvador"][0]
    my_region_id = my_region[0]
    # add_farm(con, cursor, 1500, "Nombre de Dios", my_region_id)
    # add_bean(con, cursor, "Natural Bourbon")
    # add_bean_from_farm(con, cursor, "Natural Bourbon", 1)
    # add_refining_method(con, cursor, "washed", "rinse the beans in cold water for 20 minutes")
    # add_batch(con ,cursor, 2021, 8, "washed", 1)
    # add_batch_contains_bean(con, cursor, 1, "Natural Bourbon")
    # add_region(con, cursor, "Trondheim", "Norge")
    # add_roastery(con, cursor, "Jacobsen & Svart", 2)
    add_coffee(con, cursor, "Vinterkaffe 2022", "light", "20.01.2022", 
    "A tasty and complex coffee for polar nights", 600, 1, 1)
    
