def main():
    not_validated = True

    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1 and number <= 10:
                print ("Success!")
                not_validated = False
            else:
                print("Error")
        except ValueError:
            print("You must enter a number between 1 and 10.")

    while True:
        try:
            name = input("Enter a name:")
            f_letter = name[0]
            print("Name stored successfully.")
            break
        except IndexError:
            print("You MUST enter your name.")

if __name__=="__main__":
    main()
