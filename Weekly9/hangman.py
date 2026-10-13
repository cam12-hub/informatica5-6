import random
def main ():#Define main function
    start_game("random_words.txt")
#Create a txt file containing random words
def start_game(file): #Define a start_game function with 1 parameter
    with open(file) as random_word: #Open the txt file in our start_game funtion
        content = random_word.read().splitlines()#Convert our txt file into a list
    print(random.choice(content))#Print a word



if __name__=="__main__":
    main()


