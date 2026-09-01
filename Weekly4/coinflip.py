import random

def main():

    print("Take a guess on the coin flip game")
    guess = int(input("Heads = 1 or Tales = 2: "))

    flip = random.randint(1, 2)
    if flip == 1:
       print("Heads")
    elif flip == 2:
       print("Tales")

    if guess >2:
        print("Invalid option")
    elif guess == flip:
        print("Winner")
    else:
        print("Loser")

if __name__ == "__main__":
    main()
