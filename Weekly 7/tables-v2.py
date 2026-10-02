def main():
    while True:
        print("Welcome to the times table quiz")
        try:
            times_table = int(input("Enter a times table that you would like to be tested on: "))
            break
        except ValueError:
             print("You must enter a NUMBER.")
    if times_table >= 1 and times_table <= 10:
            try:
                max_value = int(input("Enter maximum value for the times table: ")) #
                if max_value >= 1 and max_value <= 10:
                    print(f"Here is your quiz in the {times_table} times table")
            except ValueError:
                print("You must enter a NUMBER.")
            for x in range(1,max_value + 1):
                answer = x * int(times_table)
                print(f"{times_table} x {x}")
                user_answer = int(input("Type an answer: ")) #
                if user_answer == answer:
                    print("Correct!")
                else:
                    print("Incorrect")

if __name__== "__main__":
    main()
