def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))
    while True:
        print("Welcome to the times table quiz")
        times_table = input("Enter a times table that you would like to be tested on:")
        break

    if times_table in valid_nums:
            max_value = int(input("Enter maximum value for the times table: "))
            print(f"Here is your quiz in the {times_table} times table")
            for x in range(1,max_value + 1):
                user_answer = int(input("Type an answer: "))
    else:
            print("Incorrect")

if __name__== "__main__":
    main()
