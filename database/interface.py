import sqlite3
from datetime import date

from database import create_database

def main():
    choice = get_choice()
    if(choice == "v"):
        # View coffees
        print("Viewing")
    elif(choice == "r"):
        # Review a coffee
        print("Reviewing")

def get_choice():
    choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    while(choice != "v" and choice != "r"):
        print("Choice must be 'v' or 'r'")
        choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    return choice

def reviewCoffee():
    coffee_name = input("What is the name of the coffee you wish to review? ")

def user_stories():
    user_story = int(input("What user story would you like to see [1-5]? "))
    while(user_story < 1 or user_story > 5):
        user_story = int(input("What user story would you like to see [1-5]? "))
    execute_story(user_story)

def execute_story(story: int):
    create_database("my.db")
    match story:
        case 1:
            user_story_1()
        case 2:
            user_story_2()
        case 3:
            user_story_3()
        case 4:
            user_story_4()
        case 5:
            user_story_5()

def user_story_1(cursor: sqlite3.Cursor):
    user_list = cursor.execute('''
    SELECT Email.Email, User.Password, User.UserID FROM User NATURAL JOIN Email;
    ''').fetchall()
    choice = input("Please [l]ogin or [r]egister: ")
    while(choice != "l" and choice != "r"):
        print("Wrong input")
        choice = input("Please [l]ogin or [r]egister: ")
    if choice == "l":
        print("Please login")
        mail = input("Email: ")
        while(mail not in [x[0] for x in user_list] and mail != "q"):
            print("Wrong email! Please try again or quit using [q]")
            mail = input("Email: ")
            if(mail == "q"):
                return 0
        pword = ""
        user_ID = -1
        for user in user_list:
            if(user[0] == mail):
                pword = user[1]
                user_ID = user[2]
        user_pword = input("Password: ")
        while(user_pword not in [x[1] for x in user_list] and user_pword != "q"):
            print("Wrong password! Please try again or quit using [q]")
            user_pword = input("Password: ")
            if(user_pword == "q"):
                return 0
        print("Login successful!")



def user_story_2(cursor: sqlite3.Cursor) -> None:
    year = date.today().year
    user_coffee_tasted = cursor.execute('''
    SELECT User.FullName, count(*) as CoffeesTasted 
    FROM User NATURAL JOIN Review NATURAL JOIN Coffee 
    WHERE Review.Date LIKE "%''' + str(year) + 
    '''" GROUP BY User.UserID 
    ORDER BY CoffeesTasted DESC;
    ''').fetchall()

    print("\nCoffees tasted | User")
    print("---------------|-----------------")
    for user_coffee in user_coffee_tasted:
        print(str(user_coffee[1]) + " " * (15 - len(str(user_coffee[1]))) + "| " + user_coffee[0])
    print()


def user_story_3(cursor: sqlite3.Cursor) -> None:
    coffee_value = cursor.execute('''
    SELECT Coffee.CoffeeName, AVG(Review.Score) AS AverageReview, Coffee.PricePerKilo, Roastery.Name 
    FROM Coffee JOIN Review on Coffee.CoffeeID == Review.CoffeeID JOIN Roastery ON Coffee.RoasteryID == Roastery.RoasteryID 
    GROUP BY Coffee.CoffeeID 
    ORDER BY AverageReview DESC;
    ''').fetchall()

    print("\n Avg. Score | Name of the Coffee | Price | Roastery")
    print("------------|--------------------|-------|--------------")
    for value in coffee_value:
        print(str(value[1]) + " " * (12 - len(str(value[1]))) + "| " + value[0] + " " * (19 - len(str(value[0]))) + "| " + str(value[2]) + " " * (6 - len(str(value[2]))) + "| " + value[3])
    print()


def user_story_4(cursor: sqlite3.Cursor) -> None:
    coffee_floral = cursor.execute('''
    SELECT Roastery.Name, Coffee.CoffeeName 
    FROM Coffee NATURAL JOIN Roastery JOIN Review ON Coffee.CoffeeID == Review.CoffeeID 
    WHERE Review.Note LIKE '%a%' OR Coffee.Description LIKE '%a%'
    GROUP BY Coffee.CoffeeID;
    ''').fetchall()

    print("\nRoastery            | Coffee")
    print("--------------------|----------------")
    for value in coffee_floral:
        print(str(value[0]) + " " * (20 - len(str(value[0]))) + "| " + value[1])
    print()


def user_story_5(cursor: sqlite3.Cursor):
    coffee_not_washed = cursor.execute(
    '''
    SELECT Roastery.Name, Coffee.CoffeeName 
    FROM Coffee 
    NATURAL JOIN Roastery JOIN Batch ON Coffee.BatchID == Batch.BatchID JOIN Farm ON Batch.FarmID == Farm.FarmID 
    JOIN Region ON Farm.RegionID == Region.RegionID  
    WHERE Batch.MethodName NOT LIKE "washed" AND Region.Country == "Colombia" OR Region.Country == "Rwanda";
    ''').fetchall()

    print("\nRoastery            | Coffee")
    print("--------------------|----------------")
    for value in coffee_not_washed:
        print(str(value[0]) + " " * (20 - len(str(value[0]))) + "| " + value[1])
    print()


if __name__ == "__main__":
    con, cursor = create_database("test.db")
    user_story_1(cursor)