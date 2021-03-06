/* Coffee database, Oskar Jorgensen and Oscar Halvorsen */

BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "User" (
	"UserID"	INTEGER,
	"Password"	TEXT NOT NULL,
	"FullName"	TEXT NOT NULL,
	PRIMARY KEY("UserID")
);
CREATE TABLE IF NOT EXISTS "Email" (
	"UserID"	INTEGER,
	"Email"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("UserID")
);
CREATE TABLE IF NOT EXISTS "Review" (
	"UserID"	INTEGER,
	"CoffeeID"	INTEGER,
	"Date"	DATE NOT NULL,
	"Note"	TEXT,
	"Score"	INTEGER CHECK("SCORE" >= 0 AND "SCORE" <= 10),
	FOREIGN KEY("UserID") REFERENCES "User"("UserID") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("CoffeeID") REFERENCES "Coffee"("CoffeeID") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("UserID","CoffeeID")
);
CREATE TABLE IF NOT EXISTS "Coffee" (
	"CoffeeID"	INTEGER,
	"CoffeeName"	TEXT,
	"RoastingDegree"	TEXT NOT NULL CHECK("RoastingDegree" = "light" OR "RoastingDegree" = "medium" OR "RoastingDegree" = "dark"),
	"RoastingDate"	DATE NOT NULL,
	"Description"	TEXT,
	"PricePerKilo"	INTEGER CHECK("PricePerKilo" > 0),
	"BatchID"	INTEGER,
	"RoasteryID"	INTEGER,
	FOREIGN KEY("RoasteryID") REFERENCES "Roastery"("RoasteryID") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("BatchID") REFERENCES "Batch"("BatchID") ON DELETE SET NULL ON UPDATE CASCADE,
	PRIMARY KEY("CoffeeID")
);
CREATE TABLE IF NOT EXISTS "Roastery" (
	"RoasteryID"	INTEGER,
	"Name"	TEXT NOT NULL,
	"RegionID"	INTEGER,
	FOREIGN KEY("RegionID") REFERENCES "Region"("RegionID") ON DELETE SET NULL ON UPDATE CASCADE,
	PRIMARY KEY("RoasteryID")
);
CREATE TABLE IF NOT EXISTS "Batch" (
	"BatchID"	INTEGER,
	"HarvestYear"	INTEGER,
	"PayPerKilo"	INTEGER CHECK("PayPerKilo" > 0),
	"MethodName"	INTEGER,
	"FarmID"	INTEGER,
	FOREIGN KEY("FarmID") REFERENCES "Farm"("FarmID") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("MethodName") REFERENCES "RefiningMethod"("MethodName") ON DELETE SET NULL ON UPDATE CASCADE,
	PRIMARY KEY("BatchID")
);
CREATE TABLE IF NOT EXISTS "BatchContainsBean" (
	"BatchID"	INTEGER,
	"Species"	INTEGER,
	FOREIGN KEY("Species") REFERENCES "Bean"("Species") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("BatchID") REFERENCES "Batch"("BatchID") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("BatchID","Species")
);
CREATE TABLE IF NOT EXISTS "Bean" (
	"Species"	TEXT,
	PRIMARY KEY("Species")
);
CREATE TABLE IF NOT EXISTS "BeanFromFarm" (
	"Species"	INTEGER,
	"FarmID"	INTEGER,
	FOREIGN KEY("Species") REFERENCES "Bean"("Species") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("FarmID") REFERENCES "Farm"("FarmID") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("Species","FarmID")
);
CREATE TABLE IF NOT EXISTS "Farm" (
	"FarmID"	INTEGER,
	"Elevation"	INTEGER,
	"Name"	TEXT,
	"RegionID"	INTEGER,
	FOREIGN KEY("RegionID") REFERENCES "Region"("RegionID") ON DELETE SET NULL ON UPDATE CASCADE,
	PRIMARY KEY("FarmID")
);
CREATE TABLE IF NOT EXISTS "Region" (
	"RegionID"	INTEGER,
	"Name"	TEXT,
	"Country"	TEXT,
	PRIMARY KEY("RegionID")
);
CREATE TABLE IF NOT EXISTS "RefiningMethod" (
	"MethodName"	TEXT,
	"Description"	TEXT,
	PRIMARY KEY("MethodName")
);
COMMIT;
