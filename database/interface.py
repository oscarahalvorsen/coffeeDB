import sqlite3
from datetime import date, datetime

from database import create_database, add_review, add_user


def get_choice():
    choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    while(choice != "v" and choice != "r"):
        print("Choice must be 'v' or 'r'")
        choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    return choice


def user_stories(con: sqlite3.Connection, cursor: sqlite3.Cursor):
    user_story = int(input("What user story would you like to see [1-5]? "))
    while(user_story < 1 or user_story > 5):
        user_story = int(input("What user story would you like to see [1-5]? "))
    execute_story(user_story, cursor, con)

def execute_story(story: int, cursor: sqlite3.Cursor, con: sqlite3.Connection):
    create_database("my.db")
    match story:
        case 1:
            print("This story allows you to leave a review for an existing coffee\n")
            user_story_1(cursor, con)
        case 2:
            print("This story shows which users have tasted the most coffees this year\n")
            user_story_2(cursor)
        case 3:
            print("This story shows the coffees with the highest rating per price\n")
            user_story_3(cursor)
        case 4:
            print("This story shows the coffees which have been describes as floral, either by users or the roastery\n")
            user_story_4(cursor)
        case 5:
            print("This story shows coffees with beans from Rwanda or Colombia, that have not been washed")
            user_story_5(cursor)

def user_story_1(con: sqlite3.Connection, cursor: sqlite3.Cursor):
    user_list = cursor.execute('''
    SELECT Email.Email, User.Password, User.UserID FROM User NATURAL JOIN Email;
    ''').fetchall()
    choice = input("Please [l]ogin or [r]egister: ")
    while(choice != "l" and choice != "r"):
        print("Wrong input")
        choice = input("Please [l]ogin or [r]egister: ")
    user_ID = -1
    if choice == "r":
        print("Please register")
        full_name = input("Name: ")
        mail = input("Email: ")
        pword = input("Password: ")
        user_ID = add_user(con, cursor, pword, full_name, mail)[0]
        print(user_ID)
    if choice == "l":
        print("Please login")
        mail = input("Email: ")
        while(mail not in [x[0] for x in user_list] and mail != "q"):
            print("Wrong email! Please try again or quit using [q]")
            mail = input("Email: ")
            if(mail == "q"):
                return 0
        for user in user_list:
            if(user[0] == mail):
                user_ID = user[2]
                print(user_ID)
        user_pword = input("Password: ")
        while(user_pword not in [x[1] for x in user_list] and user_pword != "q"):
            print("Wrong password! Please try again or quit using [q]")
            user_pword = input("Password: ")
            if(user_pword == "q"):
                return 0
        print("Login successful!")
    review_choice = input("Would you like to leave a [r]eview or [q]uit? ")
    if(review_choice == "q"):
        return 0
    while(review_choice != "r" and review_choice != "q"):
        if(review_choice == "q"):
            return 0
        print("Wrong input")
        review_choice = input("Would you like to leave a [r]eview or [q]uit? ")
    coffee_name = input("What is the name of the coffee (leave empty to show all)? ")
    coffees = cursor.execute('''
    SELECT Coffee.CoffeeName, Roastery.Name, Coffee.RoastingDate, Coffee.CoffeeID 
    FROM Coffee NATURAL JOIN Roastery 
    WHERE Coffee.CoffeeName LIKE '%''' + coffee_name + '''%'
    ''').fetchall()
    if(len(coffees) == 0):
        print("No coffees matched your search.")
        return 0
    print()
    for i in range(len(coffees)):
        print(f"[{i+1}] {coffees[i][0]}(roasted {coffees[i][2]}) by {coffees[i][1]}")
    print()
    coffee_choice = input(f"Select using a number (1-{len(coffees)}): ")
    coffee_choice = coffees[int(coffee_choice) - 1]
    note = input("Write what you thought about the coffee: ")
    score = input("Leave a score (1-10): ")
    while True:
        try:
            score = int(score)
            if(score > 0 and score <= 10):
                break
            else:
                print("Score must be a number from 1 to 10!")
                score = input("Leave a score (1-10): ")
        except:
            print("Score must be a number from 1 to 10!")
            score = input("Leave a score (1-10): ")
    add_review(con, cursor, user_ID, coffee_choice[3], datetime.now().strftime("%d.%m.%Y"), note, score)
        

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
    WHERE Review.Note LIKE '%floral%' OR Coffee.Description LIKE '%floral%'
    GROUP BY Coffee.CoffeeID;
    ''').fetchall()

    print("\nRoastery            | Coffee")
    print("--------------------|----------------")
    for value in coffee_floral:
        print(str(value[0]) + " " * (20 - len(str(value[0]))) + "| " + value[1])
    print()


def user_story_5(cursor: sqlite3.Cursor):
    coffee_not_washed = cursor.execute('''
    SELECT Roastery.Name, Coffee.CoffeeName 
    FROM Coffee 
    NATURAL JOIN Roastery JOIN Batch ON Coffee.BatchID == Batch.BatchID JOIN Farm ON Batch.FarmID == Farm.FarmID 
    JOIN Region ON Farm.RegionID == Region.RegionID  
    WHERE Batch.MethodName NOT LIKE "%washed%" AND Region.Country == "Colombia" OR Region.Country == "Rwanda";
    ''').fetchall()

    print("\nRoastery            | Coffee")
    print("--------------------|----------------")
    for value in coffee_not_washed:
        print(str(value[0]) + " " * (20 - len(str(value[0]))) + "| " + value[1])
    print()


if __name__ == "__main__":
    con, cursor = create_database("test.db")
    user_stories(con, cursor)