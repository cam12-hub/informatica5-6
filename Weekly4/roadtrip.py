def main():
    answer = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").title().strip()
    print("We just arrived!")

if __name__ == "__main__":
    main()
