def main():
    print("Thanks for eating at Burritos el Primo, please leave a review!")

    rating = float(input("Rate 0-5: "))

    if rating > 4.5:
        print("Perfection")

    elif rating > 4:
        print("Excellent")

    elif rating > 3:
        print("Good")

    elif rating > 2:
        print("Fair")

    else:
        print("Poor")

    print("Thanks for your review come back soon!")

if __name__=="__main__":
    main()
