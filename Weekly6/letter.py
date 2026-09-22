def main():
    characters = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser" ]

    for receiver in characters:
        if receiver != "Princess Peach":
        print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {characters[5]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")





if __name__ == "__main__":
    main()
