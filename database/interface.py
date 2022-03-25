import sqlite3
from .database import create_database

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

def user_story_1():
    pass


def user_story_2(con: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute('''''')


def user_story_3():
    pass


def user_story_4():
    pass


def user_story_5():
    pass


if __name__ == "__main__":
    main()