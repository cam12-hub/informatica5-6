import random

def main():
    name = input("Hello! What's your name? ").strip().title()
    print(f"Well, {name}, I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    print("Take a guess!")
    guess = int(input(""))

    while guess != number:
        if guess > number:
            print("Your number is too high")
            guess = int(input("Take another guess "))
        elif guess < number:
            print("Your number is too low")
            guess = int(input("Take another guess "))
        elif guess == number:
            break
    print(f"Good job, {name}! You guessed my number.")

if __name__ == "__main__":
    main()
