def main():
    welcome()
    get_item()




def get_item():
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    choice = input("What would you like to order?: ")
    if choice == "cheeseburger":
        print("Here you go! 🍔")
    elif choice == "fries":
        print("Here you go! 🍟")
    elif choice == "soda":
        print("Here you go! 🥤")
    elif choice == "ice cream":
        print("Here you go! 🍦")
    elif choice == "cookie":
        print("Here you go! 🍪")
    else:
        print("Please choose from the options available")



def welcome():
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to B.B.Town!")
    print("Here's our menu: ")
    for i in range(len(menu)):
        print(f"{i+1} {menu[i]}")


if __name__=="__main__":
    main()
