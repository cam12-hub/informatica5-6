def main():
    # planet = input("Planet:")

    # #Separation
    # print("Hello", planet)

    # #Concatenation
    # print("Hello " + planet)

    # #Formatted Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hllo", end=" ")
    # print(planet)

    name = input("What is your name?").strip().title()
    color = input("Tell me a color:").strip().lower()
    adj = input("Give an adjective:").strip().lower()
    goal = input("A goal you would like to achieve:").strip().lower()

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")
    print()
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.".strip().upper())


if __name__ == "__main__":
    main()
