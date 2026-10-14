import random
def main ():#Define main function
    start_game("random_words.txt")
#Create a txt file containing random words
def start_game(file): #Define a start_game function with 1 parameter
    with open(file) as random_word: #Open the txt file in our start_game funtion
        content = random_word.read().splitlines()#Convert our txt file into a list
        secret_w = random.choice(content)
        secret_w = (["_"] * len(secret_w))
    print("Welcome to hangman game!")
    print("This is your word: ")
    print(" ".join(secret_w))

    while True:
        guess = input("Take a guess: ")
        if len(guess) == 1:
            break
        else:
            print("Invalid guess, type just ONE letter.")

    

if __name__=="__main__":
    main()


