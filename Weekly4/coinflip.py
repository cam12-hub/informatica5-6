import random

def main():
    #My codeeeee
    #print("Take a guess on the coin flip game")
    #guess = int(input("Heads = 1 or Tales = 2: "))

    #flip = random.randint(1, 2)
    #if flip == 1:
       #print("Heads")
    #elif flip == 2:
       #print("Tales")

    #if guess >2:
        #print("Invalid option")
    #elif guess == flip:
        #print("Winner")
    #else:
        #print("Loser")

    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        guess = input("Heads or tails?: ").strip().lower()

        print("The coin landed on", flip)

        if guess == flip:
            print("Winner")
            break
        else:
            print("Loser")
            attempts -= 1
            print("Attempts left:", attempts)
            
if __name__ == "__main__":
    main()
