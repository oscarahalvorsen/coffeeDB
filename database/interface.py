
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
    

if __name__ == "__main__":
    main()