import random
def main ():#Define main function
    start_game("random_words.txt")
#Create a txt file containing random words
def start_game(file): #Define a start_game function with 1 parameter
    attempts = 10
    with open(file) as random_word: #Open the txt file in our start_game funtion
        content = random_word.read().splitlines()#Convert our txt file into a list
        secret_w = random.choice(content)
        hint = (["_"] * len(secret_w))
        incorrect_letters = []
    while attempts > 0:
        print("Welcome to hangman game!")
        print("This is your word: ")
        print(" ".join(hint))
        while True:
            guess = input("Take a guess: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess, type just ONE letter.")
        if guess in secret_w and guess not in hint:
            for i in range(len(secret_w)):
                if secret_w[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")
        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", secret_w)
            break
    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", secret_w)

if __name__=="__main__":
    main()


