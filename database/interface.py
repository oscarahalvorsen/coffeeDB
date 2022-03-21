
def main():
    choice = getChoice()
    if(choice == "v"):
        # View coffees
        print("Viewing")
    elif(choice == "r"):
        # Review a coffee
        print("Reviewing")

def getChoice():
    choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    while(choice != "v" and choice != "r"):
        print("Choice must be 'v' or 'r'")
        choice = input("Would you like to [v]iew coffee(s) or leave a [r]eview? ").lower()
    return choice

if __name__ == "__main__":
    main()