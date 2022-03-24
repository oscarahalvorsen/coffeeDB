import sqlite3

def createTables(cursor: sqlite3.Cursor):
    createUserTable(cursor)
    createEmailTable(cursor)
    createReviewTable(cursor)
    createCoffeeTable(cursor)
    createRoasteryTable(cursor)
    createBatchTable(cursor)
    createBatchContainsBeanTable(cursor)
    createBeanTable(cursor)
    createBeanFromFarmTable(cursor)
    createFarmTable(cursor)
    createRegionTable(cursor)
    createRefiningMethodTable(cursor)

def createUserTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE User
    (
        UserID INTEGER PRIMARY KEY, 
        Password TEXT NOT NULL,
        FullName TEXT NOT NULL
    );
    ''')

def createEmailTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Email
    (
        UserID INTEGER PRIMARY KEY,
        Email TEXT NOT NULL UNIQUE
    );
    ''')

def createReviewTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Review 
    (
        UserID INTEGER REFERENCES User(UserID) ON DELETE SET NULL ON UPDATE CASCADE, 
        CoffeeID INTEGER REFERENCES Coffee(CoffeeID) ON DELETE CASCADE ON UPDATE CASCADE,
        Date TEXT NOT NULL,
        Note TEXT,
        Score INTEGER CHECK (SCORE >= 0 AND SCORE <= 10),
        PRIMARY KEY (UserID, CoffeeID)
    );
    ''')

def createCoffeeTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Coffee 
    (
        CoffeeID INTEGER PRIMARY KEY,
        CoffeeName TEXT,
        RoastingDegree TEXT NOT NULL CHECK (RoastingDegree = "light" OR RoastingDegree = "medium" or RoastingDegree = "dark"),
        RoastingDate TEXT NOT NULL,
        Description TEXT,
        PricePerKilo INTEGER CHECK (PricePerKilo > 0),
        BatchID INTEGER REFERENCES Batch(BatchID) ON DELETE SET NULL ON UPDATE CASCADE,
        RoasteryID INTEGER REFERENCES Roastery(RoasteryID) ON DELETE SET NULL ON UPDATE CASCADE
    );
    ''')

def createRoasteryTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Roastery 
    (
        RoasteryID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        RegionID INTEGER REFERENCES Region(RegionID) ON DELETE SET NULL ON UPDATE CASCADE
    );
    ''')

def createBatchTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Batch 
    (
        BatchID INTEGER PRIMARY KEY,
        HarvestYear INTEGER,
        PayPerKilo INTEGER CHECK (PayPerKilo > 0),
        MethodName INTEGER REFERENCES RefiningMethod(MethodName) ON DELETE SET NULL ON UPDATE CASCADE,
        FarmID INTEGER REFERENCES Farm(FarmID) ON DELETE SET NULL ON UPDATE CASCADE
    );
    ''')

def createBatchContainsBeanTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE BatchContainsBean
    (
        BatchID INTEGER REFERENCES Batch(BatchID) ON DELETE CASCADE ON UPDATE CASCADE,
        Species INTEGER REFERENCES Bean(Species) ON DELETE SET NULL ON UPDATE CASCADE,
        PRIMARY KEY (BatchID, Species)
    );
    ''')

def createBeanTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Bean 
    (
        Species TEXT PRIMARY KEY
    );
    ''')

def createBeanFromFarmTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE BeanFromFarm
    (
        Species INTEGER REFERENCES Bean(Species) ON DELETE SET NULL ON UPDATE CASCADE,
        FarmID INTEGER REFERENCES Farm(FarmID) ON DELETE CASCADE ON UPDATE CASCADE,
        PRIMARY KEY (Species, FarmID)
    );
    ''')

def createFarmTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Farm 
    (
        FarmID INTEGER PRIMARY KEY, 
        Elevation INTEGER,
        Name TEXT,
        RegionID INTEGER REFERENCES Region(RegionID) ON DELETE SET NULL ON UPDATE CASCADE
    );
    ''')

def createRegionTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE Region 
    (
        RegionID INTEGER PRIMARY KEY, 
        Name TEXT,
        Country TEXT
    );
    ''')

def createRefiningMethodTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE RefiningMethod 
    (
        MethodName TEXT PRIMARY KEY,
        Description TEXT
    );
    ''')