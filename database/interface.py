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
    if(story == 1):
        pass


if __name__ == "__main__":
    main()