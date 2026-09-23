def main():
    while True:
        number = int(input("Enter a number (1-10): "))
        if number <= 10:
            print(f"Here is the {number} times table")
            for i in range (1,11):
                result = i * number
                print(f"{i} * {number} = {result}" )
        command = input("Do you wanna keep learning? ").lower().strip()
        if command == "yes":
            continue
        else:
            break






if __name__ == "__main__":
    main()
